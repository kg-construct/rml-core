## RMLTC0015b-PostgreSQL

**Title**: "Generation of language tags from a table with language information, and a term map with invalid rr:language value"

**Description**: "Tests a term map with an invalid rr:language value, which is an error"

**Error expected?** Yes

**Input**
```
DROP TABLE IF EXISTS Country;

CREATE TABLE Country (
  Code VARCHAR(2),
  Name VARCHAR(100),
  Lan VARCHAR(10),
  PRIMARY KEY (Code,Lan)
);
INSERT INTO Country (Code, Name, Lan) VALUES ('BO', 'Bolivia, Plurinational State of', 'EN');
INSERT INTO Country (Code, Name, Lan) VALUES ('BO', 'Estado Plurinacional de Bolivia', 'ES');
INSERT INTO Country (Code, Name, Lan) VALUES ('IE', 'Ireland', 'EN');
INSERT INTO Country (Code, Name, Lan) VALUES ('IE', 'Irlanda', 'ES');

```

**Mapping**
```
@prefix d2rq: <http://www.wiwiss.fu-berlin.de/suhl/bizer/D2RQ/0.1#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rml: <http://w3id.org/rml/> .

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:logicalSource [
      rml:iterator """
        SELECT Code, Name, Lan
        FROM Country
        WHERE Lan = 'EN';
       """;
      rml:source <http://example.com/base/#DB_source>;
      rml:referenceFormulation rml:SQL2008Query
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:language "a-english";
          rml:reference "Name"
        ];
      rml:predicate rdfs:label
    ];
  rml:subjectMap [
      rml:template "http://example.com/{Code}"
    ] .

<http://example.com/base/TriplesMap2> a rml:TriplesMap;
  rml:logicalSource [
      rml:iterator """
        SELECT Code, Name, Lan
        FROM Country
        WHERE Lan = 'EN';
       """;
      rml:source <http://example.com/base/#DB_source>;
      rml:referenceFormulation rml:SQL2008Query
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:language "a-spanish";
          rml:reference "Name"
        ];
      rml:predicate rdfs:label
    ];
  rml:subjectMap [
      rml:template "http://example.com/{Code}"
    ] .

<http://example.com/base/#DB_source> a d2rq:Database;
  d2rq:jdbcDSN "CONNECTIONDSN";
  d2rq:jdbcDriver "org.postgresql.Driver";
  d2rq:password "";
  d2rq:username "postgres" .

```

