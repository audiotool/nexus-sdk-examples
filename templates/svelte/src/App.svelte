<script lang="ts">
  import { throw_ } from "@audiotool/nexus/utils"
  import { audiotoolLoginManager } from "./lib/audiotool-utils/login-manager.svelte"
  import Login from "./lib/Login.svelte"
  import SelectProject from "./lib/SelectProject.svelte"
  import type { AudiotoolClient } from "@audiotool/nexus"
  import EntityCounter from "./lib/EntityCounter.svelte"
  import { audiotoolProjectLister } from "./lib/audiotool-utils/project-lister.svelte"
  import {
    audiotoolProjectOpener,
    type NexusStatus,
  } from "./lib/audiotool-utils/project-opener.svelte"

  const loginManager = audiotoolLoginManager({
    clientId: "de492211-42ba-436e-9837-7f52597bb31e",
    redirectUrl:
      // define redirect URL depending on whether we're deployed
      import.meta.env.MODE === "development"
        ? "http://127.0.0.1:5173/"
        : throw_("redirect url not set for production"),
    scope: "project:write",
  })

  let projectOpener = audiotoolProjectOpener(loginManager)
  let projectLister = audiotoolProjectLister(loginManager)
  let nexus = $derived<NexusStatus>(projectOpener.nexus)
</script>

<Login {loginManager} />

{#if nexus === undefined}
  <SelectProject {projectOpener} {projectLister} />
{:else if nexus.type === "loading"}
  <p>Opening project...</p>
{:else if nexus.type === "error"}
  <p>Error opening project: {nexus.error.message}</p>
{:else}
  <EntityCounter nexus={nexus.nexus} />
{/if}
