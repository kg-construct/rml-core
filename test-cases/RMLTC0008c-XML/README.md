## RMLTC0008c-XML

**Title**: "Generation of triples by using multiple predicateMaps within a rr:predicateObjectMap"

**Description**: "Tests the generation of triples by using multiple predicateMaps within a rr:predicateObjectMap"

**Error expected?** No

**Input**
```
<?xml version="1.0"?>

<students>
  <student>
    <ID>10</ID>
    <Name>Venus Williams</Name>
    <Sport>Tennis</Sport>
  </student>
</students>

```

**Mapping**
```
@prefix ex: <http://example.com/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix rml: <http://w3id.org/rml/> .

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
      rml:iterator "/students/student";
      rml:referenceFormulation rml:XPath;
      rml:source [ a rml:RelativePathSource;
          rml:root rml:MappingDirectory;
          rml:path "student.xml"
        ]
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:reference "Name"
        ];
      rml:predicate ex:name, foaf:name
    ];
  rml:subjectMap [
      rml:template "http://example.com/Student/{ID}/{Name}"
    ] .

```

**Output**
```
<http://example.com/Student/10/Venus%20Williams> <http://xmlns.com/foaf/0.1/name> "Venus Williams"  .
<http://example.com/Student/10/Venus%20Williams> <http://example.com/name> "Venus Williams"  .


```

