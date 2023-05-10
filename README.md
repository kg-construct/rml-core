# RML-Core

RML-Core specification, SHACL shapes, ontology, and test-cases

- Specification: http://w3id.org/rml/core/spec
- Ontology: http://w3id.org/rml/core
- Shapes: http://w3id.org/rml/core/shapes
- Backwards compatibility with R2RML: http://w3id.org/rml/core/bc
- Test-cases: [test-cases](./test-cases)

## Specification

The specification webpage is generated from directory [/spec](spec).

It is accessible using URL https://w3id.org/rml/core/spec.

#### Edition quickstart

- cd to [/spec](spec)
- Edit sections/index.html
- Make sure all your local assets are in the `resources` folder, and the links in your `index.html` file are relative (important because the publishing script creates multiple nested paths)
- Run a HTTP server in this directory: `python3 -m http.server`
- Open `index.html` with a browser as http://localhost:8000/index.html
- Save as snapshot to `rendered.html` [using the respec functionality](https://respec.org/docs/#using-browser) (button ReSpec/Export/HTML) and copy it to this same folder

URL https://w3id.org/rml/core/spec must redirect to the `/spec/docs`(docs) folder.


## License

RML-Core (c) by W3C Community Group on Knowledge Graph Construction

RML-Core is licensed under a
Creative Commons Attribution-ShareAlike 4.0 International License.

You should have received a copy of the license along with this
work.  If not, see <http://creativecommons.org/licenses/by-sa/4.0/>.
