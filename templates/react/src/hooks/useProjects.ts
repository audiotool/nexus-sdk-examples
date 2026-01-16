import type { AudiotoolClient } from "@audiotool/nexus";
import { useCallback, useEffect, useRef, useState } from "react";

export type Project = {
  name: string;
  displayName: string;
  coverUrl: string;
  updateTime: Date | null;
};

export type UseProjectsResult =
  | { case: "loading" }
  | {
      case: "loaded";
      projects: Project[];
      refresh: () => void;
      loadMore: () => void;
      hasMore: boolean;
      isLoadingMore: boolean;
      createProject: (displayName: string) => Promise<Project | null>;
      isCreating: boolean;
    }
  | { case: "error"; error: string; retry: () => void };

const PAGE_SIZE = 10;

/**
 * Fetches and manages user projects with pagination and creation.
 *
 * @param client - Authenticated client or null. Pass null when logged out.
 *
 * @example
 * ```tsx
 * const result = useProjects(client)
 * if (result.case === 'loaded') {
 *   return (
 *     <div>
 *       {result.projects.map(p => <div key={p.name}>{p.displayName}</div>)}
 *       {result.hasMore && <button onClick={result.loadMore}>Load More</button>}
 *       <button onClick={() => result.createProject('New')}>Create</button>
 *     </div>
 *   )
 * }
 * ```
 */
export function useProjects(client: AudiotoolClient | null): UseProjectsResult {
  const [projects, setProjects] = useState<Project[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [isLoadingMore, setIsLoadingMore] = useState(false);
  const [isCreating, setIsCreating] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [nextPageToken, setNextPageToken] = useState<string | undefined>(
    undefined
  );
  const clientRef = useRef(client);
  clientRef.current = client;

  const fetchProjects = useCallback(async (pageToken?: string) => {
    const currentClient = clientRef.current;
    if (!currentClient) {
      setIsLoading(true);
      return;
    }

    if (!pageToken) {
      setIsLoading(true);
      setError(null);
    } else {
      setIsLoadingMore(true);
    }

    const response = await currentClient.api.projectService.listProjects({
      pageSize: PAGE_SIZE,
      orderBy: "project.update_time desc",
      pageToken,
    });

    if (response instanceof Error) {
      console.error("Failed to fetch projects:", response);
      setError(response.message);
      setIsLoading(false);
      setIsLoadingMore(false);
      return;
    }

    const newProjects: Project[] = response.projects.map((p) => ({
      name: p.name,
      displayName: p.displayName || "Untitled Project",
      coverUrl: p.coverUrl,
      updateTime: p.updateTime
        ? new Date(Number(p.updateTime.seconds) * 1000)
        : null,
    }));

    if (pageToken) {
      setProjects((prev) => [...prev, ...newProjects]);
    } else {
      setProjects(newProjects);
    }

    setNextPageToken(response.nextPageToken || undefined);
    setIsLoading(false);
    setIsLoadingMore(false);
  }, []);

  const refresh = useCallback(() => {
    setNextPageToken(undefined);
    fetchProjects();
  }, [fetchProjects]);

  const loadMore = useCallback(() => {
    if (nextPageToken && !isLoadingMore) {
      fetchProjects(nextPageToken);
    }
  }, [nextPageToken, isLoadingMore, fetchProjects]);

  const createProject = useCallback(
    async (displayName: string): Promise<Project | null> => {
      const currentClient = clientRef.current;
      if (!currentClient) return null;

      setIsCreating(true);
      const createResponse =
        await currentClient.api.projectService.createProject({
          project: { displayName },
        });

      if (createResponse instanceof Error) {
        console.error("Failed to create project:", createResponse);
        setIsCreating(false);
        return null;
      }

      if (createResponse.project) {
        const newProject: Project = {
          name: createResponse.project.name,
          displayName: createResponse.project.displayName || displayName,
          coverUrl: createResponse.project.coverUrl,
          updateTime: createResponse.project.updateTime
            ? new Date(Number(createResponse.project.updateTime.seconds) * 1000)
            : null,
        };
        // Refresh the list to include the new project at the top
        await fetchProjects();
        setIsCreating(false);
        return newProject;
      }

      setIsCreating(false);
      return null;
    },
    [fetchProjects]
  );

  useEffect(() => {
    if (client) {
      fetchProjects();
    }
  }, [client, fetchProjects]);

  if (isLoading) {
    return { case: "loading" };
  }

  if (error) {
    return {
      case: "error",
      error,
      retry: refresh,
    };
  }

  return {
    case: "loaded",
    projects,
    refresh,
    loadMore,
    hasMore: !!nextPageToken,
    isLoadingMore,
    createProject,
    isCreating,
  };
}
