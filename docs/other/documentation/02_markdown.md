---
title: "Markdown Formats"
nav_order: 2
---

## Markdown Formats

### Typography

Text can be **bold**, _italic_, or ~~strikethrough~~.

```md
Text can be **bold**, _italic_, or ~~strikethrough~~.
```

[Link to another page](another-page)

[Link to page with new tab](https://www.google.com/)

```md
[Link to another page](another-page)
[Link to page with new tab](https://www.google.com/)
```

There should be whitespace between paragraphs.

There should be whitespace between paragraphs. We recommend including a README, or a file with information about your project.

```md
# Header 1

## Header 2

## Header 3

### Header 4

#### Header 5

##### Header 6

###### Header 7
```

# Header 1

This is a normal paragraph following a header. GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.

## Header 2

> This is a blockquote following a header.
>
> When something is important enough, you do it even if the odds are not in your favor.

### Header 3

```js
// Javascript code with syntax highlighting.
var fun = function lang(l) {
  dateformat.i18n = require("./lang/" + l);
  return true;
};
```

```ruby
# Ruby code with syntax highlighting
GitHubPages::Dependencies.gems.each do |gem, version|
  s.add_dependency(gem, "= #{version}")
end
```

#### Header 4

- This is an unordered list following a header.
- This is an unordered list following a header.
- This is an unordered list following a header.

##### Header 5

1. This is an ordered list following a header.
2. This is an ordered list following a header.
3. This is an ordered list following a header.

###### Header 6

| head1        | head two          | three |
| :----------- | :---------------- | :---- |
| ok           | good swedish fish | nice  |
| out of stock | good and plenty   | nice  |
| ok           | good 'oreos'      | hmm   |
| ok           | good 'zoute' drop | yumm  |

```md
| head1        | head two          | three |
| :----------- | :---------------- | :---- |
| ok           | good swedish fish | nice  |
| out of stock | good and plenty   | nice  |
| ok           | good `oreos`      | hmm   |
| ok           | good `zoute` drop | yumm  |
```

### Horizontal rule example

```md
---
```

### Here is an unordered list:

- Item foo
- Item bar
- Item baz
- Item zip

```md
- Item foo
- Item bar
- Item baz
- Item zip
```

### And an ordered list:

1.  Item one
1.  Item two
1.  Item three
1.  Item four

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

```md
- [ ] Hello, this is a TODO item
- [ ] Hello, this is another TODO item
- [x] Goodbye, this item is done
```

### Small image

![](https://assets-cdn.github.com/images/icons/emoji/octocat.png)

```md
![](https://assets-cdn.github.com/images/icons/emoji/octocat.png)
```

### Large image

![](https://guides.github.com/activities/hello-world/branching.png)

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
