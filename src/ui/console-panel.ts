export const createConsolePanel = (): HTMLDivElement => {
  const consolePanel = document.createElement("div");
  consolePanel.classList.add("console-panel");

  const consolePre = document.createElement("pre");
  consolePre.classList.add("console");
  consolePanel.appendChild(consolePre);

  // replace console.clear and console.log with our own functions
  console.clear = () => {
    consolePre.textContent = "";
  };
  const log = console.log
  console.log = (...args: string[]) => {
    log(...args)
    consolePre.textContent += args.join(" ") + "\n";
  };

  return consolePanel;
};
