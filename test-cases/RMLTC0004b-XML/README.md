## RMLTC0004b-XML

**Title**: "One column mapping, presence of rr:termType rr:Literal on rr:subjectMap"

**Description**: "Tests: (1) one column mapping (2) the presence of rr:termType rr:Literal on rr:subjectMap, which is invalid"

**Error expected?** Yes

**Input**
```
<?xml version="1.0"?>

<students>
  <student>
    <Name>Venus</Name>
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
          rml:reference "Name"
        ];
      rml:predicate foaf:name
    ];
  rml:subjectMap [
      rml:template "http://example.com/{Name}";
      rml:termType rml:Literal
    ] .

```

