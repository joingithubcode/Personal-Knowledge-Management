[0m
> pkm-writer · nemotron-3.5-lightning-free
[0m
## Result
- File: dry run
- Action: dry-run
- Summary: B-tree indexes in PostgreSQL

```markdown
# B-tree Indexes (PostgreSQL)

**Type:** Performance :: Indexing  
**Status:** draft  

## Summary
B‑tree is the default index type in PostgreSQL. It stores key‑value pairs in a balanced tree structure, enabling fast equality and range lookups on indexed columns.

## Key points
- **Structure:** Each internal node holds up to `ceil(page_size / average_key_size)` child pointers; leaf nodes store the actual row IDs (CTIDs).
- **Balanced:** All leaf pages are at the same depth, guaranteeing O(log n) search time.
- **Ordering:** Keys are stored sorted, which makes range queries (`BETWEEN`, `>`, `<`) efficient.
- **Default:** Created automatically with `CREATE INDEX` or via `PRIMARY KEY`/`UNIQUE` constraints.
- **Collation:** Uses the column’s collation; supports partial indexes and expression indexes.
- **Maintenance:** `VACUUM` and `REINDEX` can reclaim space and refresh ordering.

## Examples
```sql
-- Create a standard B‑tree index
CREATE INDEX idx_users_name ON users(name);

-- Expression index (lower‑case search)
CREATE INDEX idx_users_lower_name ON users (lower(name));

-- Partial index (only active rows)
CREATE INDEX idx_orders_active ON orders(status) WHERE status = 'pending';
```

## Related notes
- Hash indexes (when to use `hash` operator class)
- GiST/GIN indexes for full‑text and geometric data
- Covering indexes and index-only scans

## Notes
- B‑tree indexes accelerate `SELECT … WHERE col OP value` and `ORDER BY col`.
- Large numbers of indexes can slow down `INSERT`/`UPDATE`/`DELETE` because each modification must be propagated to all relevant index pages.
- Choose selectivity wisely; highly selective columns benefit most.
- Never invent sources or quotes; all statements are based on PostgreSQL documentation.
```
