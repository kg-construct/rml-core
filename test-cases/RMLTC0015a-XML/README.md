## RMLTC0015a-XML

**Title**: "Generation of language tags from a table with language information"

**Description**: "Generation of language tags from a table with language information"

**Error expected?** No

**Input**
```
<?xml version="1.0"?>

<countries>
  <country><Code>BO</Code><Name>Bolivia, Plurinational State of</Name></country>
  <country><Code>IE</Code><Name>Ireland</Name></country>
</countries>

```

**Mapping**
```
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rml: <http://w3id.org/rml/> .

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
      rml:iterator "/countries/country";
      rml:referenceFormulation rml:XPath;
      rml:source [ a rml:RelativePathSource;
          rml:root rml:MappingDirectory;
          rml:path "country_en.xml"
        ]
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:language "en";
          rml:reference "Name"
        ];
      rml:predicate rdfs:label
    ];
  rml:subjectMap [
      rml:template "http://example.com/{Code}"
    ] .

<http://example.com/base/TriplesMap2> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
      rml:iterator "/countries/country";
      rml:referenceFormulation rml:XPath;
      rml:source [ a rml:RelativePathSource;
          rml:root rml:MappingDirectory;
          rml:path "country_es.xml"
        ]
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:language "es";
          rml:reference "Name"
        ];
      rml:predicate rdfs:label
    ];
  rml:subjectMap [
      rml:template "http://example.com/{Code}"
    ] .

```

**Output**
```
<http://example.com/BO> <http://www.w3.org/2000/01/rdf-schema#label> "Bolivia, Plurinational State of"@en .
<http://example.com/BO> <http://www.w3.org/2000/01/rdf-schema#label> "Estado Plurinacional de Bolivia"@es .
<http://example.com/IE> <http://www.w3.org/2000/01/rdf-schema#label> "Ireland"@en .
<http://example.com/IE> <http://www.w3.org/2000/01/rdf-schema#label> "Irlanda"@es .



```

