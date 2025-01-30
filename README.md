# Bachelor Project 2022 - Blif2GV Translator

My Bachelor Project @ USI - Università della Svizzera Italiana.  
More information can be find in my [Bachelor Project Report](https://github.com/matteoalberici4/blif2gv-translator/blob/main/docs/bachelor_project_report.pdf).

## Introduction

The *Blif2GV Translator* is an application that offers a clear graphical view of a circuit. This converter inputs a *blif* file holding the textual representation of a Boolean circuit and outputs the corresponding file in *GV* format.  
The entire translator was developed using the Python programming language. The following sections offer a detailed explanation of what happens during each execution phase.
Since the *Blif2GV Translator* deals with Boolean circuits, we must introduce a few notions. Boolean
logic is the branch of algebra in which the values of the variables are the truth values true and
false, usually denoted by the numbers 1 and 0, respectively. George Boole introduced it in the
book "The Mathematical Analysis of Logic" [1847]. A Boolean operator is a function that takes
binary variables in input, processes them, and returns a single binary output (i.e., either 1 or 0).
Let us analyze the following example, representing an AND operator:

    1 ∧ 0 = 0

Such operations are defined by truth tables, wherein the combinations of inputs and the corresponding output are shown. Given the fact that we could encounter any type of unary (i.e., one
input - one output) and binary (i.e., two inputs - one output) operators while parsing a *blif* file, we should define each possible input(s)-output relation in order to be able to understand each component of a Boolean circuit. Every Boolean operator is exhaustively defined in Appendix A,
along with the corresponding truth table.
<br>

### Introducing the blif Format

*The Berkeley Logic Interchange Format* (BLIF) represents a logic-level hierarchical circuit in
textual form. The term circuit refers to a combinational and sequential network of Boolean functions which can be viewed as a directed graph, where each node can be broken up into the
following components:

* **Inputs**: the set of inputs received by the node; it could consist of a single input, in the case of a
unary operator, an ordered pair of inputs, in the case of a binary operator, or a sequence of
inputs with no pre-defined limits, in the case of a special operator. In the latter is the case,
then the node must be declared in a .subckt.
* **Operator**: the operator that processes the input received by the node and returns the corresponding
output; it could be a unary operator, such as NOT, a binary operator, such as AND, or a
special operator, such as MUX.
* **Output**: the single output returned by the operator after the latter finishes processing the received
input.

The file’s body is composed of "commands", which are lines that declare logic gates. The circuit nodes are defined by specifying the input(s), the operator, and the output. There exist two
different ways of writing such definitions:

* *.subckt*  
This kind of definition has the following syntax:  

        .subckt $<operator> A=<input> [B=<input2> ...] Y=<output>

    Every pair *letter=name* but the last one represents an input of the defined node. The following example shows a logical AND gate definition:  

        .subckt $and g0 g1 g2

* *.names*  
This kind of definition has the following syntax:

        .names <input> [<input2> ...] <output>
        <truth-table>

    The operator is defined by the truth table declared in the lines immediately below. A truth
table is defined by one or more lines of numbers, each indicating a boolean relation that
returns the logic value true. There must be a sequence of non-separated numbers, one for
each input, and a number for the output, white-space-separated by the first sequence. The
following example shows a logical AND gate definition:

        .names g0 g1 g2
        11 1
<br>

### Introducing the GV Format

A *Graphviz Dot* (GV) file provides the characteristics of a graph and is written using the DOT
language. The body of a *GV* file can be broken up into two parts: the nodes declaration and the
edges assignment. Each node-declaring line defines a single gate using the following syntax:  

    <node_name> [label="<node_label>" <style>]

The name displayed after converting a *GV* file into a pdf is the value of the property label. Each
edge-declaring line defines a link from a source node to a destination node with the following
syntax:

    <source_node> -> <destination_node>

<br>

### Blif2GV Algorithm Description

Since we deal with logic circuits, we need to implement a way of representing a circuit. A circuit
object has a set of inputs, a set of outputs, and a set of sub-circuits, and it is created by parsing
a *blif* file’s header. Moreover, we must design a way of defining the objects a circuit is made of:
the sub-circuits. A sub-circuit object has a set of inputs, an operator, and a single output and
represents a circuit gate.  
The following is the procedure performed by the translator:

1. Generate a ckt object from the given file
2. Set the subckts list to []  
3. Open the given file  
4. For each line in the file do:
    1. Create a subckt object
    2. Append the subckt to the subckts list
5. Close the file
6. Assign the subckts list to the ckt
7. Assign children and parents to each subckt
8. Simplify the ckt
9. Return the ckt

In order to parse .name lines, we must perform a few more operations.
In the case of such a line, we need to parse the first line to get the input(s) and the output; then,
we must parse the truth table defined in the following lines to assign the corresponding operator.
The encounterable truth tables are defined in dictionaries created by permuting each operator
definition. As a result, a truth table is identified independently of how it is declared.

<br>

### Fixing the Syntax

After implementing the translator, we wish to program more features to generate more simple
circuit.  
Given that the syntax of a *GV* file rejects several symbols that, in contrast, could be used in a
*blif* file, we must modify everything that could lead to an error. More specifically, the *GV* syntax
does not accept non-alphanumeric characters at the beginning of a gate name and many special
symbols inside it.
Let us examine the following example, taken from *BLASYS*:

    .subckt $and A=$not$abs_.v:164$307_Y B=$not$abs_.v:164$308_Y Y=$and$abs_.v:164$309_Y
                                ⇓
    1) input: n164_307_Y operator: and output: n164_309_Y <br>
    2) input: n164_308_Y operator: and output: n164_309_Y

<br>

### Removing Useless ASSIGN Gates

The role of an ASSIGN gate is renaming the received input and forwarding it to another gate. Since
these gates are introduced by *blif* files and do not alter the semantical meaning of the circuit, we
decided to remove such gates. We must ensure that each link is set correctly after the removal
in order not to get errors.

### Removing Redundant NOT Gates

A NOT gate changes the value of the input received into its complement (i.e., from true to false
and vice-versa). Two or more NOT gates are redundant if the value outputted by the last gate of
the sequence is equal to the value taken in input by the first gate.

### Executing the Translator: TUI

In order to run the translator with a Text-based User Interface (TUI), it is sufficient to type the following command while
being in the project’s root directory:

    python3 main.py <blif_file_name> [dot]

The placeholder *blif_file_name* must be replaced by the path of the *blif* file that the user
wants to convert. Moreover, it is possible to add the argument dot to convert the newly generated
*GV* file into a pdf using DOT at the end of the translation process.
Depending on the result of the translation process, a different message will be displayed in the
standard output. The code handles several types of errors.

### Executing the Translator: GUI

In order to run the translator with the Graphical User Interface (GUI), it is sufficient to execute the python script *main.py*
with no additional arguments while being in the project’s root directory:

    python3 main.py

The script will then display the initial window of the GUI.
In the top-center part of the window, there are a text area and a button labeled *Browse*: the user
can either type the path to a folder containing at least one *blif* file or search for it by clicking on
the button. If the folder selected by the user contains at least one *blif* file, then the window will
display a list of all the *blif* files found in that directory on the left. The window will display an
error if the selected folder holds no *blif* files. By clicking on one of the displayed *blif* files, the corresponding line of the list will be highlighted.
The window will then display the name of the *blif* file on the left, along with a button labeled
*Convert*: if the user clicks on the latter, then the selected *blif* file will be converted to *GV* and pdf.
Finally, depending on the result of the translation process, a different message will be displayed
on the window. The code handles several types of errors.
