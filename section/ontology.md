## FNML

<div class="advisement">
This description is a proposal
</div>

We use terms defined in the <a>FNML</a> ontology to link <a>RML</a> with <a>FnO</a>.

The ontology namespace is [http://semweb.mmlab.be/ns/fnml#](http://semweb.mmlab.be/ns/fnml#),
the preferred prefix is `fnml:`.

<div class="mermaid remove">
graph LR
    A([term map]) -->|rr:constant| B[constant value]
    A -->|rml:reference| C[reference formulation]
    A -->|rr:template| D[string template]
    A -->|rr:termType| E([rr:IRI / rr:BlankNode / rr:Literal])
    A -->|rr:language| F[language tag]
    A -->|rr:datatype| G([rdfs:Datatype])
    H([rr:SubjectMap]):::note
    J([rr:PredicateMap]):::note
    K([rr:ObjectMap]):::note
    L([rr:GraphMap]):::note
    M([fnml:FunctionMap]):::new
    M -->|fnml:functionValue| I([rr:TriplesMap])
    classDef note fill:#eee,stroke-width:0px,color:#666
    classDef new fill:#8F9
    linkStyle 6 stroke:#8F9
</div>

<figure data-format="markdown">
[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggTFJcbiAgICBBKFt0ZXJtIG1hcF0pIC0tPnxycjpjb25zdGFudHwgQltjb25zdGFudCB2YWx1ZV1cbiAgICBBIC0tPnxybWw6cmVmZXJlbmNlfCBDW3JlZmVyZW5jZSBmb3JtdWxhdGlvbl1cbiAgICBBIC0tPnxycjp0ZW1wbGF0ZXwgRFtzdHJpbmcgdGVtcGxhdGVdXG4gICAgQSAtLT58cnI6dGVybVR5cGV8IEUoW3JyOklSSSAvIHJyOkJsYW5rTm9kZSAvIHJyOkxpdGVyYWxdKVxuICAgIEEgLS0-fHJyOmxhbmd1YWdlfCBGW2xhbmd1YWdlIHRhZ11cbiAgICBBIC0tPnxycjpkYXRhdHlwZXwgRyhbcmRmczpEYXRhdHlwZV0pXG4gICAgXG4gICAgSChbcnI6U3ViamVjdE1hcF0pOjo6bm90ZVxuICAgIEooW3JyOlByZWRpY2F0ZU1hcF0pOjo6bm90ZVxuICAgIEsoW3JyOk9iamVjdE1hcF0pOjo6bm90ZVxuICAgIEwoW3JyOkdyYXBoTWFwXSk6Ojpub3RlXG4gICAgTShbZm5tbDpGdW5jdGlvbk1hcF0pOjo6bmV3XG4gICAgTSAtLT58Zm5tbDpmdW5jdGlvblZhbHVlfCBJKFtycjpUcmlwbGVzTWFwXSlcbiAgICBjbGFzc0RlZiBub3RlIGZpbGw6I2VlZSxzdHJva2Utd2lkdGg6MHB4LGNvbG9yOiM2NjZcbiAgICBjbGFzc0RlZiBuZXcgZmlsbDojOEY5XG4gICAgbGlua1N0eWxlIDYgc3Ryb2tlOiM4RjkiLCJtZXJtYWlkIjp7fSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggTFJcbiAgICBBKFt0ZXJtIG1hcF0pIC0tPnxycjpjb25zdGFudHwgQltjb25zdGFudCB2YWx1ZV1cbiAgICBBIC0tPnxybWw6cmVmZXJlbmNlfCBDW3JlZmVyZW5jZSBmb3JtdWxhdGlvbl1cbiAgICBBIC0tPnxycjp0ZW1wbGF0ZXwgRFtzdHJpbmcgdGVtcGxhdGVdXG4gICAgQSAtLT58cnI6dGVybVR5cGV8IEUoW3JyOklSSSAvIHJyOkJsYW5rTm9kZSAvIHJyOkxpdGVyYWxdKVxuICAgIEEgLS0-fHJyOmxhbmd1YWdlfCBGW2xhbmd1YWdlIHRhZ11cbiAgICBBIC0tPnxycjpkYXRhdHlwZXwgRyhbcmRmczpEYXRhdHlwZV0pXG4gICAgXG4gICAgSChbcnI6U3ViamVjdE1hcF0pOjo6bm90ZVxuICAgIEooW3JyOlByZWRpY2F0ZU1hcF0pOjo6bm90ZVxuICAgIEsoW3JyOk9iamVjdE1hcF0pOjo6bm90ZVxuICAgIEwoW3JyOkdyYXBoTWFwXSk6Ojpub3RlXG4gICAgTShbZm5tbDpGdW5jdGlvbk1hcF0pOjo6bmV3XG4gICAgTSAtLT58Zm5tbDpmdW5jdGlvblZhbHVlfCBJKFtycjpUcmlwbGVzTWFwXSlcbiAgICBjbGFzc0RlZiBub3RlIGZpbGw6I2VlZSxzdHJva2Utd2lkdGg6MHB4LGNvbG9yOiM2NjZcbiAgICBjbGFzc0RlZiBuZXcgZmlsbDojOEY5XG4gICAgbGlua1N0eWxlIDYgc3Ryb2tlOiM4RjkiLCJtZXJtYWlkIjp7fSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)
<figcaption>FNML terms, in relation to the R2RML term map</figcaption>
</figure>

### fnml:FunctionMap

<dfn>fnml:FunctionMap</dfn> is a subclass of [rr:TermMap](http://www.w3.org/ns/r2rml#TermMap).
Specifically, this means that, when a FunctionMap is used within a <a>RML mapping</a>,
this term map has two classes: `fnml:FunctionMap`, and the term map within the context of the RML Mapping,
namely, subject map, predicate map, object map, or graph map.
As a consequence, all default [[RML]] processing hold, e.g.,
the [default term type depends on whether the term map is an object map or not](https://rml.io/specs/rml/#termtype),
**with following extension**:

If the term map does not have a `rr:termType` property, then its [term type](https://rml.io/specs/rml/#term-type) is:
* `rr:Literal`, if it is an [object map](https://www.w3.org/TR/r2rml/#dfn-object-map) and at least one of the following conditions is true:
   * It is a [reference-based term map](https://rml.io/specs/rml/#reference-valued-term-map),  **or also a fnml:FunctionMap**
   * It has a `rml:languageMap` and/or `rr:language` property (and thus a [language map](https://rml.io/specs/rml/#language-map) and/or a [specified language tag](https://rml.io/specs/rml/#specified-language-tag)).
   * It has a `rr:datatype` property (and thus a [specified datatype](https://rml.io/specs/rml/#specified-datatype)).
* `rr:IRI`, otherwise.

<p class="issue" data-number="5" data-format="markdown">
It is still undecided whether this extension should stay (so `rr:Literal` by default),
or go (so `rr:IRI` by default).
</p>

<p class="issue" data-number="7" data-format="markdown">
It is currently unspecified how to override the termtype of a fnml:FunctionMap result.
</p>

<p class="note" data-format="markdown">
It is currently assumed that an `fnml:FunctionMap` always returns an RDF term [[rdf-concepts]] or list thereof.
How a list of RDF terms is handled, is out of scope of this spec, but currently discussed at https://github.com/kg-construct/mapping-challenges/pull/26 and https://github.com/kg-construct/mapping-challenges/pull/27
</p>

### fnml:functionValue

<dfn>fnml:functionValue</dfn> connects the knowledge graph generating triples map with a function execution triples map.
It has range <a>fnml:FunctionMap</a> and domain rr:TriplesMap.
The triples map to which <a>fnml:functionValue</a> refers to should be an [[RML]] conforming triples map
that generates an <a>execution</a> description.

#### Logical source

When this triples map **does not specify a logical source**, the logical source of the 'parent' triples map is used.
When the triples map _does_ define a logical source (different from the logical source of the knowledge graph generating triples map),
then each result of each iteration of the function execution triples map should be used by the knowledge graph generating triples map
(i.e., a full join).
For an example on joining values across data sources, without join conditions, see test case [RMLFNOTC009](https://github.com/RMLio/rml-fno-test-cases/tree/master/RMLFNOTC0009-CSV).

<p class="issue" data-number="2" data-format="markdown">
It is still an open issue to joining values across data sources _with_ join conditions
</p>

<div class="practice">

<span class="practicelab">Joining using data transformations</span>

<p class="practicedesc" data-format="markdown">When you specifically want to have join conditions, you should use functions within [rr:joinCondition](https://www.w3.org/TR/r2rml/#foreign-key),
see, e.g. test case [RMLFNOTC0019](https://github.com/RMLio/rml-fno-test-cases/tree/master/RMLFNOTC0019-CSV).
</p>
</div>

<p class="issue" data-number="4" data-format="markdown">
The mapping challenge [Join on literals](https://github.com/kg-construct/mapping-challenges/pull/29) also influences this spec.
</p>

#### Subject map

When this triples map **does not specify a subject map**, a blank node should be generated for the subject.

<div class="note">
We should probably define a new resource that is a subclass of rr:TriplesMap,
as the description above is disjoint with rr:TriplesMap, as logical source and subjectMap are not optional in [[R2RML]]
</div>

### Nested functions

As the range of `fnml:functionValue` is `rr:TriplesMap`,
it is possible to nest functions: you generate a term in a first function, and that term is used as an parameter value in a second function.
For an example, see [RMLFNOTC0018](https://github.com/RMLio/rml-fno-test-cases/tree/master/RMLFNOTC0018-CSV).

<p class="issue" data-number="3" data-format="markdown">
For now, it is unclear how to handle a nested function where that nested triplesmap contains a join condition.
</p>
