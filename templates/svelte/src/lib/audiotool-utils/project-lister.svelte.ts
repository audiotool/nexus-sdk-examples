import type { AudiotoolClient } from "@audiotool/nexus"
import type { Project } from "@audiotool/nexus/api"
import type { SvelteLoginStatus } from "./login-manager.svelte"

/** A utility to list projects. Pass in a  login manager, get projects listed once login succeeds.
 *
 * Careful - you might get rate limited if this is called too often. Might modify to only list a few projects at a time.
 */

export type ProjectLister = {
  /** the projects. undefined while loading or not logged in. */
  projects: Project[] | undefined | Error
  list: () => void
}

export const audiotoolProjectLister = (loginStatus: {
  readonly status: SvelteLoginStatus
}): ProjectLister => {
  let projects: Project[] | undefined | Error = $state(undefined)

  // flag changing fast to make sure we only fetch projects once.
  let loadingStarted = $state(false)
  let list = $state<boolean>(false)
  $effect(() => {
    if (loginStatus.status.type !== "logged-in") {
      return
    }
    if (!list) {
      return
    }
    if (loadingStarted) {
      return
    }
    console.debug("listing!")
    loadingStarted = true
    fetchProjects(loginStatus.status.client).then((ps) => {
      projects = ps
    })
  })
  return {
    // reactive return
    get projects() {
      return projects
    },
    list: () => {
      list = true
    },
  }
}
const fetchProjects = async (
  client: AudiotoolClient
): Promise<Project[] | Error> => {
  let nextPageToken = ""
  let projects: Project[] = []
  do {
    const response = await client.api.projectService.listProjects({
      pageSize: 100,
      pageToken: nextPageToken,
    })
    if (response instanceof Error) {
      return response
    }
    console.debug("fetched", response.projects?.length)
    projects.push(...response.projects)
    nextPageToken = response.nextPageToken
  } while (nextPageToken !== "" && nextPageToken !== undefined)

  return projects
}
