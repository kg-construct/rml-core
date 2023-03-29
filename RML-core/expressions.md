# Generating values with expressions

To be able to map data from structured sources to RDF, expressions are needed. <dfn>Expressions</dfn> are mapping constructs that can be evaluated on a data source, according to the specified reference formulation, to generate values during the mapping process. These values are called <dfn>expression values</dfn>.

## Expression map (`rml:ExpressionMap`)

An <dfn>expression map</dfn> (`rml:ExpressionMap`) is an abstract class, that is specialized by other RML classes. An [=expression map=] MAY have one the following properties that specify:
* 0 or 1 `rr:constant`, or
* 0 or 1 `rml:reference`, or
* 0 or 1 `rr:template`

Each of these properties specifies an [=expression=] which can result in a set of [=expression values=].

### Constant expression (`rr:constant`)

A <dfn>constant-valued expression map</dfn> is an [=expression map=] that always generates the same [=expression value=]. A [=constant-valued expression map=] is represented by a resource that has exactly one `rr:constant` property, the value of which is called a <dfn>constant expression</dfn>.

The [=constant expression=] MUST be a valid [RDF term](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-term).

The <dfn>constant value</dfn> is a singleton set containing the [=constant expression=].

### Reference (`rml:reference`)
A <dfn>reference-valued expression map</dfn> is an [=expression map=] that is represented by a resource that has exactly one `rml:reference` property, the value of which is called a <dfn>reference expression</dfn>.

The [=reference expression=] MUST be a valid [=expression=] according to the defined [=reference formulation=].

The <dfn>reference value</dfn> is a set of values obtained by evaluating the expression against a given [=logical source record=].

### Template (`rr:template`)
A <dfn>template-valued expression map</dfn> is an [=expression map=] that is represented by a resource that has exactly one `rr:template` property, the value of which is called a <dfn>template expression</dfn>. The [=template expression=] MUST be a valid [=string template=].

A <dfn>string template</dfn> is a format string that can be used to build strings from multiple components. It can include [=reference expressions=] by enclosing them in curly braces (`{` and `}`). The following syntax rules apply to valid [=string templates=]:

* Pairs of unescaped curly braces MUST enclose valid [=reference expressions=].
* Curly braces that do not enclose [=reference expressions=] MUST be escaped by a backslash character (`\`). This also applies to curly braces within [=reference expressions=].
* Backslash characters (`\`) MUST be escaped by preceding them with another backslash character, yielding (`\\`). This also applies to backslashes within [=reference expressions=].
* There SHOULD be at least one pair of unescaped curly braces.

The <dfn>template reference expressions</dfn> of a [=template expression=] is the set of [=reference expressions=] enclosed in unescaped curly braces in the [=string template=].

<aside class="issue">
SHOULD there be at least one pair of unescaped curly braces?
</aside>

The <dfn>template value</dfn> when evaluating a [=string template=] for a given [=logical source record=] is determined as follows:
1. Let `result` be the [=template reference expressions=] of the [=string template=]
2. For each [=reference expression=] in `result`:
    1. Let `values` be the [=reference value=] of the [=reference expression=] that is enclosed in the curly braces
    2. If `values` is an empty set, then return `NULL`
    3. For each `value` in `values`:
        1. Let `value` be the [=natural RDF lexical form=] corresponding to `value`
3. Let `result` be the [=n-ary Cartesian product=] of `result`
4. For each ordered list `product` in `result`:
    1. Let `template` be the [=string template=]
    2. For each pair of unescaped curly braces in `template`:
        1. Let `value` be the value at the index of `product` corresponding with the index of `value` in `template`
        2. Replace the pair of curly braces with `value`
    3. Let `product` be `template`
5. Return `result`
