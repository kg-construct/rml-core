## Definitions

- <dfn>FnO</dfn>: the Function Ontology. Describes implementation-independent functions' inputs and outputs, and execution descriptions.
- <dfn>RML</dfn>: RDF Mapping Language. Describes schema transformations from heterogeneous data sources to RDF.
- An <dfn>RML mapping</dfn> is a set of mapping rules, described in <a>RML</a>.
- The <dfn>triples map</dfn> is a rule that maps each iteration in the logical source to a number of RDF triples, as [defined](https://rml.io/specs/rml/#triples-map) in the RML specification.
- The <dfn>term map</dfn> is a function that generates an RDF term from a logical reference. The result of that function is known as the term map's generated RDF term, as [defined](https://rml.io/specs/rml/#term-map) in the RML specification.
- An <dfn>RML processor</dfn> is a tool that interprets the <a>RML mapping</a> and executes its rules to generate RDF triples.
- <dfn>FNML</dfn>: describes how to integrate data transformations in schema transformations using <a>FnO</a> in <a>RML</a>.
- A <dfn>function description</dfn> describes the function, i.e., talks about the inputs and outputs of the function.
  For example, a function can have the following description: `function int sum(int a, int b)`, namely,
  the function `sum` has two input parameters, `int a` and `int b`, and returns an integer.
- An <dfn>execution</dfn> is the assignment of the values of the parameters of a function.
  An <a>execution</a> has as result the value of the output of the function.
  For example, `sum(2, 4)` is an execution.
  The value of the output is known after the function is executed, and should in this case be the integer `6`.
- An <dfn>FnML execution</dfn> is the link between RML and FnO. It specifies how to assign the values as extracted in RML (using parameter term maps) to an FnO Execution.
- An <dfn>execution term map</dfn> is a specific type of [term map](https://rml.io/specs/rml/#term-map): it is referenced from a [=triples map=], generating an [RDF term](https://rml.io/specs/rml/#rdf-term) from a specific execution result of an [=FnML execution=].

<p class="note" data-format="markdown">
It is currently assumed that an [=execution term map=] always returns an RDF term [[rdf-concepts]].
How a list of RDF terms is handled, is out of scope of this spec, but currently discussed at https://github.com/kg-construct/mapping-challenges/pull/26 and https://github.com/kg-construct/mapping-challenges/pull/27.
</p>

<p class="issue" data-number="11" data-format="markdown">
The definitions of [=execution term map=] and [=FnML execution=] are under discussion,
but also depend on the evolution of RML.
</p>
