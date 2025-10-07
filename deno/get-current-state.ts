import { createAudiotoolClient } from "@audiotool/nexus";
import { AT_PAT, AT_PROJECT } from "./setup.ts";

const client = await createAudiotoolClient({
  pat: AT_PAT,
});

const nexus = await client.createSyncedDocument({
  mode: "online",
  project: AT_PROJECT,
});

// In this example, we'll simply print out all current note regions. This is not synced in real time.

// Calling this will fetch the current project state, so we can query it after. See documentation for more details.
await nexus.start();

nexus.queryEntities
  .ofTypes("noteRegion")
  .get()
  .forEach((region) => {
    console.debug(
      `Note Region '${region.fields.region.fields.displayName.value}' has notes:`
    );
    // get all notes...
    const notes = nexus.queryEntities
      .ofTypes("note")
      // pointing to the collection used by the note region
      .pointingTo.entities(region.fields.noteCollection.value.entityId)
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
