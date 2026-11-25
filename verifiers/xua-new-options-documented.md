---
id: xua-new-options-documented
scope: ["lib_xua/api/xua_conf_default.h"]
severity: warn
---
**Claim:** Every configuration option added to xua_conf_default.h by this
change is documented in one of doc/rst/opt_*.rst, with its default.

**Pass if:** each new option name appears in an opt_*.rst file with its default.
**Fail if:** any new option is missing from doc/rst/opt_*.rst.
**Evidence:** quote the new #define and name the doc file searched.

