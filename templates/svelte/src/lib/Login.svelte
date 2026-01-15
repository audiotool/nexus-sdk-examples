<script lang="ts">
  import type { LoginManager } from "./audiotool-utils/login-manager.svelte"

  const { loginManager }: { loginManager: LoginManager } = $props()

  let status = $derived(loginManager.status)
</script>

{#if status.type === "loading"}
  <p>Loading...</p>
{:else if status.type === "logged-in"}
  <p>Logged in as {status.userName}</p>
{:else if status.type === "logged-out"}
  <p>Logged out</p>
  <button onclick={status.login}>Login</button>
{:else if status.type === "error"}
  <p>Error: {status.error.message}</p>
  <button onclick={status.recover}>Try again</button>
{/if}

{#if status.type === "logged-in"}
  <button onclick={status.logout}>Logout</button>
{/if}
