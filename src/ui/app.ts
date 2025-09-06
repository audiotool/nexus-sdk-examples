import { createCatalog } from "./catalog";
import { createConsolePanel } from "./console-panel";
import { createControlPanel } from "./control-panel";
import { createPATSetup } from "./pat-setup";

export const AUDIOTOOL_PAT = import.meta.env.VITE_AUDIOTOOL_PAT;

export const createApp = async (): Promise<HTMLElement> => {
  // create app container
  const app = document.createElement("main");
  app.classList.add("app");

  // check if PAT is set

  if (!AUDIOTOOL_PAT || AUDIOTOOL_PAT === "your_personal_access_token_here") {
    // show PAT setup UI if PAT is not configured
    const patSetup = createPATSetup();
    app.appendChild(patSetup);
  } else {
    // initialize audiotool client and show main UI
    try {
      const consolePanel = createConsolePanel();
      const controlPanel = createControlPanel();
      const catalog = createCatalog(controlPanel);

      app.appendChild(catalog);
      app.appendChild(controlPanel.element);
      app.appendChild(consolePanel);
    } catch (error) {
      // show error message if client initialization fails
      const errorContainer = document.createElement("div");
      errorContainer.classList.add("error-container");
      errorContainer.innerHTML = `
        <h2>Error Initializing audiotool Client</h2>
        <p>${
          error instanceof Error ? error.message : "Unknown error occurred"
        }</p>
      `;
      app.appendChild(errorContainer);
    }
  }

  return app;
};
