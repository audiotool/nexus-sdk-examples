# Plain Typescript Template

This is the template without framework like react.

## Getting Started

Open this directory in the terminal, then call:

```
npm install
```

to install all dependencies.

To run the dev server, run

```
npm run dev
```

This will show something like this:

```

  ROLLDOWN-VITE v7.2.5  ready in 104 ms

  ➜  Local:   http://127.0.0.1:5173/
  ➜  press h + enter to show help

```

Open this URL in the browser and start hacking!

## Updating the package

When we release new versions of the package (visible [here](https://developer.audiotool.com/js-package-documentation/documents/%F0%9F%93%9C_Changelog.html)) you can update it by calling:

```
npm install @audiotool/nexus
```

## Contained in this repository

A few utility methods were placed in `lib/audiotool-utils` that wraps the API from the `@audiotool/nexus` package such that they're more
comfortable to use in svelte.

Notice that the file names end with `.svelte.ts` which allows them to use `$state` and `$effect`.

To design your own method like these, it's worth reading on the [exact semantics of `$state`](https://svelte.dev/docs/svelte/$state#Passing-state-across-modules).

There are utilities to:

- get & manage the login status
- list current projects
- open projects as synced documents

Note that **currently, at most one document can be opened per tab**. This is a limitation that will go away soon.
