## RMLTC0019a-XML

**Title**: "Generation of triples by using IRI value in columns"

**Description**: "Test the generation of triples by using IRI value in elements"

**Error expected?** No

**Input**
```
<?xml version="1.0"?>

<persons>
    <person>
        <ID>10</ID>
        <FirstName>http://example.com/ns#Jhon</FirstName>
        <LastName>Smith</LastName>
    </person>
    <person>
        <ID>20</ID>
        <FirstName>Carlos</FirstName>
        <LastName>Mendoza</LastName>
    </person>
</persons>

```

**Mapping**
```
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix rml: <http://w3id.org/rml/> .

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
      rml:iterator "/persons/person";
      rml:referenceFormulation rml:XPath;
      rml:source [ a rml:RelativePathSource;
          rml:root rml:MappingDirectory;
          rml:path "persons.xml"
        ]
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:reference "FirstName"
        ];
      rml:predicate foaf:name
    ];
  rml:subjectMap [
      rml:reference "FirstName"
    ] .

```

**Output**
```
<http://example.com/ns#Jhon> <http://xmlns.com/foaf/0.1/name> "http://example.com/ns#Jhon" .
<http://example.com/base/Carlos> <http://xmlns.com/foaf/0.1/name> "Carlos" .

```

