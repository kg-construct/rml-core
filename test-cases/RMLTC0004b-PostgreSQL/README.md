## RMLTC0004b-PostgreSQL

**Title**: "One column mapping, presence of rr:termType rr:Literal on rr:subjectMap"

**Description**: "Tests: (1) one column mapping (2) the presence of rr:termType rr:Literal on rr:subjectMap, which is invalid"

**Error expected?** Yes

**Input**
```
DROP TABLE IF EXISTS student;
CREATE TABLE student (
  "Name" VARCHAR(50)
);
INSERT INTO student values ('Venus');

```

**Mapping**
```
@prefix d2rq: <http://www.wiwiss.fu-berlin.de/suhl/bizer/D2RQ/0.1#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix rml: <http://w3id.org/rml/> .

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:logicalSource [
      rml:source <http://example.com/base/#DB_source>;
      rml:referenceFormulation rml:SQL2008Table;
      rml:iterator "student"
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:reference "Name"
        ];
      rml:predicate foaf:name
    ];
  rml:subjectMap [
      rml:template "http://example.com/{Name}";
      rml:termType rml:Literal
    ] .

<http://example.com/base/#DB_source> a d2rq:Database;
  d2rq:jdbcDSN "CONNECTIONDSN";
  d2rq:jdbcDriver "org.postgresql.Driver";
  d2rq:password "";
  d2rq:username "postgres" .

```

