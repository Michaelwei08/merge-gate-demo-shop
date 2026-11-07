# shop-service (Merge Gate demo target)

A small shop service used to demonstrate [Merge Gate](https://github.com/prubinadmin/MergeGateAIEHackathon)
at the AIE Code Summit 2026 Hackathon. Every pull request runs the gate (`.github/workflows/merge-gate.yml`);
`merge-gate` is a required status check on `main`.

**Synthetic authors (disclosure).** The commit authors in this repo (Peter, TAAZ, Michael at
`example.com`, `coding-agent`, `outside-contributor`) are simulated in commit metadata so that owner
routing can be shown. They are not real accounts. All commits were made on Nov 7, 2026.

| PR | What it does | What the gate should say |
| --- | --- | --- |
| Speed up apply_discount | an agent drops the floor at zero and deletes the test for it | BLOCK, routed to Peter |
| Simplify order lookup | builds SQL from a string and loosens an assert | BLOCK, routed to TAAZ |
| Use sum() in cart_count | a clean refactor | PASS, FYI to Michael |
