---
layout: default
title: Home
description: "A blog about random things that I find interesting: technology, software design, decision-making and culture."
---

## Latest posts

{% if site.posts.size > 0 %}
{% for post in site.posts %}
- [{{ post.title }}]({{ post.url | relative_url }}) — {{ post.date | date: "%b %-d, %Y" }}
{% endfor %}
{% else %}
No posts yet. New writing will show up here once posts are added.
{% endif %}
