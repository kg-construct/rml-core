## RMLTC0007c-PostgreSQL

**Title**: "One row mapping, using rr:class"

**Description**: "Tests subjectmap with more than one class IRIs, rr:class"

**Error expected?** No

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
@prefix ex: <http://example.com/> .
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
          rml:reference "ID"
        ];
      rml:predicate ex:id
    ], [
      rml:objectMap [
          rml:reference "FirstName"
        ];
      rml:predicate foaf:name
    ];
  rml:subjectMap [
      rml:class ex:Student, foaf:Person;
      rml:template "http://example.com/Student/{ID}/{FirstName}"
    ] .

<http://example.com/base/#DB_source> a d2rq:Database;
  d2rq:jdbcDSN "CONNECTIONDSN";
  d2rq:jdbcDriver "org.postgresql.Driver";
  d2rq:password "";
  d2rq:username "postgres" .

```

**Output**
```
<http://example.com/Student/10/Venus> <http://xmlns.com/foaf/0.1/name> "Venus" .
<http://example.com/Student/10/Venus> <http://example.com/id> "10"^^<http://www.w3.org/2001/XMLSchema#integer> . 
<http://example.com/Student/10/Venus> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/Student/10/Venus> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/Student> .


```

