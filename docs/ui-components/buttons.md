---
title: Buttons
parent: UI Components
nav_order: 2
---

# Buttons
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Basic button styles

### Links that look like buttons

<div class="code-example" markdown="1">
[Link button](https://www.junian.dev/jekyll-jtdocs/){: .btn }

[Link button](https://www.junian.dev/jekyll-jtdocs/){: .btn .btn-purple }
[Link button](https://www.junian.dev/jekyll-jtdocs/){: .btn .btn-blue }
[Link button](https://www.junian.dev/jekyll-jtdocs/){: .btn .btn-green }

[Link button](https://www.junian.dev/jekyll-jtdocs/){: .btn .btn-outline }
</div>
```markdown
[Link button](https://www.junian.dev/jekyll-jtdocs/){: .btn }

[Link button](https://www.junian.dev/jekyll-jtdocs/){: .btn .btn-purple }
[Link button](https://www.junian.dev/jekyll-jtdocs/){: .btn .btn-blue }
[Link button](https://www.junian.dev/jekyll-jtdocs/){: .btn .btn-green }

[Link button](https://www.junian.dev/jekyll-jtdocs/){: .btn .btn-outline }
```

### Button element

GitHub Flavored Markdown does not support the `button` element, so you'll have to use inline HTML for this:

<div class="code-example">
<button type="button" name="button" class="btn">Button element</button>
</div>
```html
<button type="button" name="button" class="btn">Button element</button>
```

---

## Using utilities with buttons

### Button size

Wrap the button in a container that uses the [font-size utility classes]({% link docs/utilities/typography.md %}) to scale buttons:

<div class="code-example" markdown="1">
<span class="fs-6">
[Big ass button](https://www.junian.dev/jekyll-jtdocs/){: .btn }
</span>

<span class="fs-3">
[Tiny ass button](https://www.junian.dev/jekyll-jtdocs/){: .btn }
</span>
</div>
```markdown
<span class="fs-8">
[Link button](https://www.junian.dev/jekyll-jtdocs/){: .btn }
</span>

<span class="fs-3">
[Tiny ass button](https://www.junian.dev/jekyll-jtdocs/){: .btn }
</span>
```

### Spacing between buttons

Use the [margin utility classes]({% link docs/utilities/layout.md %}#spacing) to add spacing between two buttons in the same block.

<div class="code-example" markdown="1">
[Button with space](https://www.junian.dev/jekyll-jtdocs/){: .btn .btn-purple .mr-2 }
[Button](https://www.junian.dev/jekyll-jtdocs/){: .btn .btn-blue }

[Button with more space](https://www.junian.dev/jekyll-jtdocs/){: .btn .btn-green .mr-4 }
[Button](https://www.junian.dev/jekyll-jtdocs/){: .btn .btn-blue }
</div>
```markdown
[Button with space](https://www.junian.dev/jekyll-jtdocs/){: .btn .btn-purple .mr-2 }
[Button](https://www.junian.dev/jekyll-jtdocs/){: .btn .btn-blue }

[Button with more space](https://www.junian.dev/jekyll-jtdocs/){: .btn .btn-green .mr-4 }
[Button](https://www.junian.dev/jekyll-jtdocs/){: .btn .btn-blue }
```
