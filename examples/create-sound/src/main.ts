import { setPAT, setupAudiotoolProject } from "@audiotool/nexus"
import { createArrayTyped } from "@audiotool/nexus/utils"

// get the pat token.
fetch("./pat")
  .then(async (res) => setPAT(await res.text()))
  .catch(() => {
    console.warn("couldn't fetch pat, create ../../pat.txt")
  })

// connect to some project.
const { nexus, api } = await setupAudiotoolProject({
  mode: "online",
  project:
    "https://beta.audiotool.com/studio?project=5a268ba0-d7b3-4fb2-9eb1-fc3f00c4fb29",
})

await nexus.start()

// step 1: we create a tonematrix with a pattern
const t = await nexus.createTransaction()

// tone matrix
const tm = t.create("tonematrix", {})
const tmPath = t.create("tonematrixPattern", {
  // patterns point to a "pattern slot", an empty field in an array. Here we attach it to slot 1. There can be at
  // most 1 pattern per slot. For the tonematrix, there are only 8 slots.
  slot: tm.fields.patterns.array[0].location,
  steps: createArrayTyped(16, () => ({
    notes: createArrayTyped(16, () => Math.random() > 0.74),
  })),
})

// then, we connect the tonematrix to the first channel that doesn't have something pointing to its audio input
const firstFreeChannel = t.entities
  .ofTypes("mixerChannel")
  .get()
  .filter(
    (chan) =>
      t.entities.pointingTo.locations(chan.fields.audioInput.location).get()
        .length === 0
  )[0]

// we expect a free channel to be there since we're in the default project created by the frontend
if (firstFreeChannel === undefined) {
  throw new Error("no new channel found, not sure what to do")
}

// now we connect the tonematrix with that channel using an audio connection
t.create("audioConnection", {
  fromSocket: tm.fields.audioOutput.location,
  toSocket: firstFreeChannel.fields.audioInput.location,
})

// and we're done.
console.debug("hello")
