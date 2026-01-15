import {
  createAudiotoolClient,
  getLoginStatus,
  type AudiotoolClient,
} from "@audiotool/nexus";

/** Managed login in the current tab */
export type LoginManager = {
  readonly status: SvelteLoginStatus;
};

export type SvelteLoginStatus =
  /** waiting for login status */
  | {
      type: "loading";
    }
  /** status is logged in  */
  | {
      type: "logged-in";
      userName: string;
      logout: () => void;
      client: AudiotoolClient;
    }
  /** status is logged out  */
  | {
      type: "logged-out";
      login: () => void;
    }
  /** something went wrong */
  | {
      type: "error";
      error: Error;
      recover: () => void;
    };

export const audiotoolLoginManager = (
  ...props: Parameters<typeof getLoginStatus>
): LoginManager => {
  let status = $state<SvelteLoginStatus>({ type: "loading" });
  getLoginStatus(...props).then(async (s) => {
    if (s.loggedIn) {
      const userName = await s.getUserName();
      if (userName instanceof Error) {
        status = {
          type: "error",
          error: userName,
          recover: () => window.location.reload(),
        };
        return;
      }
      status = {
        type: "logged-in",
        logout: s.logout,
        userName,
        client: await createAudiotoolClient({ authorization: s }),
      };
      return;
    }
    if (s.error !== undefined) {
      status = { type: "error", error: s.error, recover: s.login };
      return;
    }
    status = { type: "logged-out", login: s.login };
  });
  return {
    get status(): SvelteLoginStatus {
      return status;
    },
  };
};
