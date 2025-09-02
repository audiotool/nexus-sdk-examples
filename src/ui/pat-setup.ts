export const createPATSetup = (): HTMLElement => {
  const container = document.createElement("div");
  container.classList.add("pat-setup");

  const title = document.createElement("h1");
  title.textContent = "Audiotool setup required";
  title.classList.add("pat-setup-title");

  const message = document.createElement("p");
  message.textContent =
    "To use this application, you need to set up your Audiotool Personal Access Token (PAT).";
  message.classList.add("pat-setup-message");

  const instructions = document.createElement("div");
  instructions.classList.add("pat-setup-instructions");

  const step1 = document.createElement("p");
  step1.innerHTML =
    "<strong>Step 1:</strong> Copy the <code>.env.example</code> file to <code>.env</code>";

  const step2 = document.createElement("p");
  step2.innerHTML =
    "<strong>Step 2:</strong> Edit the <code>.env</code> file and replace <code>your_personal_access_token_here</code> with your actual PAT";

  const step3 = document.createElement("p");
  step3.innerHTML = "<strong>Step 3:</strong> Restart the development server";

  const note = document.createElement("p");
  note.innerHTML = `<strong>Note:</strong> You can get your PAT from the <a href="https://rpc.audiotool.com/dev" target="_blank">Audiotool RCP dashboard</a>`;
  note.classList.add("pat-setup-note", "text-muted-italic");

  instructions.appendChild(step1);
  instructions.appendChild(step2);
  instructions.appendChild(step3);

  container.appendChild(title);
  container.appendChild(message);
  container.appendChild(instructions);
  container.appendChild(note);

  return container;
};
