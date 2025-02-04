## RMLTC0024a-CSV

**Title**: "Invalid IRI template 1"

**Description**: "Test handling of invalid IRI template"

**Error expected?** Yes

**Input**
```
Name
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
      rml:template "http://example.com/{NON_EXISTING_COLUMN}"
      rml:class foaf:Person;
    ] .

```

