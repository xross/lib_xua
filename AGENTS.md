# XMOS Library Agent Guidance

Before making changes, read the repository-specific guidance below and the
[XMOS agent instructions](https://github.com/xross/xskills/blob/develop/AGENTS.md).
Read the central AGENTS.md in full and consult everything it directs you to.

If central guidance is inaccessible, use this repository's README and relevant
documentation, preserve existing APIs and compatibility requirements, and report
the access limitation and any material verification gaps.

## Verifiers

Before finishing a change you made, or when reviewing a change someone else
made, run every verifier whose `scope` matches the changed files, from both:

- the generic verifiers in https://github.com/xross/xskills/tree/develop/verifiers
- this repository's `verifiers/` directory (a local verifier with the same
  `id` replaces the generic one)

Follow the procedure in
[Running verifiers](https://github.com/xross/xskills/blob/develop/AGENTS.md#running-verifiers).
If the change is yours, fix `error` failures and report PASS, FIXED or FAIL per
`id`. If you are reviewing, change nothing and report PASS or FAIL per `id`.

If central guidance is inaccessible, still check each verifier in `verifiers/`
whose `scope` matches the changed files, report per `id` as above, and report
that the generic verifiers were not run.

## Repository-Specific Guidance

<!--
Add only information specific to this repository, such as supported targets,
required toolchain versions, hardware constraints, build and test commands,
and compatibility or legacy requirements. Link to existing repository
documentation where appropriate; do not duplicate shared xskills instructions.
-->

