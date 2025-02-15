# Assigning Triples to Named Graphs

Each triple generated from an [=RML mapping=] is placed into one or more graphs of the [=output dataset=]. Possible target graphs are the unnamed [=default graph=], the [=IRI=]-named [=named graphs=], and [=blank node=] named [=named graphs=]

Any [=subject map=] or [=predicate-object map=] MUST have zero or more associated <dfn>graph maps</dfn>. They are specified in one of two ways:

1. using the `rml:graphMap` property, whose value MUST be a [=graph map=],
2. using the [=constant shortcut property=] `rml:graph`.

[=Graph maps=] are themselves [=term maps=]. When [=RDF triples are generated=], the set of target graphs is determined by taking into account any [=graph maps=] associated with the [=subject map=] or [=predicate-object map=].

If a [=graph map=] generates the special IRI `rml:defaultGraph`, then the target graph is the [=default graph=] of the [=output dataset=].

<aside class="example"  id="example-graph-map" title="Usage of graph maps">

In the following [=subject map=] example, all generated [=RDF triples=] will be stored in the [=named graph=] `ex:AlbumGraph`.

<aside class="ex-mapping">

```turtle
<#ImageTriplesMap>
  rml:subjectMap [
    rml:template "http://data.example.com/image/{$.ID}" ;
    rml:graphMap [ rml:constant ex:AlbumGraph ] ;
  ] .
```

</aside>

This is equivalent to the following example, which uses a [=constant shortcut property=]:

<aside class="ex-mapping">

```turtle
<#ImageTriplesMap>
  rml:subjectMap [
    rml:template "http://data.example.com/image/{$.ID}" ;
    rml:graph ex:AlbumGraph ;
  ] .
```

</aside>

In the following example, [=RDF triples=] are placed into a [=IRI=]-named [=named graphs=] according to `ID` of the images:

<aside class="ex-mapping">

```turtle
<#ImageTriplesMap>
  rml:subjectMap [
    rml:template "http://data.example.com/image/{$.ID}" ;
    rml:graphMap [
      rml:template "http://data.example.com/graph/{$.ID}" ;
    ] ;
  ] .
```

</aside>

However, in this example, RDF triples of the [=predicate=] `ex:title` are placed into [=blank node=] [=named graphs=] according to `ID` of the images:

<aside class="ex-mapping">

```turtle
<#ImageTriplesMap>
  rml:subjectMap [
    rml:template "http://data.example.com/image/{$.ID}" ;
  ] ;
  rml:predicateObjectMap [
    rml:predicate ex:title ;
    rml:objectMap [
      rml:reference "$.Title.Value" ;
    ] ;
    rml:graphMap [
      rml:reference "$.ID" ;
      rml:termType rml:BlankNode ;
    ] ;
  ] .
```
</aside>

</aside>

