import { type AudiotoolClient } from "audiotool-nexus";

/**
 * Read user data given a username using the user service
 * @param audiotool - The audiotool client
 * @param username - The username to look up (e.g., "users/kepz")
 * @returns The user information
 * @throws {Error} If user lookup fails
 */
export const readUser = async (
  audiotool: AudiotoolClient,
  username: string
) => {
  // STEP 1: get user data using the user service
  const result = await audiotool.api.userService.getUser({
    name: "users/" + username,
  });

  // STEP 2: check if the operation was successful
  if (result instanceof Error) {
    throw new Error(`Failed to read user data: ${result.message}`);
  }

  if (result.user === undefined) {
    throw new Error("User not found");
  }

  // STEP 3: return the user information
  return {
    name: result.user.name,
    displayName: result.user.displayName,
    followers: result.user.numFollowers,
    following: result.user.numFollowing,
  };
};
