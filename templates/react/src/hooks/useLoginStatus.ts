import type { AudiotoolClient } from "@audiotool/nexus";
import { createAudiotoolClient } from "@audiotool/nexus";
import { getLoginStatus } from "@audiotool/nexus/utils";
import { useCallback, useEffect, useRef, useState } from "react";

export type UseLoginStatusResult =
  | { case: "loading" }
  | { case: "loggedIn"; client: AudiotoolClient }
  | { case: "loggedOut"; login: () => void }
  | { case: "error"; error: string; retry: () => void };

export const useLoginStatus = (): UseLoginStatusResult => {
  const [state, setState] = useState<UseLoginStatusResult>({ case: "loading" });
  const isMountedRef = useRef(true);
  const clientId = "de492211-42ba-436e-9837-7f52597bb31e";

  const checkLogin = useCallback(async () => {
    if (!isMountedRef.current) return;
    setState({ case: "loading" });

    try {
      const status = await getLoginStatus({
        clientId,
        redirectUrl: window.location.origin + "/",
        scope: "project:write",
      });

      if (!isMountedRef.current) return;

      if (status.loggedIn) {
        const client = await createAudiotoolClient({
          authorization: status,
        });
        if (!isMountedRef.current) return;
        setState({ case: "loggedIn", client });
      } else {
        setState({
          case: "loggedOut",
          login: status.login,
        });
      }
    } catch (err) {
      if (!isMountedRef.current) return;
      console.error("Login initialization error:", err);
      setState({
        case: "error",
        error: (err as Error).message,
        retry: checkLogin, // This is fine - captures the latest checkLogin
      });
    }
  }, [clientId]);

  useEffect(() => {
    isMountedRef.current = true; // Reset on mount
    checkLogin();

    return () => {
      isMountedRef.current = false;
    };
  }, [checkLogin]);

  return state;
};
