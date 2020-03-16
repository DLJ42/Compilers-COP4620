# Project 4 Semantics

* due 3/26/20 Thursday 11:59 PM (nearly midnight)

## GRADING

* **25 total points on project**

* 2 points for p4 script (including making it executable)
* 2 points for makefile
* 2 points for typescript
* 3 points for documentation
* 16 points for execution?

## SPECIFICATION

``
Project 4 is the construction of the semantic analyzer. You are to include 
in your parser appropriate checking not included in the grammar, but 
defined by the language.


This is going to be the test of the quality of your symbol
table implemented during parsing. You are to determine and
implement appropriate checks as discussed.

Your project should be shar'd containing a makefile, source file,
doc file, and typescript (showing your testing). The makefile file
should be invoked with "make" creating an executable of p4. Your
project will be invoked with   p4 fn    where fn is the data file to be
checked and p4 is a script that executes your project. BE SURE TO 
PROVIDE BOTH A MAKEFILE AND A p4 EXECUTABLE SCRIPT FOR YOUR PROJECT. 
Also, be sure to test the integrity of your shar via a script (typescript)

This project must be complete in that the lexical analyzer must be
included to create the tokens required by the parser and
semantic analyzer.

Your project should report on a single line without any additional
characters

### output

Print:
``
ACCEPT

or

REJECT
``
upon completion of the analysis.

## turnin procedure

**Note that turnin will report the 2 day late date, if the project is submitted on this date a penalty will be assessed.**

* Ensure your shar is properly constructed.
* Use turnin for submission as -> **turnin fn ree4620_4** where ``fn`` is the shar'd file of your complete project.

## semantic checks

``The following represents a set of tests that might be considered. The
list is not required, nor is it complete, but may be used as a goal
for semantic analysis.``

**Note: The list of semantic checks below *IS NOT* comprehensive. The below list is just to get you started and help you think of other types of checks that may be needed**

* functions declared int or void must have a return value of the correct type.
* void functions may or may not have a return, but must not return a value.
* parameters and arguments agree in number
* parameters and arguments agree in type
* operand agreement
* operand/operator agreement
* array index agreement
* variable declaration (all variables must be declared ... scope)
* variable declaration (all variables declared once ... scope)
* void functions cannot have a return value
* each program must have one main function
* return only simple structures
* id's should not be type void
* each function should be defined (actually a linker error)