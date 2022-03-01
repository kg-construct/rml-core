## FNML

We use terms defined in the <a>FNML</a> ontology to link <a>RML</a> with <a>FnO</a>.

The ontology namespace is [http://semweb.mmlab.be/ns/fnml#](http://semweb.mmlab.be/ns/fnml#),
the preferred prefix is `fnml:`.

<figure>
<pre class="mermaid nohighlight override">
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
    M([fnml:ExecutionTermMap]):::new
    A -->|fnml:execution| I([fnml:Execution]):::new
    A -->|fnml:output| P([IRI]):::new
    I -->|fnml:function| N([fno:Function]):::fno
    I -->|fnml:inputParameters| O([fnml:ParameterTermMap]):::new
    O -->|fnml:predicate| Q([IRI]):::new
    classDef note fill:#eee,stroke-width:0px,color:#666
    classDef new fill:#8F9
    classDef fno fill:#F89
    linkStyle 6 stroke:#8F9
</pre>
<figcaption>FNML terms, in relation to the RML/R2RML [term map](https://rml.io/specs/rml/#term-map)</figcaption>
</figure>

### fnml:ExecutionTermMap

<dfn>fnml:ExecutionTermMap</dfn> is a subclass of [rr:TermMap](http://www.w3.org/ns/r2rml#TermMap),
to denote that this [term map](https://rml.io/specs/rml/#term-map) is also an [=execution term map=].
Specifically, this means that, when an [=execution term map=] is used within an <a>RML mapping</a>,
this [term map](https://rml.io/specs/rml/#term-map) has two classes: `fnml:ExecutionTermMap`, and the [term map](https://rml.io/specs/rml/#term-map) within the context of the RML Mapping,
namely, subject map, predicate map, object map, or graph map.
As a consequence, all default [[RML]] processing hold, e.g.,
the [default term type depends on whether the term map is an object map or not](https://rml.io/specs/rml/#termtype),
**with following extension**:

If the [term map](https://rml.io/specs/rml/#term-map) does not have a `rr:termType` property, then its [term type](https://rml.io/specs/rml/#term-type) is:
* `rr:Literal`, if it is an [object map](https://www.w3.org/TR/r2rml/#dfn-object-map) and at least one of the following conditions is true:
   * It is a [reference-based term map](https://rml.io/specs/rml/#reference-valued-term-map),  **or also an [=execution term map=]**
   * It has a `rml:languageMap` and/or `rr:language` property (and thus a [language map](https://rml.io/specs/rml/#language-map) and/or a [specified language tag](https://rml.io/specs/rml/#specified-language-tag)).
   * It has a `rr:datatype` property (and thus a [specified datatype](https://rml.io/specs/rml/#specified-datatype)).
* `rr:IRI`, otherwise.

<p class="issue" data-number="5" data-format="markdown">
It is still undecided whether this extension should stay (so `rr:Literal` by default),
or go (so `rr:IRI` by default).
</p>

An [=fnml:ExecutionTermMap=] MUST have exactly one `fnml:execution` relation.
Further, it MAY have following relations specified:

* `rr:termType`: for processing, see paragraph above
* `rr:language` OR `rml:languageMap` OR `rr:datatype`: for processing, see [RML Language Tags](https://rml.io/specs/rml/#language-tag) and [RML Typed Literals](https://rml.io/specs/rml/#typed-literals)
* `fnml:output`: this relationship MUST refer to exactly one of the output predicates as specified in the FnO [=function description=]. This signifies which result of the execution to use. The default value is the first output predicate as specified in the FnO [=function description=]. This order is deterministic as the outputs of an FnO [=function description=] are described in an rdf:List.

<p class="issue" data-number="7" data-format="markdown">
Is it still unspecified how to override the termtype of an [=execution term map=] result?
</p>

<p class="issue" data-number="12" data-format="markdown">
A proper Term map definition in RML is pending.
For now, we refer to the R2RML spec, but it is assumed these references will be updated based on the evolution of RML.
</p>

### fnml:Execution

<dfn class="lint-ignore">fnml:Execution</dfn> is a class to denote an [=FnML execution=].
It is referred from a [=fnml:ExecutionTermMap=] via the predicate `fnml:execution`.
It refers to an FnO [=function description=] via the predicate `fnml:function`,
and to zero or more input parameters via the predicate `fnml:inputParameters`.

### fnml:ParameterTermMap

<dfn>fnml:ParameterTermMap</dfn> is a subclass of [rr:TermMap](http://www.w3.org/ns/r2rml#TermMap).
All default [[RML]] processing holds,
**with the same extension as with the [=fnml:ExecutionTermMap=]**.

#### Logical source

The logical source of the [=fnml:ParameterTermMap=]s are determined by the logical source of the triples map that refers to the [=fnml:Execution=].

<p class="issue" data-format="markdown">
For an old example on joining values across data sources, without join conditions, see test case [RMLFNOTC009](https://github.com/RMLio/rml-fno-test-cases/tree/master/RMLFNOTC0009-CSV).
</p>

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

### fnml:execution

fnml:execution connects the RDF dataset generating triples map via a [fnml:ExecutionTermMap] with a [=fnml:Execution=].
It has domain [=fnml:ExecutionTermMap=] and range [=fnml:Execution=].

### fnml:output

<dfn class="lint-ignore">fnml:output</dfn> connects the RDF dataset generating triples map via a [fnml:ExecutionTermMap] with an output predicate.
It has domain [=fnml:ExecutionTermMap=] and range [rdf:Property].

### fnml:function

<dfn class="lint-ignore">fnml:function</dfn> connects the [fnml:Execution] with an FnO [=function description=].
It has domain [=fnml:Execution=] and range [fno:Function](https://w3id.org/function/ontology#Function).

### fnml:predicate

<dfn class="lint-ignore">fnml:predicate</dfn> connects the [fnml:ParameterTermMap] with a parameter predicate.
It has domain [=fnml:ParameterTermMap=] and range [rdf:Property].

### Nested functions

As [=fnml:ParameterTermMap=] is a subclass of [=term map=],
it is possible to nest functions: you generate a term in a first function, and that term is used as an parameter value in a second function.

<p class="issue" data-format="markdown">
For an old example, see [RMLFNOTC0018](https://github.com/RMLio/rml-fno-test-cases/tree/master/RMLFNOTC0018-CSV).
</p>

<p class="issue" data-number="3" data-format="markdown">
For now, it is unclear how to handle a nested function where that nested triplesmap contains a join condition.
</p>

```turtle "example": "using toUppercase in an RML mapping"
<#Person_Mapping>
    rml:logicalSource <#LogicalSource> ;
    rr:subjectMap <#SubjectMap> ;
    rr:predicateObjectMap <#NameMapping> .

<#NameMapping>
    rr:predicate dbo:title ;
    rr:objectMap <#ExecutionTermMap> .

<#ExecutionTermMap> a fnml:ExecutionTermMap ;
    fnml:execution <#Execution> ;
    fnml:output grel:stringOutput .

<#Execution> a fnml:Execution ;
    fnml:function grel:toUppercase ;
    fnml:inputParameters
        [
            a fnml:ParameterTermMap
            fnml:predicate grel:stringInput ;
            fnml:execution <#Execution2> ;     # Link to the nested execution
            fnml:output grel:stringOutput .    # Specify which output of the nested execution is taken
        ] .

<#Execution2> a fnml:Execution ;               # First, replace spaces with dashes from the `name` reference
    fnml:function grel:string_replace ;
    fnml:inputParameters
        [
            a fnml:ParameterTermMap
            fnml:predicate grel:valueParameter ;
            rr:reference "name" .
        ] ;
        [
            a fnml:ParameterTermMap
            fnml:predicate grel:p_string_find ;
            rr:reference " " .
        ] ;
        [
            a fnml:ParameterTermMap
            fnml:predicate grel:p_string_replace ;
            rr:reference "-" .
        ] ;
```

[rdf:Property]: http://www.w3.org/1999/02/22-rdf-syntax-ns#Property
