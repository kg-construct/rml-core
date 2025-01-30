## RMLTC0008a-SQLServer

**Title**: "Generation of triples to a target graph by using rr:graphMap and rr:template"

**Description**: "Test that results of the mapping can be directed to a target graph by using rr:graphMap and rr:template"

**Error expected?** No

**Input**
```
USE TestDB;
DROP TABLE IF EXISTS student;
CREATE TABLE student (
  "ID" INTEGER,
  "Name" VARCHAR(50),
  "Sport" VARCHAR(50)
);
INSERT INTO student values ('10', 'Venus Williams', 'Tennis');

```

**Mapping**
```
@prefix d2rq: <http://www.wiwiss.fu-berlin.de/suhl/bizer/D2RQ/0.1#> .
@prefix ex: <http://example.com/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rml: <http://w3id.org/rml/> .

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:logicalSource [
      rml:source <http://example.com/base/#DB_source>;
      rml:referenceFormulation rml:SQL2008Table;
      rml:iterator "student"
    ];
  rml:predicateObjectMap [
      rml:object foaf:Person;
      rml:predicate rdf:type
    ], [
      rml:objectMap [
          rml:reference "ID"
        ];
      rml:predicate ex:id
    ], [
      rml:objectMap [
          rml:reference "Name"
        ];
      rml:predicate foaf:name
    ], [
      rml:objectMap [
          rml:reference "Sport"
        ];
      rml:predicate ex:Sport
    ];
  rml:subjectMap [
      rml:graphMap [
          rml:template "http://example.com/graph/Student/{ID}/{Name}"
        ];
      rml:template "http://example.com/Student/{ID}/{Name}"
    ] .

<http://example.com/base/#DB_source> a d2rq:Database;
  d2rq:jdbcDSN "CONNECTIONDSN";
  d2rq:jdbcDriver "com.microsoft.sqlserver.jdbc.SQLServerDriver";
  d2rq:password "YourSTRONG!Passw0rd;";
  d2rq:username "sa" .

```

**Output**
```
<http://example.com/Student/10/Venus%20Williams> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> <http://example.com/graph/Student/10/Venus%20Williams> .
<http://example.com/Student/10/Venus%20Williams> <http://xmlns.com/foaf/0.1/name> "Venus Williams" <http://example.com/graph/Student/10/Venus%20Williams> .
<http://example.com/Student/10/Venus%20Williams> <http://example.com/id> "10"^^<http://www.w3.org/2001/XMLSchema#integer> <http://example.com/graph/Student/10/Venus%20Williams> . 
<http://example.com/Student/10/Venus%20Williams> <http://example.com/Sport> "Tennis" <http://example.com/graph/Student/10/Venus%20Williams> . 



```

