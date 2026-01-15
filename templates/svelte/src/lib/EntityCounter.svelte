<script lang="ts">
  import type { SyncedDocument } from "@audiotool/nexus"

  let { nexus }: { nexus: SyncedDocument } = $props()

  let count = $state<number | undefined>(undefined)

  nexus.start().then(() => {
    count = nexus.queryEntities.get().length
  })
</script>

{#if count === undefined}
  <p>Counting entities...</p>
{:else}
  <p>Count: {count}</p>
{/if}
