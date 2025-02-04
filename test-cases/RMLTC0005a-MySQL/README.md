## RMLTC0005a-MySQL

**Title**: "Typing of resources"

**Description**: "Tests the typing of resources"

**Error expected?** No

**Input**
```
USE test;
DROP TABLE IF EXISTS test.IOUs;
CREATE TABLE IOUs (
      fname VARCHAR(20),
      lname  VARCHAR(20),
      amount FLOAT);
INSERT INTO IOUs (fname, lname, amount) VALUES ('Bob', 'Smith', 30);
INSERT INTO IOUs (fname, lname, amount) VALUES ('Sue', 'Jones', 20);
INSERT INTO IOUs (fname, lname, amount) VALUES ('Bob', 'Smith', 30);

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
      rml:iterator "IOUs"
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:reference "amount"
        ];
      rml:predicate ex:owes
    ];
  rml:subjectMap [
      rml:class foaf:Person;
      rml:template "http://example.com/{fname};{lname}"
    ] .

<http://example.com/base/#DB_source> a d2rq:Database;
  d2rq:jdbcDSN "CONNECTIONDSN";
  d2rq:jdbcDriver "com.mysql.cj.jdbc.Driver";
  d2rq:password "";
  d2rq:username "root" .

```

**Output**
```
<http://example.com/Bob;Smith> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/Bob;Smith> <http://example.com/owes> "3.0E1"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.com/Sue;Jones> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/Sue;Jones> <http://example.com/owes> "2.0E1"^^<http://www.w3.org/2001/XMLSchema#double> .


```

