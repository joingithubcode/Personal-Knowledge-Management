---
title: "javascript-event-loop"
status: draft
created: 2026-08-08
tags:
  - javascript
  - concurrency
  - web-development
related:
  - frontend-vs-backend
---

# javascript-event-loop

## Purpose

Explain the JavaScript event loop and how a single thread handles async work
without blocking.

## Context

JavaScript in the browser runs on one thread, yet it manages animations,
clicks, network calls, and timers at the same time. It does this with an
event loop that queues work and runs it one piece at a time. Understanding
the loop explains why some code orderings behave unexpectedly.

## Main Notes

- JavaScript runs tasks one at a time on the call stack; the event loop
  pulls the next task when the stack is empty.
- Asynchronous operations (timers, fetch, events) do not block the thread;
  they schedule callbacks for later.
- Two queues matter: the macrotask queue (setTimeout, events) and the
  microtask queue (promises), and microtasks run before the next macrotask.
- A long-running synchronous function stalls the loop, freezing the page.
- Promise callbacks (microtasks) run right after the current script finishes,
  before rendering or the next timer.
- The loop is also the model for server-side JavaScript, which stays single
  threaded and shares the same ordering rules.
- Writing non-blocking code means avoiding heavy synchronous work and
  splitting it with awaits or web workers.

## References

- Foundational concept; no single source.
- Described in the HTML standard and JavaScript runtime documentation.

## Related Notes

- [[frontend-vs-backend]]

## Tags

This note is tagged in the front matter as javascript, concurrency,
web-development.

## Review History

- 2026-08-08: Created as a draft.
