import "./style.css";
import { createApp } from "./ui/app.ts";

const initializeApp = async () => {
  const appElement = await createApp();
  document.querySelector<HTMLDivElement>("#app")?.appendChild(appElement);
};

initializeApp().catch((error) => {
  console.error("Failed to initialize app:", error);
  const errorContainer = document.createElement("div");
  errorContainer.innerHTML = `
    <h1>Failed to Initialize Application</h1>
    <p>${error instanceof Error ? error.message : "Unknown error occurred"}</p>
  `;
  document.querySelector<HTMLDivElement>("#app")?.appendChild(errorContainer);
});
