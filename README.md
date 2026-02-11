# PHYST

### Introduction

The **PHY**logenetic **S**tarting **T**ree (PHYST) pipeline uses popular phylogenetic software packages to pass optimised parsimony trees to likelihood software.

PHYST is currently under development at the University.

Current developers:
- Joe
- Daniel

## Getting Started

PHYST is not reliant on any external python packages, but does require Python3.11 to run.

PHYST is currently reliant on both MPBoot and IQ-Tree binaries, which are available from:

- MPBoot: http://www.iqtree.org/mpboot/ 
- IQ-Tree: http://www.iqtree.org/

Both binaries are required within the 'lib/' folder.

Currently, PHYST is ran using the following command:
~~~~
python3.11 src/main.py --msa <msa>
~~~~

### Command-line options

Run PHYST with more or few initial trees:
~~~~
--init-trees <num of trees>
~~~~ 

Parallelisation can be achived through either specifying how many cores should be used:
~~~~
--parallel <num of cores>
~~~~

or using maximum cores:
~~~~
--max-parallel
~~~~

Command-line options can be passed directly to IQ-Tree through PHYST:
~~~
-iqtree-options '<options>'
~~~
With options to be passed enclosed by quotations.

# Licence
APACHE License v2 (January 2004)

# Contact
Please direct any questions about PHYST to Joe or Daniel.