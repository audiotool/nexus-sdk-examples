import { type AudiotoolClient } from "audiotool-nexus";

/**
 * Count entities of a given type in a project and return their IDs
 * @param audiotool - The audiotool client
 * @param project - The project URL to connect to
 * @param entityType - The type of entities to count (e.g., "tonematrix", "mixerChannel", "sample")
 * @returns Object containing count and array of entity IDs
 * @throws {Error} If connection or query fails
 */
export const countEntities = async (
  audiotool: AudiotoolClient,
  project: string,
  entityType: string
) => {
  // STEP 1: connect to the given project
  const nexus = await audiotool.createSyncedDocument({
    mode: "online",
    project,
  });

  await nexus.start();

  // STEP 2: query entities of the specified type
  const entities = nexus.queryEntities.ofTypes(entityType).get();

  // STEP 3: extract entity IDs and return count information
  const entityIds = entities.map((entity) => entity.id);

  return {
    count: entities.length,
    entityIds,
    entityType,
  };
};
