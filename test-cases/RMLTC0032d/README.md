## RMLTC0032d

**Title**: "Blank node subject mapping can omit logical source"

**Description**: "Test a Triples Map with a blank node subject map without expressions can omit logical source"

**Default Base IRI**: http://example.com/

**Error expected?** No

**Mapping**
```
@prefix rml: <http://w3id.org/rml/>.
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:subjectMap [ rml:termType rml:BlankNode ];
  rml:predicateObjectMap [
    rml:predicate rdfs:label;
    rml:objectMap [
      rml:constant "Gaston Lagaffe";
      rml:languageMap [ rml:constant "fr-BE" ];
    ];
  ].


```

**Output**
```
_:bn0 <http://www.w3.org/2000/01/rdf-schema#label> "Gaston Lagaffe"@fr-BE .
```

