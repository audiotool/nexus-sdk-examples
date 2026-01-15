<script lang="ts">
  import type { SyncedDocument } from "@audiotool/nexus"
  import ProjectSelector from "./SelectProject.svelte"

  let { nexus }: { nexus: SyncedDocument } = $props()

  let count = $state<number | undefined>(undefined)

  nexus.start().then(() => {
    count = nexus.queryEntities.get().length
  })
</script>

<h1>Entity Count</h1>
{#if count === undefined}
  <p>Counting entities...</p>
{:else}
  <p>Count: {count}</p>
{/if}
