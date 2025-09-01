import { hasPAT, setPAT } from "@audiotool/nexus"

const app = document.getElementById("app") as HTMLDivElement

function render() {
    if (!app) return
    app.innerHTML = ""

    // Check if PAT is already set
    if (hasPAT()) {
        showPATSetView()
    } else {
        showPATInputView()
    }
}

function showPATSetView() {
    const status = document.createElement("p")
    status.textContent = "✓ Personal Access Token is set"

    const clearButton = document.createElement("button")
    clearButton.textContent = "Clear PAT"
    clearButton.onclick = () => {
        setPAT("")
        render()
    }

    app.append(status, clearButton)
}

function showPATInputView() {
    const instructions = document.createElement("p")
    instructions.textContent = "Enter your Personal Access Token to authenticate with the Audiotool API:"

    const label = document.createElement("label")
    label.textContent = "Personal Access Token:"

    const input = document.createElement("input")
    input.type = "text"
    input.placeholder = "at_pat_..."
    input.id = "pat-input"

    const submitButton = document.createElement("button")
    submitButton.textContent = "Set PAT"
    submitButton.onclick = () => {
        const token = input.value.trim()
        if (token) {
            setPAT(token)
            render()
        }
    }

    const clearButton = document.createElement("button")
    clearButton.textContent = "Clear PAT"
    clearButton.onclick = () => {
        setPAT("")
        render()
    }

    // Add Enter key support for input
    input.addEventListener("keypress",   (e) => {
        if (e.key === 'Enter') {
            submitButton.click()
        }
    })

    app.append(instructions, label, input, submitButton, clearButton)
}

// Initialize the app
render()


