---
title: "php-basics"
status: draft
created: 2026-08-08
tags:
  - programming
  - web-development
  - server-side
related:
  - frontend-vs-backend
---

# php-basics

## Purpose

Explain the core of PHP as a server-side language for building web
applications.

## Context

PHP is a scripting language designed for the web. Code runs on the server,
producing HTML that is sent to the browser. It powers a large share of the
web, often behind frameworks such as Laravel and WordPress.

## Main Notes

- PHP runs server-side: the server executes the script and returns the
  output, usually HTML, to the client.
- PHP code is written inside <?php ... ?> tags mixed with template markup.
- Variables start with $ and are loosely typed; arrays are the main
  data structure.
- Common built-in features handle form input, cookies, sessions, and
  database access.
- A request maps to a PHP file or route; each request starts a fresh script
  execution.
- Functions, classes, and namespaces organize code; modern PHP supports
  object-oriented style and strong typing.
- PHP is typically run by a web server such as Apache or Nginx via an
  interface like PHP-FPM.
- Security basics still apply: validate input, escape output, and never trust
  client-supplied data.

## References

- Foundational concept; no single source.
- Official documentation at php.net; PHP language reference.

## Related Notes

- [[frontend-vs-backend]]

## Tags

This note is tagged in the front matter as programming, web-development,
server-side.

## Review History

- 2026-08-08: Created as a draft.
