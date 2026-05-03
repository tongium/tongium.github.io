# tongium.github.io

Personal blog source for [tongium.github.io](https://tongium.github.io/).

This repository is a GitHub Pages site built with Jekyll and `jekyll-theme-minimal`. It currently includes a homepage, an about page, and blog posts stored in the standard Jekyll `_posts` directory.

## Structure

- `_config.yml` - site title, description, theme, and timezone
- `index.md` - homepage with the latest posts
- `about.md` - about page
- `_posts/` - dated blog posts
- `_layouts/` - layout overrides
- `assets/` - site assets such as CSS

## Adding content

### New post

Add a Markdown file to `_posts/` using the Jekyll naming format:

`YYYY-MM-DD-title.md`

Example front matter:

```md
---
layout: default
title: "Post title"
date: 2026-05-03 00:00:00 +0700
---
```

### New page

Add a Markdown file at the repository root with Jekyll front matter, for example:

```md
---
layout: default
title: About
permalink: /about/
---
```

## Deployment

This repository is intended to be published through GitHub Pages. Pushing changes to the publishing branch updates the live site after GitHub Pages rebuilds it.
