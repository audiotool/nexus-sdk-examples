import { createAudiotoolClient, createPATAuth } from "@audiotool/nexus";
import { createDiskWasmLoader } from "@audiotool/nexus/node";
import { AT_PAT, AT_PROJECT } from "./setup.ts";

const client = await createAudiotoolClient({
  auth: createPATAuth(AT_PAT),
  wasm: createDiskWasmLoader(),
});

const nexus = await client.open(AT_PROJECT);

// In this example, we print out when a note region is created, removed, moved, resized, or renamed.

// subscribe to note region creation
nexus.events.onCreate("noteRegion", (region) => {
  // store current name so we can notify from/to name change
  let currentName = region.fields.region.fields.displayName.value;
  // print out name
  console.debug(
    "crated region with name:",
    currentName,
    "at position:",
    region.fields.region.fields.positionTicks.value
  );

  // log change of name
  nexus.events.onUpdate(
    region.fields.region.fields.displayName,
    () => {
      console.debug(
        `renamed region from ${currentName} to ${region.fields.region.fields.displayName.value}`
      );
      currentName = region.fields.region.fields.displayName.value;
    },

    // false so we don't call the callback for the initial value
    false
  );

  // log change of position
  nexus.events.onUpdate(
    region.fields.region.fields.positionTicks,
    () => {
      console.debug("moved region with name:", currentName);
    },
    false
  );

  // log change of size
  nexus.events.onUpdate(
    region.fields.region.fields.durationTicks,
    () => {
      console.debug(
        "resized region with name:",
        currentName,
        "to size:",
        region.fields.region.fields.durationTicks.value
      );
    },
    false
  );

  nexus.events.onPointingTo(region.fields.collection.value, (note) => {
    console.debug("note created in region with name:", currentName);
    // this is more complicated than it needs to be, SDK is still in development!

    // get the entity
    const noteEntity = nexus.queryEntities.mustGetEntity(note.entityId);
    // subscribe to removal; a note can't suddenly point to another region, so we know the only situation where it stops pointing to the parent
    // is when the note is removed.
    nexus.events.onRemove(noteEntity, () => {
      console.debug("note removed from region with name:", currentName);
    });
  });

  return () => {
    console.debug("removed region with name:", currentName);
  };
});

// Start syncing. Will first call the above callbacks will all current regions, then with regions created live in the editor.
await nexus.start();
