## RMLTC0007g-XML

**Title**: "Assigning triples to the default graph"

**Description**: "Tests the generation of triples to the default graph"

**Error expected?** No

**Input**
```
<?xml version="1.0"?>

<students>
  <student>
    <ID>10</ID>
    <FirstName>Venus</FirstName>
    <LastName>Williams</LastName>
  </student>
</students>

```

**Mapping**
```
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
          rml:reference "FirstName"
        ];
      rml:predicate foaf:name
    ];
  rml:subjectMap [
      rml:graph rml:defaultGraph;
      rml:template "http://example.com/Student/{ID}/{FirstName}"
    ] .

```

**Output**
```
<http://example.com/Student/10/Venus> <http://xmlns.com/foaf/0.1/name> "Venus" .


```

