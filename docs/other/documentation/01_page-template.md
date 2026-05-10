---
title: "Page Template"
nav_order: 1
---

## Page Template

Use MyST-compatible front matter at the top of each Markdown file when page metadata is needed.

```md
---
title: Robot Protocols # title of the page
description: MQTT robot protocol reference
nav_order: 1 # used by maintainers when ordering pages in the Sphinx toctree
---
```

Add pages to the root `index.rst` toctree so Sphinx includes them in the build and navigation.

Possible Markdown techniques can be found in [Markdown Techniques](2_markdown.md).

Sphinx-specific directives can be written with MyST fenced directives, for example admonitions and toctrees.
