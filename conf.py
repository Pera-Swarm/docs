from datetime import datetime

project = "Pera Swarm Documentation"
author = "Pera Swarm"
release = "v1.0.0"
copyright = f"{datetime.now().year}, Pera-Swarm | Department of Computer Engineering, University of Peradeniya"

extensions = [
    "myst_parser",
    "sphinxcontrib.mermaid",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

exclude_patterns = [
    "_build",
    "_site",
    ".venv",
    "docs/index.rst",
    "README.md",
]

html_title = project
html_baseurl = "https://pera-swarm.ce.pdn.ac.lk/docs/"
html_theme = "sphinx_rtd_theme"
html_logo = "assets/images/logo.png"
html_favicon = "assets/images/favicon.ico"

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_image",
]
myst_heading_anchors = 3
suppress_warnings = [
    "myst.header",
    "myst.xref_missing",
]
