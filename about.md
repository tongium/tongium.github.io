---
layout: default
title: About
permalink: /about/
description: "About Tongium's Blog, a personal blog on technology, software design, decision-making and culture."
---

**{{ site.title }}** is a personal blog by {{ site.author.name }}. {{ site.description }}

Topics include software architecture and security, AI, decision-making, and everyday observations.

Browse the [latest posts]({{ "/" | relative_url }}) or subscribe via [RSS]({{ "/feed.xml" | relative_url }}).

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": {{ site.author.name | jsonify }},
  "url": {{ "/about/" | absolute_url | jsonify }},
  "mainEntityOfPage": {{ "/about/" | absolute_url | jsonify }},
  "owns": {"@type": "Blog", "name": {{ site.title | jsonify }}, "url": {{ "/" | absolute_url | jsonify }}}
}
</script>
