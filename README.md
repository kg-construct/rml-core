# The RML + FNML specification

For a rendered version, see <https://kg-construct.github.io/rml-fno-spec/>.

# Quickstart

Run a HTTP server in this directory: 

using php: `php -S localhost:8000`

using node.js: `npx serve`


# IRI Strategy followed by the specs

base: http://xxx.xx/rml/ (xxx could be w3id.org now or w3.org in the future)

core: http://xxx.org/rml/core
extension: http://xxx.org/rml/extension-name (e.g., http://xxx.org/rml/rml-star)

We are still not sure if the extensions should include the term rml or not (i.e. rml-star, rml-fno, etc).
