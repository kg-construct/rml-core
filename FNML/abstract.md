RML+FnO is an approach to provide for data transformations when generating knowledge graphs from (semi-)structured data using the [RDF Mapping Language](https://rml.io) (RML).

In RML+FnO, data transformations

- are defined declaratively using the [Function Ontology](https://fno.io) (FnO) and
- are aligned with the [RDF Mapping Language](https://rml.io) (RML).

This approach is not case-specific:
data transformations are independent of their implementation and thus interoperable,
while the functions are decoupled and reusable.
This allows developers to improve the generation framework
independent from the contributors that focus on generating the knowledge graphs.
