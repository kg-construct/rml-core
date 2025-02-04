#!/bin/bash

for i in RML*; do
	echo "<section id=\"$i\" data-include=\"$i/README.md\" data-include-format="markdown"></section>"
done
