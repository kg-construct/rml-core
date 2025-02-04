## RMLTC0007h-PostgreSQL

**Title**: "Assigning triples to a non-IRI named graph"

**Description**: "Tests the generation of triples to a non-IRI named graph, which is an error"

**Error expected?** Yes

**Input**
```
DROP TABLE IF EXISTS student;

CREATE TABLE student (
  "ID" INTEGER,
  "FirstName" VARCHAR(50),
  "LastName" VARCHAR(50)
);
INSERT INTO student values ('10', 'Venus', 'Williams');

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
      rml:graphMap [
          rml:reference "Name";
          rml:termType rml:Literal
        ];
      rml:template "http://example.com/Student/{ID}/{FirstName}"
    ] .

<http://example.com/base/#DB_source> a d2rq:Database;
  d2rq:jdbcDSN "CONNECTIONDSN";
  d2rq:jdbcDriver "org.postgresql.Driver";
  d2rq:password "";
  d2rq:username "postgres" .

```

