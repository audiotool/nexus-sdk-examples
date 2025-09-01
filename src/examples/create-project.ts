import { type AudiotoolClient } from "@audiotool/nexus";

/**
 * Create a new project using the project service
 * @param audiotool - The audiotool client
 * @param displayName - The display name for the new project
 * @returns The created project information
 * @throws {Error} If project creation fails
 */
export const createProject = async (
  audiotool: AudiotoolClient,
  displayName: string
) => {
  // STEP 1: create a new project using the project service
  const result = await audiotool.api.projectService.createProject({
    project: {
      displayName,
    },
  });

  // STEP 2: check if the operation was successful
  if (result instanceof Error) {
    throw new Error(`Failed to create project: ${result.message}`);
  }

  if (result.project === undefined) {
    throw new Error("Failed to create project");
  }

  // STEP 3: return the created project information
  return {
    name: result.project.name,
    displayName: result.project.displayName,
    creatorName: result.project.creatorName,
    url: result.project.name.replace(
      "projects/",
      "https://beta.audiotool.com/studio?project="
    ),
  };
};
