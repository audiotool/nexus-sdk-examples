import { setPAT, setupAudiotoolProject } from "@audiotool/nexus"

const throw_ = () => {
  throw new Error()
}

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
    "https://beta.audiotool.com/studio?project=0410b64e-ba1c-477e-a995-7e2bc1697576",
})

await nexus.start()

// Here we just query the document once; the list won't refresh if we add sample regions, to focus
// on downloading samples

// Get the list of all audio regions.
for (const region of nexus.queryEntities.ofTypes("audioRegion").get()) {
  // First, we retrieve the sample entity that the region points to
  const sampleEntity = nexus.queryEntities.mustGetEntityAs(
    region.fields.sample.value.entityId,
    "sample"
  )

  // The is the sample "name", the identifier used in the backend...
  const sampleName = sampleEntity.fields.sampleId.value

  // we can call getSample using the name to get more infos on the sample
  const sampleInfo = await api.sampleService.getSample({ name: sampleName })
  if (sampleInfo instanceof Error) {
    throw new Error("couldn't fetch sample info for audio region", {
      cause: sampleInfo,
    })
  }
  console.debug("Infos about this sample:", sampleInfo?.sample)

  // Now we download the mp3 of the sample. There's also flac & wav.
  const mp3Data = await fetch(sampleInfo.sample?.mp3Url ?? throw_()).then(
    (res) => res.arrayBuffer()
  )

  // And we're done!

  // The rest of this file just adds the sample to a list of samples that we can play on click.

  const wrapper = document.createElement("div")

  const audio = document.createElement("audio")
  const blob = new Blob([mp3Data], { type: "audio/flac" })
  const url = URL.createObjectURL(blob)
  audio.src = url

  const playButton = document.createElement("button")
  playButton.textContent = "Play"

  const nameLabel = document.createElement("span")
  nameLabel.textContent = region.fields.region.fields.displayName.value

  wrapper.append(playButton, nameLabel)
  document.getElementById("app")?.appendChild(wrapper)

  // promise resolves when playback ends
  const stopPromise = new Promise<void>((res) => {
    audio.onended = () => {
      URL.revokeObjectURL(url)
      res()
    }
  })

  playButton.addEventListener("click", () => {
    audio.play()
  })
  await stopPromise
}
