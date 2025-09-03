import type { ControlPanel } from "../control-panel";
import {
  EXAMPLE_CREATE_SOUND,
  EXAMPLE_DOWNLOAD_SAMPLES,
  EXAMPLE_CREATE_PROJECT,
  type Example,
} from "./examples";

export const createCatalog = (controlPanel: ControlPanel): HTMLDivElement => {
  const catalog = document.createElement("div");
  catalog.classList.add("catalog");

  // import all examples
  const examples: Example[] = [
    EXAMPLE_CREATE_SOUND,
    EXAMPLE_DOWNLOAD_SAMPLES,
    EXAMPLE_CREATE_PROJECT,
  ];

  const title = document.createElement("h2");
  title.textContent = "Examples Catalog";
  catalog.appendChild(title);

  examples.forEach((example) => {
    const anchor = document.createElement("a");
    anchor.classList.add("example-link");
    anchor.textContent = example.title;
    anchor.href = "#";

    anchor.addEventListener("click", (e) => {
      e.preventDefault();
      controlPanel.loadExample(example);
    });

    catalog.appendChild(anchor);
  });

  return catalog;
};
