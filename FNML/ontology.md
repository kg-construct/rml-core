## FNML

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
    M([fnml:FunctionTermMap]):::new
    M -->|fnml:functionValue| I([fnml:FuntionTriplesMap])
    classDef note fill:#eee,stroke-width:0px,color:#666
    classDef new fill:#8F9
    linkStyle 6 stroke:#8F9
</div>

<figure data-format="markdown">
[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggTFJcbiAgICBBKFt0ZXJtIG1hcF0pIC0tPnxycjpjb25zdGFudHwgQltjb25zdGFudCB2YWx1ZV1cbiAgICBBIC0tPnxybWw6cmVmZXJlbmNlfCBDW3JlZmVyZW5jZSBmb3JtdWxhdGlvbl1cbiAgICBBIC0tPnxycjp0ZW1wbGF0ZXwgRFtzdHJpbmcgdGVtcGxhdGVdXG4gICAgQSAtLT58cnI6dGVybVR5cGV8IEUoW3JyOklSSSAvIHJyOkJsYW5rTm9kZSAvIHJyOkxpdGVyYWxdKVxuICAgIEEgLS0-fHJyOmxhbmd1YWdlfCBGW2xhbmd1YWdlIHRhZ11cbiAgICBBIC0tPnxycjpkYXRhdHlwZXwgRyhbcmRmczpEYXRhdHlwZV0pXG4gICAgXG4gICAgSChbcnI6U3ViamVjdE1hcF0pOjo6bm90ZVxuICAgIEooW3JyOlByZWRpY2F0ZU1hcF0pOjo6bm90ZVxuICAgIEsoW3JyOk9iamVjdE1hcF0pOjo6bm90ZVxuICAgIEwoW3JyOkdyYXBoTWFwXSk6Ojpub3RlXG4gICAgTShbZm5tbDpGdW5jdGlvblRlcm1NYXBdKTo6Om5ld1xuICAgIE0gLS0-fGZubWw6ZnVuY3Rpb25WYWx1ZXwgSShbZm5tbDpGdW50aW9uVHJpcGxlc01hcF0pXG4gICAgY2xhc3NEZWYgbm90ZSBmaWxsOiNlZWUsc3Ryb2tlLXdpZHRoOjBweCxjb2xvcjojNjY2XG4gICAgY2xhc3NEZWYgbmV3IGZpbGw6IzhGOVxuICAgIGxpbmtTdHlsZSA2IHN0cm9rZTojOEY5IiwibWVybWFpZCI6e30sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggTFJcbiAgICBBKFt0ZXJtIG1hcF0pIC0tPnxycjpjb25zdGFudHwgQltjb25zdGFudCB2YWx1ZV1cbiAgICBBIC0tPnxybWw6cmVmZXJlbmNlfCBDW3JlZmVyZW5jZSBmb3JtdWxhdGlvbl1cbiAgICBBIC0tPnxycjp0ZW1wbGF0ZXwgRFtzdHJpbmcgdGVtcGxhdGVdXG4gICAgQSAtLT58cnI6dGVybVR5cGV8IEUoW3JyOklSSSAvIHJyOkJsYW5rTm9kZSAvIHJyOkxpdGVyYWxdKVxuICAgIEEgLS0-fHJyOmxhbmd1YWdlfCBGW2xhbmd1YWdlIHRhZ11cbiAgICBBIC0tPnxycjpkYXRhdHlwZXwgRyhbcmRmczpEYXRhdHlwZV0pXG4gICAgXG4gICAgSChbcnI6U3ViamVjdE1hcF0pOjo6bm90ZVxuICAgIEooW3JyOlByZWRpY2F0ZU1hcF0pOjo6bm90ZVxuICAgIEsoW3JyOk9iamVjdE1hcF0pOjo6bm90ZVxuICAgIEwoW3JyOkdyYXBoTWFwXSk6Ojpub3RlXG4gICAgTShbZm5tbDpGdW5jdGlvblRlcm1NYXBdKTo6Om5ld1xuICAgIE0gLS0-fGZubWw6ZnVuY3Rpb25WYWx1ZXwgSShbZm5tbDpGdW50aW9uVHJpcGxlc01hcF0pXG4gICAgY2xhc3NEZWYgbm90ZSBmaWxsOiNlZWUsc3Ryb2tlLXdpZHRoOjBweCxjb2xvcjojNjY2XG4gICAgY2xhc3NEZWYgbmV3IGZpbGw6IzhGOVxuICAgIGxpbmtTdHlsZSA2IHN0cm9rZTojOEY5IiwibWVybWFpZCI6e30sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)
<figcaption>FNML terms, in relation to the RML/R2RML [term map](https://rml.io/specs/rml/#term-map)</figcaption>
</figure>

### fnml:FunctionTermMap

<dfn>fnml:FunctionTermMap</dfn> is a subclass of [rr:TermMap](http://www.w3.org/ns/r2rml#TermMap),
to denote that this [term map](https://rml.io/specs/rml/#term-map) is also a [=function term map=].
Specifically, this means that, when a [=function term map=] is used within a <a>RML mapping</a>,
this [term map](https://rml.io/specs/rml/#term-map) has two classes: `fnml:FunctionTermMap`, and the [term map](https://rml.io/specs/rml/#term-map) within the context of the RML Mapping,
namely, subject map, predicate map, object map, or graph map.
As a consequence, all default [[RML]] processing hold, e.g.,
the [default term type depends on whether the term map is an object map or not](https://rml.io/specs/rml/#termtype),
**with following extension**:

If the [term map](https://rml.io/specs/rml/#term-map) does not have a `rr:termType` property, then its [term type](https://rml.io/specs/rml/#term-type) is:
* `rr:Literal`, if it is an [object map](https://www.w3.org/TR/r2rml/#dfn-object-map) and at least one of the following conditions is true:
   * It is a [reference-based term map](https://rml.io/specs/rml/#reference-valued-term-map),  **or also a [=function term map=]**
   * It has a `rml:languageMap` and/or `rr:language` property (and thus a [language map](https://rml.io/specs/rml/#language-map) and/or a [specified language tag](https://rml.io/specs/rml/#specified-language-tag)).
   * It has a `rr:datatype` property (and thus a [specified datatype](https://rml.io/specs/rml/#specified-datatype)).
* `rr:IRI`, otherwise.

<p class="issue" data-number="5" data-format="markdown">
It is still undecided whether this extension should stay (so `rr:Literal` by default),
or go (so `rr:IRI` by default).
</p>

<p class="issue" data-number="7" data-format="markdown">
It is currently unspecified how to override the termtype of a [=function term map=] result.
</p>

<p class="issue" data-number="12" data-format="markdown">
A proper Term map definition in RML is pending.
For now, we refer to the R2RML spec, but it is assumed these references will be updated based on the evolution of RML.
</p>

### fnml:FunctionTriplesMap

<dfn>fnml:FunctionTriplesMap</dfn> is a subclass of [rr:TripleMap](http://www.w3.org/ns/r2rml#TriplesMap).
The [=function triples map=] should be an [[RML]] conforming [triples map](https://rml.io/specs/rml/#triples-map)
that generates an [=execution=] description.

#### Logical source

When this triples map **does not specify a logical source**, the logical source of the 'parent' triples map is used.
When the triples map _does_ define a logical source (different from the logical source of the RDF dataset generating triples map),
then each result of each iteration of the function execution triples map should be used by the RDF dataset generating triples map
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
The blank node's ID should be unique.

### fnml:functionValue

<dfn>fnml:functionValue</dfn> connects the RDF dataset generating triples map using a [=function term map=] with a [=function triples map=].
It has domain [=fnml:FunctionTermMap=] and range [=fnml:FunctionTriplesMap=].

### Nested functions

As [=fnml:FunctionTriplesMap=] is a subclass of [rr:TripleMap](http://www.w3.org/ns/r2rml#TriplesMap),
it is possible to nest functions: you generate a term in a first function, and that term is used as an parameter value in a second function.
For an example, see [RMLFNOTC0018](https://github.com/RMLio/rml-fno-test-cases/tree/master/RMLFNOTC0018-CSV).

<p class="issue" data-number="3" data-format="markdown">
For now, it is unclear how to handle a nested function where that nested triplesmap contains a join condition.
</p>
