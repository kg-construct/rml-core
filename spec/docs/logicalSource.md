# Defining Logical Sources

A <dfn>logical source</dfn> is a function on a [=data source=] that provides data to be mapped to [=RDF triples=].

A [=logical source=] (`rml:LogicalSource`) MUST have:
* exactly one `rml:referenceFormulation` property, whose value is a <dfn>reference formulation</dfn> which defines how the underlying [=data source=] is to be accessed, and which [=expressions=] can be evaluated on [=logical iterations=],
* zero or one `rml:iterator` property, whose value is a <dfn data-lt="iterator">logical iterator</dfn> that defines a sequence of [=logical iterations=] on the [=data source=]. If no [=iterator=] is provided, a <dfn class="lint-ignore">default iterator</dfn> MUST be associated with the [=reference formulation=].

A <dfn data-lt="iteration">logical iteration</dfn> is an item in the sequence produced by the [=logical source=], on which [=expressions=] can be evaluated.

A <dfn>data source</dfn> is an abstract concept that represents a source of data that can be accessed via a [=logical source=]. A [=data source=] can be a file, a database, a web service, or any other source of data.
