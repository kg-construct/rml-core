## RMLTC0001a-SQLServer

**Title**: "One column mapping, subject URI generation by using rr:template"

**Description**: "Tests: (1) one column mapping; (2) subject URI generation by using rr:tmplate; (3) one column to one property"

**Error expected?** No

**Input**
```
USE TestDB;
EXEC sp_msforeachtable 'ALTER TABLE ? NOCHECK CONSTRAINT all'
EXEC sp_msforeachtable 'DROP TABLE ?'

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
      rml:template "http://example.com/{Name}"
    ] .

<http://example.com/base/#DB_source> a d2rq:Database;
  d2rq:jdbcDSN "CONNECTIONDSN";
  d2rq:jdbcDriver "com.microsoft.sqlserver.jdbc.SQLServerDriver";
  d2rq:password "YourSTRONG!Passw0rd;";
  d2rq:username "sa" .

```

**Output**
```
<http://example.com/Venus> <http://xmlns.com/foaf/0.1/name> "Venus" .

```

