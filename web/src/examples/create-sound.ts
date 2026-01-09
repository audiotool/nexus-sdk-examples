import { type AudiotoolClient } from "@audiotool/nexus";
import { createTypedArray } from "@audiotool/nexus/utils";

/**
 * Create a sound with a tonematrix in the specified project
 * @param audiotool - The audiotool client
 * @param project - The project URL
 * @throws {Error} If no free channel is found
 */
export const createSound = async (
  audiotool: AudiotoolClient,
  project: string
) => {
  // STEP 1: connect to the given project
  const nexus = await audiotool.createSyncedDocument({
    mode: "online",
    project,
  });

  await nexus.start();

  // STEP 2: create a transaction to work on
  const t = await nexus.createTransaction();

  // STEP 3: create a tonematrix with a pattern and a desktop placement
  const tm = t.create("tonematrix", {});

  // this creates a pattern for the tonematrix
  t.create("tonematrixPattern", {
    // patterns point to a "pattern slot", an empty field in an array. Here we attach it to slot 1. There can be
    // at most 1 pattern per slot. For the tonematrix, there are only 8 slots.
    slot: tm.fields.patternSlots.array[0].location,
    steps: createTypedArray(16, () => ({
      notes: createTypedArray(16, () => Math.random() > 0.74),
    })),
  });

  // STEP 4: connect the tonematrix to the first channel that doesn't have
  //         something pointing to its audio input
  let freeChannel = t.entities
    .ofTypes("mixerChannel")
    .get()
    .filter(
      (channel) =>
        t.entities.pointingTo
          .locations(channel.fields.audioInput.location)
          .get().length === 0
    )[0];

  // as for this example we expect a free channel to be there on the given
  // project
  if (freeChannel === undefined) {
    freeChannel = t.create("mixerChannel", {
      displayParameters: {
        orderAmongStrips:
          // get the max of all existing channels, add 1
          t.entities
            .ofTypes(
              "mixerChannel",
              "mixerGroup",
              "mixerAux",
              "mixerDelayAux",
              "mixerReverbAux"
            )
            .get()
            .reduce(
              (max, channel) =>
                Math.max(
                  max,
                  channel.fields.displayParameters.fields.orderAmongStrips.value
                ),
              0
            ) + 1,
      },
    });
  }

  // STEP 5: connect the tonematrix with that channel using an audio connection
  t.create("desktopAudioCable", {
    fromSocket: tm.fields.audioOutput.location,
    toSocket: freeChannel.fields.audioInput.location,
  });

  // STEP 6: send the transaction
  t.send();

  // ...and we're done!
};
