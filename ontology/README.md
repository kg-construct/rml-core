# How to generate the documentation
* Download and install [WIDOCO](https://github.com/dgarijo/Widoco/releases) in this folder. Make sure you do not commit the jar file.
* Run the following command: `java -jar widoco.jar -ontFile rml-core.owl -outFolder tmp -crossRef`

The only things that are generated are the overview and the cross reference sections. These are generated in the folder `./tmp/doc`. The `tmp` folder is ignored. If the generation was successful, move the contents of `./tmp/doc` to `./documentation`. 