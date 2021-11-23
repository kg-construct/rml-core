# SHACL shapes for RML v1

SHACL shapes for the [original RML specification](https://rml.io/specs/rml) (v1)
These shapes were created manually, based upon the R2RML, RML, CSVW, SD,
D2RQ, and DCAT specifications.

These SHACL shapes validate:
- R2RML Graph Map
- R2RML Logical Table
- R2RML Object Map
- R2RML Predicate Map
- R2RML Predicate Object Map
- R2RML Subject Map
- R2RML Triples Map
- R2RML Reference Object Map
- RML Logical Source
- RML reference
- CSVW for rml:source (CSV files)
- SD for rml:source (SPARQL endpoints)
- D2RQ for rml:source (RDBs)
- DCAT Dataset & Distribution for rml:source (W3C DCAT)

All these shapes can be combined into one giant shape (included as well)
with `./generate_shape.py` to make it easier for for validating mapping
rules with existing SHACL tools.

These shapes are tested with a set of test cases and are executed by
Github Actions. These test cases verify if required properties are
present and verifies the cardinalities of required and optional
properties.
