import type { AudiotoolClient } from "@audiotool/nexus";
import type { Example } from "./catalog/examples";

export type ControlPanel = {
  element: HTMLDivElement;
  loadExample: (example: Example) => void;
};

export const createControlPanel = (
  audiotool: AudiotoolClient
): ControlPanel => {
  const controlPanel = document.createElement("div");
  controlPanel.classList.add("control-panel");

  return {
    element: controlPanel,
    loadExample: (example: Example) => {
      // clear the console
      console.clear();

      // clear the control panel
      controlPanel.innerHTML = "";

      // create title
      const title = document.createElement("h2");
      title.textContent = example.title;
      controlPanel.appendChild(title);

      // create description
      const description = document.createElement("p");
      description.textContent = example.description;
      controlPanel.appendChild(description);

      // create form container
      const form = document.createElement("div");
      form.classList.add("example-form");

      // create input fields for each requirement
      const inputValues: string[] = [];
      example.requirements.forEach((requirement, index) => {
        const inputContainer = document.createElement("div");
        inputContainer.classList.add("input-container");

        const label = document.createElement("label");
        label.textContent = requirement;

        const input = document.createElement("input");
        input.type = "text";
        input.placeholder = `Enter ${requirement.toLowerCase()}`;

        input.addEventListener("input", (e) => {
          const target = e.target as HTMLInputElement;
          inputValues[index] = target.value;
        });

        inputContainer.appendChild(label);
        inputContainer.appendChild(input);
        form.appendChild(inputContainer);
      });

      // create submit button
      const submitButton = document.createElement("button");
      submitButton.textContent = example.actionLabel;
      submitButton.classList.add("submit-button");

      submitButton.addEventListener("click", async () => {
        // validate that all inputs have values
        if (inputValues.some((value) => !value)) {
          console.log("Error: Please fill in all required fields");
          return;
        }

        try {
          submitButton.disabled = true;
          submitButton.textContent = "Executing...";

          await example.action(audiotool, ...inputValues);

          console.log("--------------------------------");
          console.log(`Successfully executed: ${example.title}`);
        } catch (error) {
          console.log(
            `Error executing ${example.title}: ${
              error instanceof Error ? error.message : "Unknown error"
            }`
          );
        } finally {
          submitButton.disabled = false;
          submitButton.textContent = example.actionLabel;
        }
      });

      form.appendChild(submitButton);
      controlPanel.appendChild(form);
    },
  };
};
