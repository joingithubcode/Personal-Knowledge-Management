---
name: pkm-cross-link-check
description: Verify that every link in a note points to an existing file
---
1. grep the note for [[...]] and ](...) links.
2. For each local link, glob to confirm the target exists.
3. Report broken links as a list: note, link, reason. Fix them only if you are the writer; the reviewer only reports.
