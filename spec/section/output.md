# The Output Dataset
The <dfn>output dataset</dfn> of an [=RML mapping=] is an [=RDF dataset=] that contains the [=generated RDF triples=] for each of the [=triples maps=] of the [=RML mapping=]. 
The [=output dataset=] MUST NOT contain any other [=RDF triples=] or [=named graphs=] besides these. 
However, [=RML processors=] MAY provide access to datasets that contain additional triples or graphs beyond those in the [=output dataset=], such as inferred triples or provenance information.

Conforming [=RML processors=] MAY rename [=blank nodes=] when providing access to the [=output dataset=]. 
This means that client applications may see actual [=blank node identifiers=] that differ from those produced by the [=RML mapping=]. 
Client applications SHOULD NOT rely on the specific text of the blank node identifier for any purpose.

<aside class="note">
RDF syntaxes and RDF APIs generally represent [=blank nodes=] with [=blank node identifiers=]. But the characters allowed in [=blank node identifiers=] differ between syntaxes, and not all characters occurring in the values produced by a [=term map=] may be allowed, so a bijective mapping function from values to valid [=blank node identifiers=] may be required. The details of this mapping function are implementation-dependent, and [=RML processors=] may have to use different functions for different output syntaxes or access interfaces. Strings matching the regular expression `[a-zA-Z_][a-zA-Z_0-9-]*` are valid [=blank node identifiers=] in all W3C-recommended RDF syntaxes (as of this document's publication).
</aside>

<aside class="note">
[=RDF datasets=] may contain empty [=named graphs=]. RML cannot generate such [=output datasets=].
</aside>

## The Generated RDF Triples of a Triples Map

This subsection describes the process of <dfn data-lt="generated RDF triples">generating RDF triples</dfn> from a [=Triples Map=]. This process contributes [=RDF triples=] to the [=output dataset=]. Each generated triple MUST be placed into one or more graphs of the output dataset.

The [=generated RDF triples=] are determined by the following algorithm. [=RML Processors=] MAY employ alternative implementations to compute the generated [=RDF triples=], provided that the resulting output dataset is semantically equivalent to the one obtained by this algorithm.


Let:

- **sm** be the [=subject map=] of the [=Triples Map=].
- **iterations** be the set of [=logical iterations=] obtained by evaluating the [=logical source=] of the [=Triples Map=] using its declared [=reference formulation=].
- **classes** be the set of [=class IRIs=] defined in **sm** (via `rml:class`).
- **sgm** be the set of [=graph maps=] attached to **sm**.

For each [=logical iteration=]  **iteration** in **iterations**, apply the following steps:

1. Let [=subject=] be the [=RDF term=] resulting from applying **sm** to **iteration**.
2. Let **subject_graphs** be the set of [=generated RDF terms=] resulting from applying each graph map in **sgm** to **iteration**.
3. For each [=class IRI=] in **classes**, add a triple to the [=output dataset=] as follows:

   | Component | Value |
   |------------|--------|
   | Subject | **subject** |
   | Predicate | `rdf:type` |
   | Object | class IRI |
   | Target graphs | If **sgm** is empty → `rml:defaultGraph`; otherwise → **subject_graphs** |

4. For each [=predicate-object map=] of the Triples Map, apply the following steps:

   - Let **predicates** be the set of [=RDF terms=] resulting from applying each predicate map of the predicate-object map to **iteration**.
   - Let **objects** be the set of [=generated RDF terms=] resulting from applying each [=object map=] (excluding [=referencing object maps=]) to **iteration**.
   - Let **pogm** be the set of graph maps of the predicate-object map.
   - Let **predicate_object_graphs** be the set of [=generated RDF terms=] resulting from applying each [=graph map=] in **pogm** to **iteration**.

   For each possible combination `<predicate, object>`, where *predicate* ∈ **predicates** and *object* ∈ **objects**, add a triple to the output dataset as follows:

   | Component | Value |
   |------------|--------|
   | Subject | **subject** |
   | Predicate | *predicate* |
   | Object | *object* |
   | Target graphs | If both **sgm** and **pogm** are empty → `rml:defaultGraph`; otherwise → union(**subject_graphs**, **predicate_object_graphs**) |


For each [=referencing object map=] of a [=predicate-object map=] in the [=Triples Map=] apply the following steps:

- Let **psm** be the [=subject map=] of the [=parent Triples Map=] referenced by [=referencing object map=].
- Let **pogm** be the set of [=graph maps=] of the [=predicate-object map=].
- Let **joined_iterations** be the result of evaluating the [=join conditions=] defined by the [=referencing object map=], combining iterations from both the [=child logical source=] and [=parent logical sources=].

For each pair `<child_iteration, parent_iteration>` in **joined_iterations**, apply the following steps:

1. Let **subject** be the [=RDF terms=] resulting from applying **sm** to **child_iteration**.
2. Let **predicates** be the set of [=RDF terms=] resulting from applying each [=predicate map=] of the [=predicate-object map=] to **child_iteration**.
3. Let **object** be the [=RDF terms=] resulting from applying **psm** to **parent_iteration**.
4. Let **subject_graphs** be the set of RDF terms resulting from applying each graph map in **sgm** to **child_iteration**.
5. Let **predicate_object_graphs** be the set of RDF terms resulting from applying each graph map in **pogm** to **child_iteration**.

For each *predicate* in **predicates**, add a triple to the output dataset as follows:

| Component | Value |
|------------|--------|
| Subject | **subject** |
| Predicate | *predicate* |
| Object | **object** |
| Target graphs | If both **sgm** and **pogm** are empty → `rml:defaultGraph`; otherwise → union(**subject_graphs**, **predicate_object_graphs**) |


#### Adding Triples to the Output Dataset

“Add triples to the output dataset” is a process that takes the following inputs:

| Input | Description                                     |
|--------|-------------------------------------------------|
| **Subject** | an [=IRI=], a [=URI=], [=blank node=], or empty |
| **Predicate** | an [=IRI=], a [=URI=], or empty                 |
| **Object** | an [=RDF term=] or empty                        |
| **Target graphs** | a set of zero or more [=IRIs=]                  |

Execute the following steps:

1. If **Subject**, **Predicate**, or **Object** is empty, **abort** these steps.  
2. Otherwise, generate an [=RDF triple=] `<Subject, Predicate, Object>`.  
3. If the set of target graphs includes `rml:defaultGraph`, add the triple to the [=default graph=] of the [=output dataset=].  
4. For each [=IRI=] in the set of target graphs not equal to `rml:defaultGraph`, add the triple to the [=named graph=] identified by that [=IRI=] in the [=output dataset=].  
   - If the [=named graph=] does not yet exist, create it.  
5. RDF graphs MUST NOT contain duplicate triples. Adding multiple identical triples to the same graph has the same effect as adding it once.  
6. The scope of blank nodes is limited to the output dataset being generated.

### Generated RDF Term of a Term Map


A [=term map=] defines how an [=RDF term=] is generated from the evaluation of a [=logical iteration=] over a [=logical source=].  
The result of evaluating a term map for a given [=logical iteration=] can be one of the following:

- **Empty**, if any referenced value of the [=term map=] evaluates to a null, empty or missing value (each data format defines it in [RML-IO-Registry](https://w3id.org/kg-construct/rml-io-registry/));  
- **An [=RDF term=]**, when evaluation produces a valid [=RDF term=] according to the [=term generation rules=];  
- **A [=data error=]**, when a valid RDF term cannot be produced.

The [=generated RDF term=] of a [=term map=] for a given [=logical iteration=] is determined as follows:

1. If the term map is a [=constant-valued term map=], then the generated RDF term is the term map’s [=constant value=].
2. If the term map is a [=reference-valued term map=], then the generated RDF term is determined by applying the [=term generation rules=] to its [=reference value=].
3. If the term map is a [=template-valued term map=], then the generated RDF term is determined by applying the [=term generation rules=] to the [=template value=].

The <dfn>term generation rules</dfn> define how a concrete RDF term is generated from each value from an [=expression evaluation result=]:

1. **If the value is null, empty or missing**, then no RDF term is generated.

2. **If the term type is `rml:IRI`:**
   1. Let *value* be the [=natural RDF lexical form=] corresponding to the evaluated value.
   2. If *value* is a valid [absolute IRI](https://datatracker.ietf.org/doc/html/rfc3987#section-2.2) [[RFC3987]], then return an [=IRI=] generated from *value*.
   3. Otherwise, prepend *value* with the [=base IRI=]. If the result is a valid [absolute IRI](https://datatracker.ietf.org/doc/html/rfc3987#section-2.2) [[RFC3987]], then return that [=IRI=].
   4. Otherwise, raise a **data error**.

3. **If the term type is `rml:URI`:**
   1. Let *value* be the [=natural RDF lexical form=] corresponding to the evaluated value.
   2. If *value* is a valid [=absolute URI=] [[RFC3986]], then return an [=URI=] generated from *value*.
   3. Otherwise, prepend *value* with the [=base IRI=]. If the result is a valid [=absolute URI=] [[RFC3986]], then return that [=URI=] .
   4. Otherwise, raise a **data error**.

4. **If the term type is `rml:BlankNode`:**
   - Return a blank node that is unique in the target graph.

5. **If the term type is `rml:Literal`:**
   - If the term map declares a [=language map=], then evaluate the [=language map=] to obtain a [=language tag=] and return a literal with that [=language tag=] and the natural RDF lexical form corresponding to *value*.
   - Otherwise, if the term map declares a [=datatype map=], then evaluate it to obtain a [=datatype-override RDF literal=] corresponding to *value* and the specified datatype.
   - Otherwise, return the [=natural RDF literal=] corresponding to *value*.




