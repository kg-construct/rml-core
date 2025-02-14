# Assigning Triples to Named Graphs

Each triple generated from an [=RML mapping=] is placed into one or more graphs of the [=output dataset=]. Possible target graphs are the unnamed [=default graph=], the [=IRI=]-named [=named graphs=], and [=blank node=] named [=named graphs=]

Any [=subject map=] or [=predicate-object=] map MUST have zero or more associated <dfn>graph maps</dfn>. They are specified in one of two ways:

1. using the rml:graphMap property, whose value MUST be a [=graph map=](),
2. using the [=constant shortcut property=]() rml:graph.

[=Graph maps=] are themselves [=term maps=]. When [=RDF triples are generated=], the set of target graphs is determined by taking into account any [=graph maps=] associated with the [=subject map=] or [=predicate-object map=].

If a [=graph map=]() generates the special IRI rml:defaultGraph, then the target graph is the [=default graph=]() of the [=output dataset=]().

<aside class="example"  id="example-graph-map" title="Usage of graph map">

In the following [=subject map=] example, all generated [=RDF triples=] will be stored in the [=named graph=] `ex:DepartmentGraph`.
<aside class="ex-mapping">
```turtle
[]  rml:subjectMap [
      rml:template "http://data.example.com/department/{DEPTNO}";
      rml:graphMap [ rml:constant ex:DepartmentGraph ];
].
```
</aside>
This is equivalent to the following example, which uses a [=constant shortcut property=]:
<aside class="ex-mapping">
```turtle
[]  rml:subjectMap [
      rml:template "http://data.example.com/department/{DEPTNO}";
      rml:graph ex:DepartmentGraph;
].
```
</aside>
In the following example, [=RDF triples=] are placed into [=IRI=]-named [=named graphs=] according to the job title of employees:
<aside class="ex-mapping">
```turtle
[]  rml:subjectMap [
      rml:template "http://data.example.com/employee/{EMPNO}";
      rml:graphMap [ rml:template "http://data.example.com/jobgraph/{JOB}" ];
].
```
</aside>
However, in this example, RDF triples of the [=predicate-object=] `ex:name` are placed into a [=blank node=] named [=named graphs=] according to the job title of employees:
<aside class="ex-mapping">
```turtle
[]  rml:subjectMap [
      rml:template "http://data.example.com/employee/{EMPNO}";
    ];
    rml:predicateObjectMap [
      rml:predicate ex:name;
      rml:objectMap [ rml:reference "name"; ];
      rml:graphMap [
        rml:reference "JOB"
        rml:termType rr:IRI
      ];
    ].
```
</aside>

</aside>

