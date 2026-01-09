export const appendButton = (text: string, onclick: () => void) => {
  const button = document.createElement("button");
  button.textContent = text;
  button.addEventListener("click", onclick);
  document.body.appendChild(button);
  return button;
};

export const appendInput = (placeholder: string): { value: string } => {
  const input = document.createElement("input");
  input.type = "text";
  input.placeholder = placeholder;
  let value = "";
  input.addEventListener("change", (event) => {
    value = (event.target as HTMLInputElement).value;
  });
  document.body.appendChild(input);
  return {
    get value() {
      return value;
    },
  };
};

export const appendP = (text: string, bold?: boolean) => {
  const p = document.createElement("p");
  p.textContent = text;
  if (bold) {
    p.style.fontWeight = "bold";
  }
  document.body.appendChild(p);
  return p;
};
