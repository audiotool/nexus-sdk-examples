import { createAudiotoolClient, createPATAuth } from "@audiotool/nexus";
import { createDiskWasmLoader } from "@audiotool/nexus/node";
import { Ticks } from "@audiotool/nexus/utils";
import { AT_PAT, AT_PROJECT } from "./setup.ts";

const client = await createAudiotoolClient({
  auth: createPATAuth(AT_PAT),
  wasm: createDiskWasmLoader(),
});

const nexus = await client.open(AT_PROJECT);

// In this example, we write a melody to the project.

// A note track has to point to a "note track player" entity, which is a device
// that can consume notes. See which devices can consume notes here:
// https://rpc.audiotool.com/dev/nexus/types/entity-types.NoteTrackType.html#player

// We'll create a note track player from scratch and wire it up to make it audible,
// for completeness. We could also just use an existing note track player and attach
// another note track there.

// We must start syncing before we can write notes.
await nexus.start();

// create a transaction. See docs for more details.
const t = await nexus.createTransaction();

// step 1: Crate a device...
const pulv = t.create("pulverisateur", {
  displayName: "My Pulv",
  positionX: 100,
  positionY: 300,
});

// step 2: wire the device up with the mixer, so it becomes audible.
//
// Create a channel strip...

const mixerChannel = t.create("mixerChannel", {});

// wire the pulv with the channel strip
t.create("desktopAudioCable", {
  fromSocket: pulv.fields.audioOutput.location,
  toSocket: mixerChannel.fields.audioInput.location,
});

// now, create a note track, wire up with the pulv
const track = t.create("noteTrack", {
  player: pulv.location,
  // This value orders the tracks visually, amongst all tracks there are in the project.
  // It must be globally unique. We hack this by adding a random number. A better way would be
  // to determine where exactly the note track should be placed:
  // * after/before last/first: add/subtract 1 from last/first
  // * between two tracks: take average of two (this value is float)
  orderAmongTracks: 1000 + Math.random() * 1000,
});

// then we first need a note collection. A collection is pointed to by a note region,
// and by the notes that should lie in that note region. This is because multiple note regions
// could contain the same notes.
const collection = t.create("noteCollection", {});

// now we can create a note region

t.create("noteRegion", {
  // point to the collection
  collection: collection.location,
  track: track.location,
  region: {
    // unless looping is desired, these two values should match
    durationTicks: Ticks.Beat * 4,
    loopDurationTicks: Ticks.Beat * 4,
    // can be left at 0
    loopOffsetTicks: 0,
    // position the region
    positionTicks: 0,
    // can be left at 0, advanced usage only
    collectionOffsetTicks: 0,
    colorIndex: 3,
    displayName: "My Melody",
    isEnabled: true,
  },
});

// now we can add notes to the collection.
[
  {
    positionBeats: 0,
    pitch: 60,
    durationBeats: 1,
  },
  {
    positionBeats: 1,
    pitch: 62,
    durationBeats: 1,
  },
  {
    positionBeats: 1,
    pitch: 64,
    durationBeats: 0.5,
  },
  {
    positionBeats: 1.5,
    pitch: 67,
    durationBeats: 0.5,
  },
  {
    positionBeats: 2,
    pitch: 69,
    durationBeats: 1,
  },
].forEach((note) => {
  t.create("note", {
    collection: collection.location,
    positionTicks: Math.floor(note.positionBeats * Ticks.Beat),
    durationTicks: Math.floor(note.durationBeats * Ticks.Beat),
    pitch: note.pitch,
  });
});

t.send();
console.debug("Melody created");
