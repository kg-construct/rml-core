# Generating values with expressions

<dfn>Expressions</dfn> are mapping constructs that can be evaluated on a [=logical iteration=], according to the specified [=reference formulation=], to generate values during the mapping process.

## Expression map (`rml:ExpressionMap`)

An <dfn>expression map</dfn> (`rml:ExpressionMap`) is an abstract class, that is specialized by other RML classes. An [=expression map=] MUST have one the following properties:
* 0 or 1 `rml:constant`, or
* 0 or 1 `rml:reference`, or
* 0 or 1 `rml:template`, or
* another property, or properties, defined by a subclass of `rml:ExpressionMap`.

Each of these properties specifies an [=expression=] which, upon evaluation, results in a naturally ordered list of values (i.e., preserving the order in which they are produced by the iterations), called the <dfn>expression evaluation result</dfn>.

The <dfn>reference expression set</dfn> of an [=expression map=] is the set of expressions which are evaluated on a [=logical iteration=].

### Constant expression (`rml:constant`)

A <dfn>constant-valued expression map</dfn> is an [=expression map=] that always generates the same [=expression evaluation result=]. A constant-valued expression map is represented by a resource that has exactly one `rml:constant` property, the value of which is called a <dfn>constant expression</dfn>.

The <dfn>constant value</dfn> is a singleton list containing the [=constant expression=].

The [=reference expressions=] of a [=constant-valued expression map=] is an empty list.

### Reference (`rml:reference`)
A <dfn>reference-valued expression map</dfn> is an [=expression map=] that is represented by a resource that has exactly one `rml:reference` property, the value of which is called a <dfn>reference expression</dfn>.

The [=reference expression=] MUST be a valid [=expression=] according to the defined [=reference formulation=] in the [=logical source=].

The [=reference expression set=] of a [=reference-valued expression map=] is the singleton set containing the [=reference expression=].

The <dfn>reference value</dfn> is the [=expression evaluation result=] obtained by evaluating the [=reference expression=] against a given [=logical iteration=].

### Template (`rml:template`)
A <dfn>template-valued expression map</dfn> is an [=expression map=] that is represented by a resource that has exactly one `rml:template` property, the value of which is called a <dfn>template expression</dfn>. The [=template expression=] MUST be a valid [=string template=].

A <dfn>string template</dfn> is a format string that can be used to build strings from multiple components. It can apply [=reference expressions=] by enclosing them in curly braces (`{` and `}`). The following syntax rules apply to valid [=string templates=]:

* Pairs of unescaped curly braces MUST enclose valid [=reference expressions=].
* Curly braces that do not enclose [=reference expressions=] MUST be escaped by a backslash character (`\`). This also applies to curly braces within [=reference expressions=].
* Backslash characters (`\`) MUST be escaped by preceding them with another backslash character, yielding (`\\`). This also applies to backslashes within [=reference expressions=].
* There SHOULD be at least one pair of unescaped curly braces.

The [=reference expression set=] of a [=template expression=] is the set of [=reference expressions=] enclosed in unescaped curly braces in the [=string template=].

Sub classes of [=template-valued expression maps=] MAY define a <dfn>reference value transforming function</dfn> which will be applied to each [=reference value=] when evaluating the template.

The <dfn>template value</dfn> when evaluating a [=string template=] for a given [=logical iteration=] is determined as follows:
1. Let `result` be the [=reference expression set=] of the [=string template=]
2. For each [=reference expression=] in `result`:
    1. Let `values` be the [=reference value=] of the [=reference expression=] that is enclosed in the curly braces
    2. If `values` is an empty list, then return `NULL`
    3. For each `value` in `values`:
        1. Let `value` be the [=natural RDF lexical form=] corresponding to `value`
3. Let `result` be the [=n-ary Cartesian product=] of `result`
4. For each ordered list `product` in `result`:
    1. Let `template` be the [=string template=]
    2. For each pair of unescaped curly braces in `template`:
        1. Let `value` be the value at the index of `product` corresponding with the index of `value` in `template`
        2. If a [=reference value transforming function=] is applicable, let `value` be the value after applying the [=reference value transforming function=]
        3. Replace the pair of curly braces with `value`
    3. Let `product` be `template`
5. Return `result`
