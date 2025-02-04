## RMLTC0001b-XML

**Title**: "One column mapping, generation of a BlankNode subject by using rr:termType"

**Description**: "Tests: (1) one column mapping; (2) generation of a BlankNode subject by using rr:termType; (3) one column to one property"

**Error expected?** No

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
      rml:template "{Name}";
      rml:termType rml:BlankNode
    ] .

```

**Output**
```
_:Venus <http://xmlns.com/foaf/0.1/name> "Venus" .


```

