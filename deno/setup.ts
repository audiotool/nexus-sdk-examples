import { throw_ } from "@audiotool/nexus/utils";

export const AT_PROJECT =
  Deno.env.get("AT_PROJECT") ?? throw_("missing AT_PROJECT env var");
export const AT_PAT =
  Deno.env.get("AT_PAT") ?? throw_("missing AT_PAT env var");
