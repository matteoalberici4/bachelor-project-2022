# Bachelor Project 2022
My Bachelor Project @ USI - Università della Svizzera Italiana.

# Task 1: Blif Parser

More detailed information can be found in the [Blif Parser Guide](https://github.com/matteoalberici4/bachelor-project-2022/blob/main/Task_1/blif_parser_guide.pdf).

## 1. Introduction

This document is a guide for using the blif parser I implemented during the ﬁrst
part of my Bachelor project. What my project does until now consists of receiving a blif ﬁle in input and converting it into a gv ﬁle. Moreover, it takes the newly generated gv ﬁle and creates the correspondent pdf ﬁle using dot. Let’s have a closer look to all the ﬁles the blif parser is composed of.

## 2. Source Files

### 2.1 Classes

In order to deal with a circuit and all the gates it is composed of, I decided to implement three diﬀerent classes, described in the following paragraphs.

#### Entity

Entity is the super class that represents an object with a given set of inputs and a given set of outputs. It has only one class method, **generate()**, which is abstract. The purpose of this class is to deﬁne a blueprint which is common to both the sub-classes needed for parsing a blif ﬁle.

#### Ckt

Ckt is a sub-class of entity and represents a circuit object with a given set of inputs, a given set of outputs, and ﬁnally a list of sub-circuits the circuit itself is composed of. It has only one class method, **generate(file_name)**, which overrides the one deﬁned in the entity class. The method takes in input a blif ﬁle, retrieves from it the list of inputs and the list of outputs, and ﬁnally returns the circuit object. The list of sub-circuits will be ﬁlled while parsing the entire ﬁle.

#### Subckt

Subckt is another sub-class of the entity class and represents a sub-circuit object with a given input, a given output, and ﬁnally a given operator. It has only one class method, **generate( input, output, operator)**, which overrides the one deﬁned in the entity class. The method takes an input, an output, and an operator and simply generates a sub-circuit with the elements received in input.

### 2.2 Truth Tables

In a blif ﬁle, a sub-circuit can be represented by the following lines:

1) subckt *operator input(s) output*
2) names *input(s) output*

The lines starting with ”*.names*” are followed by one or more lines deﬁning the truth table obeyed by that sub-circuit. In the ﬁle *truth_tables.py*, there are two dictionaries, one for the unary gates and one for the binary ones, and one function, **permute(gate, combinations)**, which evaluates all the possible ways to describe an operator. While parsing a blif ﬁle, the dictionaries are read in order to ﬁnd and assign the correct operator.

### 2.3 Blif Parser

The ﬁle *blif_parser.py* deﬁnes the core function of the translator: **blif_parser(file_name)**. The function takes a blif ﬁle, generates a circuit, and then starts reading every line of the ﬁle, creating a sub-circuit for each line read. After all the sub-circuits deﬁned by the ﬁle have been created, the parser renames the inputs and the outputs through the function *ﬁx_syntax(string)*, in order to avoid errors caused by the gv syntax. Finally, the parser removes all the ”*assign*” nodes which do not lead to an output of the circuit.

### 2.4 Gv Writer

The ﬁle *gv_writer.py* deﬁnes the function which takes a ﬁle, creates a circuit object by parsing that ﬁle, and ﬁnally writes the correspondent gv ﬁle.

### 2.5 Main

The ﬁle *main.py* displays a simple GUI with some instructions in order to convert a blif ﬁle to a gv ﬁle and ﬁnally to the correspondent pdf ﬁle:

1. By clicking the button ”Browse”, the user chooses a folder containing at least one blif ﬁle
2. The user chooses a ﬁle among the ones displayed
3. By clicking the button ”Convert”, the ﬁle is ﬁrst converted to a gv ﬁle, and then to a pdf ﬁle.

The GUI also displays error/success messages after every action made.
