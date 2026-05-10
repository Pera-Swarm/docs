
# Pera Swarm Documentation

This site is built with [Sphinx](https://www.sphinx-doc.org/) and MyST Markdown.

## Setup

Install dependencies with uv:

```sh
uv sync
```

## Build

Build the static site into `_site`:

```sh
make build
```

Run the warning-as-error build used by CI:

```sh
make test
```

Serve the site locally with live reload:

```sh
make serve
```

## Writing Pages

Documentation articles live under `docs/`. Add new pages to the `index.md` toctree so they appear in the Sphinx navigation and are included in the build.

Use MyST-compatible front matter when metadata is useful:

```md
---
title: Robot Protocols
description: MQTT robot protocol reference
nav_order: 1
---
```

Use MyST fenced directives for Sphinx features:

````md
```{note}
Under Construction
```
````
