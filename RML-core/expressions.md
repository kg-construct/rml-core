# Generating values with expressions

To be able to map data from structured sources to RDF, expressions are needed. <dfn>Expressions</dfn> are mapping constructs that can be evaluated on a data source, according to the specified reference formulation, to generate values during the mapping process.

## Expression map (`rml:ExpressionMap`)

An <dfn>expression map</dfn> (`rml:ExpressionMap`) is an abstract class, that is specialized by other RML classes. An [=expression map=] can have at least the following properties that specify:
* 0 or 1 `rr:constant`
* 0 or 1 `rml:reference`
* 0 or 1 `rr:template`

Each of these properties specifies an [=expression=] which can result in a list of values.

### Constant expression (`rr:constant`)

A <dfn>constant-valued expression map</dfn> is an [=expression map=] that always generates the same expression value. A constant-valued expression map is rerpesented by a resource that has exactly one `rr:constant` property, the value of which is called a <dfn>constant expression</dfn>.

### Reference (`rml:reference`)
A <dfn>reference-valued expression map</dfn> is a [=expression map=] that is represented by a resource that has exactly one `rml:reference` property, the value of which is called a <dfn>reference expression</dfn>.

The [=reference expression=] must be a valid [=expressions=] according to the defined [=reference formulation=].

### Template (`rr:template`)
A <dfn>template-valued expression map</dfn> is an [=expression map=] that is represented by a resource that has exactly one `rr:template` property, the value of which is called a <dfn>template expression</dfn>. The [=template expression=] MUST be a valid [=string template=].

A <dfn>string template</dfn> is a format string that can be used to build strings from multiple components. It can include [=expressions=] by enclosing them in curly braces (`{` and `}`). The following syntax rules apply to valid [=string templates=]:

* Pairs of unescaped curly braces MUST enclose valid [=expressions=].
* Curly braces that do not enclose [=expressions=] MUST be escaped by a backslash character (`\`). This also applies to curly braces within [=expressions=].
* Backslash characters (`\`) MUST be escaped by preceding them with another backslash character, yielding (`\\`). This also applies to backslashes within [=expressions=].
* There SHOULD be at least one pair of unescaped curly braces.
* If a template contains multiple pairs of unescaped curly braces, then any pair SHOULD be separated from the next one by a <dfn>safe separator</dfn>. This is any character or string that does not occur anywhere in any of the data values of either expression result.

<aside class="issue">
Pano: It is not entirely clear to me why we need the [=safe separator=]. Possibly something to do with one of the expression result values being empty?
</aside>
