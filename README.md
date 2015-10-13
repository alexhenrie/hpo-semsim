The general idea:

1. Define groups of HPO terms in instance_annots.tsv
2. List pairs of groups to be compared in input_queries.tsv
3. Execute the SML Toolkit with the included XML configuration file (doit.sh or
   doit.py)

There are three folders, each with a different doit file:
* **set-to-set-similarities:** Takes a list of sets and compares each set to every
  other set in the list using a variety of similarity measures.
* **term-specificities:** Computes the specificity of the term according to the
  Rada, Kyogoku, and Eilbeck1 measures.
* **term-to-set-similarities:** Compares each term from all sets to each
  individual set, returning the best SimUI score between the term and each of
  the terms in the set.

Example:
```
./get-deps.sh
cd set-to-set-similarities
./doit.sh noonan-sets
cp noonan-sets/set-to-set-similarities.tsv ~/Desktop
````

References:
* http://www.semantic-measures-library.org/sml/index.php?q=toolkit
* https://groups.google.com/d/msg/sml-support/CzhS5cRTapE/KcHcKLkKxUsJ
