<script lang="ts">
  import type { AudiotoolClient, SyncedDocument } from "@audiotool/nexus"
  import {
    audiotoolProjectOpener,
    type ProjectOpener,
  } from "./audiotool-utils/project-opener.svelte"
  import {
    audiotoolProjectLister,
    type ProjectLister,
  } from "./audiotool-utils/project-lister.svelte"
  import type { LoginManager } from "./audiotool-utils/login-manager.svelte"

  let {
    projectOpener,
    projectLister,
  }: {
    projectOpener: ProjectOpener
    projectLister: ProjectLister
  } = $props()

  let inputProjectUrl = $state("")
  $inspect(projectLister.projects)
</script>

<div class="horizontal">
  <!-- create a new project-->
  <div>
    <h2>Create new project</h2>
    <button onclick={() => projectOpener.createProject("New Project")}
      >Create new project</button
    >
  </div>
  <!-- list projects-->
  <div>
    <h2>List projects</h2>
    <button onclick={() => projectLister.list()}>List Projects</button>

    {#if projectLister.projects instanceof Error}
      <p>Error listing projects: {projectLister?.projects.message}</p>
    {:else}
      <ul>
        {#each projectLister.projects as project}
          <li>
            <button onclick={() => projectOpener.openProject(project.name)}>
              {project.displayName}
            </button>
          </li>
        {/each}
      </ul>
    {/if}
  </div>
  <!-- paste project url-->
  <div>
    <h2>Open project</h2>
    <input type="text" bind:value={inputProjectUrl} />
    <button onclick={() => projectOpener.openProject(inputProjectUrl)}>
      Open project</button
    >
  </div>
</div>

<style>
  .horizontal {
    display: flex;
    flex-direction: row;
    margin-top: 20px;
    gap: 10px;
  }
  .horizontal div {
    border: 1px solid #8b8b8b;

    border-radius: 10px;
    padding: 10px;
  }
  .horizontal h2 {
    font-size: 1.2rem;
  }
  li button {
    padding: 1px;
    margin: 2px;
  }
  ul {
    overflow-y: scroll;
    max-height: 200px;
  }
</style>
