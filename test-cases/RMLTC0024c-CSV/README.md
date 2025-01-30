## RMLTC0024c-CSV

**Title**: "Invalid IRI template 3"

**Description**: "Test handling of invalid IRI template"

**Error expected?** Yes

**Input**
```
N\ame
Venus

```

**Mapping**
```
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix rml: <http://w3id.org/rml/> .

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
      rml:referenceFormulation rml:CSV;
      rml:source [ a rml:RelativePathSource;
          rml:root rml:MappingDirectory;
          rml:path "student.csv"
        ]
    ];
  rml:subjectMap [
      rml:template "http://example.com/{N\ame}"
      rml:class foaf:Person;
    ] .

```

