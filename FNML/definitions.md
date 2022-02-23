## Definitions

- <dfn>FnO</dfn>: the Function Ontology. Describes implementation-independent functions' inputs and outputs, and execution descriptions.
- <dfn>RML</dfn>: RDF Mapping Language. Describes schema transformations from heterogeneous data sources to RDF.
- An <dfn>RML mapping</dfn> is a set of mapping rules, described in <a>RML</a>.
- The <dfn>triples map</dfn> is a rule that maps each iteration in the logical source to a number of RDF triples, as [defined](https://rml.io/specs/rml/#triples-map) in the RML specification.
- An <dfn>RML processor</dfn> is a tool that interprets the <a>RML mapping</a> and executes its rules to generate RDF triples.
- <dfn>FNML</dfn>: describes how to integrate data transformations in schema transformations using <a>FnO</a> in <a>RML</a>.
- A <dfn>function description</dfn> describes the function, i.e., talks about the inputs and outputs of the function.
  For example, a function can have the following description: `function int sum(int a, int b)`, namely,
  the function `sum` has two input parameters, `int a` and `int b`, and returns an integer.
- An <dfn>execution</dfn> is the assignment of the values of the parameters of a function.
  An <a>execution</a> has as result the value of the output of the function.
  For example, `sum(2, 4)` is an execution.
  The value of the output is known after the function is executed, and should in this case be the integer `6`.
- A <dfn>function triples map</dfn> is a specific type of [=triples map=] that MUST NOT specify a logical source. The logical source of the [=function triples map=] always defaults to the logical source of the [=triples map=] that is being executed. It is is used to describe an [=execution=] using [=RML=], but the generated execution triples are not part of the output.
  The output of a function triples map is a function execution result, an internal set of triples which can be referred to by one or more [=function term map=]s.
- A <dfn>function term map</dfn> is a specific type of [term map](https://rml.io/specs/rml/#term-map): it is referenced from an [=triples map=], generating an [RDF term](https://rml.io/specs/rml/#rdf-term) from the execution result of a [=function triples map=].

<p class="note" data-format="markdown">
The [subject map](https://rml.io/specs/rml/#subject-map) of a [=function triples map=] should be specified, conforming to the [=triples map=] definition.
However, for brevity, when no subject map is specified, a blank node is generated as subject of the [=execution=].
</p>

<p class="note" data-format="markdown">
_How_ a unique blank node for an execution is generated, is under discussion.
</p>

<p class="note" data-format="markdown">
It is currently assumed that a [=function term map=] always returns an RDF term [[rdf-concepts]].
How a list of RDF terms is handled, is out of scope of this spec, but currently discussed at https://github.com/kg-construct/mapping-challenges/pull/26 and https://github.com/kg-construct/mapping-challenges/pull/27.
</p>

<p class="issue" data-number="11" data-format="markdown">
The definitions of [=function term map=] and [=function triples map=] are under discussion,
but also depend on the evolution of RML.
</p>

<p class="issue" data-number="29" data-format="markdown">
Currently, how to refer to the output of an execution is underspecified.
</p>

[triples map]: https://rml.io/specs/rml/#triples-map
