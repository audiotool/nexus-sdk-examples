# Audiotool Nexus SDK Examples

A comprehensive collection of examples demonstrating how to use the [Audiotool Nexus SDK](https://rpc.audiotool.com/dev/nexus/) for API usage and document manipulation in Audiotool projects.

## 🚀 What is the Audiotool Nexus SDK?

The Audiotool Nexus SDK is a powerful TypeScript/JavaScript library that enables developers to:

- Create and manage Audiotool projects programmatically
- Access real-time collaborative editing capabilities
- Integrate with Audiotool's API services

## 📚 Available Examples

### 1. **Create Project** (`create-project.ts`)

Creates a new Audiotool project with a custom display name.

**Use Case:** Automating project creation workflows, batch project setup

### 2. **Create Sound** (`create-sound.ts`)

Creates a Tonematrix device on an existing project with a randomly generated pattern and wire it to a free mixer channel.

**Use Case:** Adding devices, creating patterns, setup cables.

### 3. **Download Samples** (`download-samples.ts`)

Downloads samples from a project with specified type filtering.

**Use Case:** Sample extraction, backup systems, sample library organization

### 4. **Read User** (`read-user.ts`)

Reads user data from a given username using the user service.

**Use Case:** Getting user data, user management, user authentication.

### 5. **Count entities** (`count-entities.ts`)

Counts the number of entities of a given type in a project.

**Use Case:** Getting entity count, entity management, entity tracking, stats.

## 🛠️ Getting Started

### Prerequisites

- npm or yarn
- Audiotool account with Personal Access Token (PAT)

### Installation

```bash
# Install dependencies
npm install

# Start the development server
npm run dev
```

The application will be available at `http://localhost:5174`

### Environment Setup

Create a `.env` file in the project root:

```env
VITE_AUDIOTOOL_PAT=at_pat_your_token_here
```

**How to get your Personal Access Token:**

1. Log in to [Audiotool](https://beta.audiotool.com)
2. Go to [RPC Portal](https://rpc.audiotool.com/dev/pats/)
3. Generate a new Personal Access Token

## 🏗️ Development

### Project Structure

```
src/
├── examples/          # Example implementations
│   ├── create-project.ts
│   ├── read-user.ts
│   ├── create-sound.ts
│   ├── download-samples.ts
│   └── types.ts
├── ui/               # User interface components
│   ├── app.ts        # Main application
│   ├── catalog/      # Examples catalog
│   ├── control-panel.ts
│   ├── console-panel.ts
│   └── pat-setup.ts
├── main.ts           # Application entry point
└── style.css         # Global styles
```

## 🔧 Dependencies

- **audiotool-nexus**: The main SDK package
- **TypeScript**: For type safety and development experience
- **Vite**: For fast development and building

## 📖 API Reference

For detailed information about the Audiotool Nexus SDK, visit:

- [SDK Documentation](https://rpc.audiotool.com/dev/nexus/)

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Report Issues**: Found a bug? Open an issue with detailed steps to reproduce
2. **Suggest Examples**: Have an idea for a useful example? Let us know!
3. **Submit PRs**: Implement improvements or new examples
4. **Improve Documentation**: Help make this README and examples clearer

## 🔗 Related Links

- [Audiotool Platform](https://beta.audiotool.com)
- [Nexus SDK Repository](https://github.com/audiotool/nexus-sdk)
- [Audiotool API Documentation](https://rpc.audiotool.com/dev/nexus)

---

**Happy coding with Audiotool Nexus SDK! 🎵**
