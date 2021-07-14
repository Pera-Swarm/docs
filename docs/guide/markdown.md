---
layout: default
title: Markdown Formats
nav_order: 2
permalink: documentation/markdown
parent: Useful Links

search_exclude: true
sitemap: false

gh_link: docs/guide/markdown.md
---

# Markdown Formats
{: .no_toc }

## Typography

Text can be **bold**, _italic_, or ~~strikethrough~~.

<span style="color:orange; padding-bottom:0;" >Markdown Syntax:</span>
```md
Text can be **bold**, _italic_, or ~~strikethrough~~.
```

[Link to another page](another-page)

[Link to page with new tab](https://www.google.com/){:target="_blank"}

<span style="color:orange; padding-bottom:0;" >Markdown Syntax:</span>
```md
[Link to another page](another-page)
[Link to page with new tab](https://www.google.com/){:target="_blank"}
```

There should be whitespace between paragraphs.

There should be whitespace between paragraphs. We recommend including a README, or a file with information about your project.

<span style="color:orange; padding-bottom:0;" >Markdown Syntax:</span>
```md
# Header 1
## Header 2
## Header 3
### Header 4
#### Header 5
##### Header 6
###### Header 7
```

# [](#header-1)Header 1

This is a normal paragraph following a header. GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.

## [](#header-2)Header 2

> This is a blockquote following a header.
>
> When something is important enough, you do it even if the odds are not in your favor.

### [](#header-3)Header 3

```js
// Javascript code with syntax highlighting.
var fun = function lang(l) {
  dateformat.i18n = require('./lang/' + l)
  return true;
}
```

```ruby
# Ruby code with syntax highlighting
GitHubPages::Dependencies.gems.each do |gem, version|
  s.add_dependency(gem, "= #{version}")
end
```

#### [](#header-4)Header 4

*   This is an unordered list following a header.
*   This is an unordered list following a header.
*   This is an unordered list following a header.

##### [](#header-5)Header 5

1.  This is an ordered list following a header.
2.  This is an ordered list following a header.
3.  This is an ordered list following a header.

###### [](#header-6)Header 6


| head1        | head two          | three |
|:-------------|:------------------|:------|
| ok           | good swedish fish | nice  |
| out of stock | good and plenty   | nice  |
| ok           | good 'oreos'      | hmm   |
| ok           | good 'zoute' drop | yumm  |

<span style="color:orange; padding-bottom:0;" >Markdown Syntax:</span>
```md
| head1        | head two          | three |
|:-------------|:------------------|:------|
| ok           | good swedish fish | nice  |
| out of stock | good and plenty   | nice  |
| ok           | good `oreos`      | hmm   |
| ok           | good `zoute` drop | yumm  |
```


### There's a horizontal rule below this.

* * *

<span style="color:orange; padding-bottom:0;" >Markdown Syntax:</span>
```md
* * *
```

### Here is an unordered list:

*   Item foo
*   Item bar
*   Item baz
*   Item zip

<span style="color:orange; padding-bottom:0;" >Markdown Syntax:</span>
```md
*   Item foo
*   Item bar
*   Item baz
*   Item zip
```

### And an ordered list:

1.  Item one
1.  Item two
1.  Item three
1.  Item four

<span style="color:orange; padding-bottom:0;" >Markdown Syntax:</span>
```md
1.  Item one
1.  Item two
1.  Item three
1.  Item four
```

### And a nested list:

- level 1 item
  - level 2 item
  - level 2 item
    - level 3 item
    - level 3 item
- level 1 item
  - level 2 item
  - level 2 item
  - level 2 item
- level 1 item
  - level 2 item
  - level 2 item
- level 1 item


<span style="color:orange; padding-bottom:0;" >Markdown Syntax:</span>
```md
- level 1 item
  - level 2 item
  - level 2 item
    - level 3 item
    - level 3 item
- level 1 item
  - level 2 item
  - level 2 item
  - level 2 item
- level 1 item
  - level 2 item
  - level 2 item
- level 1 item
```

### Nesting an ol in ul in an ol

- level 1 item (ul)
  1. level 2 item (ol)
  1. level 2 item (ol)
    - level 3 item (ul)
    - level 3 item (ul)
- level 1 item (ul)
  1. level 2 item (ol)
  1. level 2 item (ol)
    - level 3 item (ul)
    - level 3 item (ul)
  1. level 4 item (ol)
  1. level 4 item (ol)
    - level 3 item (ul)
    - level 3 item (ul)
- level 1 item (ul)


<span style="color:orange; padding-bottom:0;" >Markdown Syntax:</span>
```md
- level 1 item (ul)
  1. level 2 item (ol)
  1. level 2 item (ol)
    - level 3 item (ul)
    - level 3 item (ul)
- level 1 item (ul)
  1. level 2 item (ol)
  1. level 2 item (ol)
    - level 3 item (ul)
    - level 3 item (ul)
  1. level 4 item (ol)
  1. level 4 item (ol)
    - level 3 item (ul)
    - level 3 item (ul)
- level 1 item (ul)
```

### And a task list

- [ ] Hello, this is a TODO item
- [ ] Hello, this is another TODO item
- [x] Goodbye, this item is done

<span style="color:orange; padding-bottom:0;" >Markdown Syntax:</span>
```md
- [ ] Hello, this is a TODO item
- [ ] Hello, this is another TODO item
- [x] Goodbye, this item is done
```

### Small image

![](https://assets-cdn.github.com/images/icons/emoji/octocat.png)

<span style="color:orange; padding-bottom:0;" >Markdown Syntax:</span>
```md
![](https://assets-cdn.github.com/images/icons/emoji/octocat.png)
```

### Large image

![](https://guides.github.com/activities/hello-world/branching.png)


<span style="color:orange; padding-bottom:0;" >Markdown Syntax:</span>
```md
![](https://guides.github.com/activities/hello-world/branching.png)
```

### Definition lists can be used with HTML syntax.

<dl>
<dt>Name</dt>
<dd>Godzilla</dd>
<dt>Born</dt>
<dd>1952</dd>
<dt>Birthplace</dt>
<dd>Japan</dd>
<dt>Color</dt>
<dd>Green</dd>
</dl>


<span style="color:orange; padding-bottom:0;" >Markdown Syntax:</span>
```md
<dl>
<dt>Name</dt>
<dd>Godzilla</dd>
<dt>Born</dt>
<dd>1952</dd>
<dt>Birthplace</dt>
<dd>Japan</dd>
<dt>Color</dt>
<dd>Green</dd>
</dl>
```

#### Multiple description terms and values

Term
: Brief description of Term

Longer Term
: Longer description of Term,
  possibly more than one line

Term
: First description of Term,
  possibly more than one line

: Second description of Term,
  possibly more than one line

Term1
Term2
: Single description of Term1 and Term2,
  possibly more than one line

Term1
Term2
: First description of Term1 and Term2,
  possibly more than one line

: Second description of Term1 and Term2,
  possibly more than one line

<span style="color:orange; padding-bottom:0;" >Markdown Syntax:</span>
```md
Term
: Brief description of Term

Longer Term
: Longer description of Term,
  possibly more than one line

```


### More code

```
Long, single-line code blocks should not wrap. They should horizontally scroll if they are too long. This line should be long enough to demonstrate this.
```


<style>
.highlighter-rouge{
    margin-left:20px!important;
    margin-right:20px!important;
}
</style>
