---
id: xua-conf-defaults-guarded
scope:
  - "lib_xua/api/xua_conf_default.h"
severity: error          # error | warn
---
**Claim:** Every configuration define in xua_conf_default.h is wrapped in
`#ifndef NAME` / `#endif` so applications can override it in xua_conf.h,
and has a comment describing what it controls and its default.

**Pass if:** all defines are guarded and commented.
**Fail if:** any define is unguarded, or a newly added one has no comment.
**Evidence:** quote the offending line(s).
