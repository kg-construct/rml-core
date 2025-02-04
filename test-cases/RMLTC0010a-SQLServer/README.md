## RMLTC0010a-SQLServer

**Title**: "Template with table column with special chars"

**Description**: "Tests a template with blank space in column value"

**Error expected?** No

**Input**
```
USE TestDB;
DROP TABLE IF EXISTS country_info;

CREATE TABLE country_info (
  "Country Code" INTEGER,
  "Name" VARCHAR(100),
  "ISO 3166" VARCHAR(10)
);
INSERT INTO country_info values ('1', 'Bolivia, Plurinational State of', 'BO');
INSERT INTO country_info values ('2', 'Ireland', 'IE');
INSERT INTO country_info values ('3', 'Saint Martin (French part)', 'MF');

```

**Mapping**
```
@prefix d2rq: <http://www.wiwiss.fu-berlin.de/suhl/bizer/D2RQ/0.1#> .
@prefix ex: <http://example.com/> .
@prefix rml: <http://w3id.org/rml/> .

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:logicalSource [
      rml:source <http://example.com/base/#DB_source>;
      rml:referenceFormulation rml:SQL2008Table;
      rml:iterator "country_info"
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:reference "Name"
        ];
      rml:predicate ex:name
    ];
  rml:subjectMap [
      rml:template "http://example.com/{Country Code}"
    ] .

<http://example.com/base/#DB_source> a d2rq:Database;
  d2rq:jdbcDSN "CONNECTIONDSN";
  d2rq:jdbcDriver "com.microsoft.sqlserver.jdbc.SQLServerDriver";
  d2rq:password "YourSTRONG!Passw0rd;";
  d2rq:username "sa" .

```

**Output**
```
<http://example.com/1> <http://example.com/name> "Bolivia, Plurinational State of" .
<http://example.com/2> <http://example.com/name> "Ireland" .
<http://example.com/3> <http://example.com/name> "Saint Martin (French part)" .


```

