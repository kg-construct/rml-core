## RMLTC0032c

**Title**: "Non constant mapping, while omitting logical source"

**Description**: "Test a Triples Map with reference expressions cannot omit logical source"

**Default Base IRI**: http://example.com/

**Error expected?** Yes

**Mapping**
```
@prefix rml: <http://w3id.org/rml/>.
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:subjectMap [ rml:template "http://example.com/{name}" ];
  rml:predicateObjectMap [
    rml:predicate rdfs:label;
    rml:objectMap [
      rml:reference "name";
      rml:languageMap [ rml:constant "fr-BE" ];
    ];
  ].


```

