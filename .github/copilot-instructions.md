# Copilot instructions for `tongium.github.io`

## Build, test, and lint commands

This repository does not define project-specific build, test, or lint commands. There is no `Gemfile`, package manifest, Makefile, or GitHub Actions workflow in the repo. The site is intended to be rendered by GitHub Pages from committed Jekyll content.

## High-level architecture

This is a content-first GitHub Pages site backed by Jekyll with `jekyll-theme-minimal` configured in `_config.yml`. The theme provides the layout implementation; the repository currently supplies Markdown content rather than local HTML templates or Ruby code.

Site-wide metadata lives in `_config.yml` and is consumed directly by pages through Liquid variables such as `site.title` and `site.description`.

The homepage (`index.md`) is the main aggregation point. It renders the site description from config, then loops over `site.posts` to show the latest posts and links to standalone pages.

Posts live in `_posts/` and are discovered by filename/date convention. Standalone pages such as `about.md` and `404.md` live at the repository root and use explicit front matter to control title and permalink.

## Key conventions

- Use Jekyll front matter on every page and post. Existing content uses `layout: default` everywhere, which means rendering depends on the theme's default layout unless local overrides are later added.
- Keep posts in `_posts/` with `YYYY-MM-DD-title.md` filenames and include an explicit `date` with timezone offset. The site timezone is `Asia/Bangkok`, and the existing post uses `+0700`.
- Use `permalink` for standalone pages that need stable paths, especially `/about/` and `/404.html`.
- Use Liquid variables instead of hardcoded site metadata. Existing pages pull shared text from `_config.yml` via `site.title` and `site.description`.
- Use `relative_url` for internal links and post URLs so links stay correct if the site base URL changes.
- For home page changes, preserve the `site.posts` loop unless intentionally changing how posts are listed; that file is the only place that currently assembles site navigation and post discovery.
