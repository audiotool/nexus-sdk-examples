# Nexus SDK Examples

This project demonstrates how to use the audiotool-nexus SDK with various examples.

## Features

- **Examples Catalog**: Browse and select from available examples
- **Dynamic Control Panel**: Load examples with input fields for requirements
- **Console Output**: View execution results and errors
- **Personal Access Token Setup**: Configure your audiotool credentials

## Available Examples

1. **Create Sound**: Create a sound with a project URL
2. **Download Samples**: Download samples from a project with specified type
3. **Set Personal Access Token**: Configure your personal access token

## How to Use

1. **Setup**: Configure your Personal Access Token (PAT) in the environment
2. **Browse**: Click on any example in the catalog to load it
3. **Configure**: Fill in the required input fields for your selected example
4. **Execute**: Click the action button to run the example
5. **Monitor**: View results and any errors in the console panel

## Development

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build
```

## Environment Variables

Set `VITE_AUDIOTOOL_PAT` in your `.env` file with your audiotool Personal Access Token.

## Project Structure

- `src/examples/` - Example definitions and implementations
- `src/ui/` - UI components (catalog, control panel, console)
- `src/main.ts` - Application entry point
