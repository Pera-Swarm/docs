
# Usage instructions

You can find the current documentation articles in the directory, './docs/'. Can use any folder structure for organize the md files.
Use the header file start three dashes and end with three dashes for define the properties of each page.

```md
---
layout: default                 # keep it as 'default'
parent: MQTT                    # title of the parent article in the navigation tree
grand_parent: Communication     # optional, use if the article is a grandchild in the navigation tree
title: Robot Protocols          # title of the page
nav_order: 1                    # You can use this number to define the order the items in navigation bar. otherwise it will use alphabetical order
permalink: communication/mqtt   # this is the actual url of the article (Here, https://pera-swarm.ce.pdn.ac.lk/docs/communication/mqtt.html)
has_children: true              # Make this true if there any child pages under this page
---
```

More details on these properties can be found in [Navigation Structure](https://pmarsceill.github.io/just-the-docs/docs/navigation-structure/)

Possible Markdown techniques can be found in [here](https://pera-swarm.ce.pdn.ac.lk/docs/markdown-tech) and you can see the syntax from [here](https://raw.githubusercontent.com/Pera-Swarm/docs/main/docs/theme/index-test.md).

Please refer [typography details](https://pmarsceill.github.io/just-the-docs/docs/utilities/typography/) and [layout options](https://pmarsceill.github.io/just-the-docs/docs/utilities/layout/) for any advanced uses.
