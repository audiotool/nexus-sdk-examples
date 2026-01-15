import type { AudiotoolClient, SyncedDocument } from "@audiotool/nexus"
import type { Project } from "@audiotool/nexus/api"
import { throw_ } from "@audiotool/nexus/utils"
import type { LoginManager } from "./login-manager.svelte"

/** an abstraction to make opening projects easier in svelte.
 *
 * Only the first call to either openProject or createProject will have an effect since
 * currently at most one project can be opened at a time - this will change soon.
 *
 * This requires authentication that's passed in on creation. The synced document is only
 * created once authentication is successful.
 */

export type ProjectOpener = {
  /** changes based on the call to openProject or createProject. */
  openedProject: ProjectOpeningStatus
  /** Open an existing project - either a project object, an url to a project on beta.audiotool.com, or a backend identifier. */
  openProject: (projectOrId: Project | string) => void
  /** create a new project with a given display name. */
  createProject: (displayName: string) => void
}

export type ProjectOpeningStatus =
  /** no project selected. */
  | undefined
  /** project selected, loading in progress. */
  | {
      type: "loading"
    }
  /** something went wrong. */
  | { type: "error"; error: Error }
  /** project is ready to use. */
  | { type: "ready"; nexus: SyncedDocument }

export const audiotoolProjectOpener = (
  loginManager: LoginManager
): ProjectOpener => {
  // set when createProject or openProject is called.
  let selectedProjectUrl = $state<
    | {
        type: "id"
        value: string
      }
    | {
        type: "name"
        value: string
      }
    | undefined
  >(undefined)

  // the return value of the document
  let nexus = $state<
    | undefined
    | {
        type: "loading"
      }
    | { type: "error"; error: Error }
    | { type: "ready"; nexus: SyncedDocument }
  >(undefined)

  $effect(() => {
    if (selectedProjectUrl === undefined) {
      return
    }
    if (loginManager.status.type !== "logged-in") {
      return
    }
    // loading already in progress, we currently can't load documents twice.
    if (nexus !== undefined) {
      return
    }

    nexus = { type: "loading" }
    loadProject(
      loginManager.status.client,
      selectedProjectUrl.value,
      selectedProjectUrl.type === "name"
    ).then(
      (n) =>
        (nexus =
          n instanceof Error
            ? { type: "error", error: n }
            : { type: "ready", nexus: n })
    )
  })

  return {
    // reactive return
    get openedProject() {
      return nexus
    },
    createProject: (displayName: string) => {
      selectedProjectUrl = { type: "name", value: displayName }
    },
    openProject: (projectOrId: Project | string) => {
      selectedProjectUrl = {
        type: "id",
        value: typeof projectOrId === "string" ? projectOrId : projectOrId.name,
      }
    },
  }
}
/** loads a project, creates one if needed  */
const loadProject = async (
  client: AudiotoolClient,
  displayNameOrName: string,
  isDisplayName: boolean
): Promise<SyncedDocument | Error> => {
  let projectName: string
  if (isDisplayName) {
    const response = await client.api.projectService.createProject({
      project: { displayName: displayNameOrName },
    })
    if (response instanceof Error) {
      return response
    }
    projectName =
      response.project?.name ?? throw_("bug: no project name returned")
  } else {
    projectName = displayNameOrName
  }
  return client.createSyncedDocument({
    mode: "online",
    project: projectName,
  })
}
