import { createAudiotoolClient, createPATAuth } from "@audiotool/nexus";
import { createDiskWasmLoader } from "@audiotool/nexus/node";
import { AT_PAT, AT_PROJECT } from "./setup.ts";

const client = await createAudiotoolClient({
  auth: createPATAuth(AT_PAT),
  wasm: createDiskWasmLoader(),
});

const nexus = await client.open(AT_PROJECT);

// In this example, we'll simply print out all current note regions. This is not synced in real time.

console.debug("Starting...");
// Calling this will fetch the current project state, so we can query it after. See documentation for more details.
await nexus.start();

const noteRegions = nexus.queryEntities.ofTypes("noteRegion").get();

if (noteRegions.length > 0) {
  noteRegions.forEach((region) => {
    console.debug(
      `Note Region '${region.fields.region.fields.displayName.value}' has notes:`
    );
    // get all notes...
    const notes = nexus.queryEntities
      .ofTypes("note")
      // pointing to the collection used by the note region
      .pointingTo.entities(region.fields.collection.value.entityId)
      .get()
      // map to a more readable format
      .map((note) => {
        return {
          position: note.fields.positionTicks.value,
          pitch: note.fields.pitch.value,
          duration: note.fields.durationTicks.value,
        };
      });

    console.table(notes);
  });
} else {
  console.debug("No note regions in this project.");
}

await nexus.stop();
