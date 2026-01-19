import { createAudiotoolClient, getLoginStatus } from "@audiotool/nexus";
import "./style.css";
import { appendButton, appendInput, appendP } from "./ui";

// status tells us if a user logged in. It will say "no" the first time executing.
const status = await getLoginStatus({
  clientId: "de492211-42ba-436e-9837-7f52597bb31e",
  redirectUrl: "http://127.0.0.1:5173/",
  scope: "project:write",
});

// no user logged in - create a login button that triggers the flow
if (status.loggedIn == false) {
  appendButton("Login", () => status.login());
  throw await new Promise(() => {}); // stop executing here
}

// suer logged in - create logout button and display username
appendButton("Logout", () => status.logout());
appendP("logged in as " + (await status.getUserName()));

// start client early to give time to initialize
const client = createAudiotoolClient({ authorization: status });

// create input for project URL
const input = appendInput("Paste project URL");

// allow counting of entities
appendButton("Count Entities", async () => {
  appendP("Counting...");

  // await client, then create a nexus document
  const nexus = await client.then((c) =>
    c.createSyncedDocument({
      project: input.value,
      mode: "online",
    })
  );

  // start syncing, fetching all current entities
  await nexus.start();

  // count entities per type
  const countMap = new Map<string, number>();
  for (const entity of nexus.queryEntities.get()) {
    countMap.set(entity.entityType, (countMap.get(entity.entityType) ?? 0) + 1);
  }

  // print results
  appendP("Counted " + countMap.size + " entities:", true);
  for (const [entityType, count] of countMap.entries()) {
    const p = document.createElement("p");
    p.textContent = `${entityType}: ${count}`;
    document.body.appendChild(p);
  }
});
