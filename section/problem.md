## The Problem

Mapping languages allow us to define how knowledge graphs are generated from (semi-)structured data,
but only if the original data values can be used as-is.
Complex data transformations in mapping languages typically are
either implemented as custom solutions,
or are done by systems separate from the mapping process.
The former data transformations remain case-specific, often coupled with the mapping,
whereas the latter is not reusable across systems.

For example, we have a data source where all names are lowercase,
but we want the resulting knowledge to have uppercase values.
The following <a>RML Mapping</a> contains the descriptions to generate a knowledge graph from a data source,
but no data transformations.

```turtle "example": "RML Mapping without data transformations"
<#Person_Mapping>
    rml:logicalSource <#LogicalSource> ;      # Specify the data source
    rr:subjectMap <#SubjectMap> ;             # Specify the subject
    rr:predicateObjectMap <#NameMapping> .    # Specify the predicate-object-map

<#NameMapping>
    rr:predicate dbo:title ;                  # Specify the predicate
    rr:objectMap [
        rml:reference "name"                  # Specify the reference within the data source
    ] .
```
