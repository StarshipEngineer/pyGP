# pyGP

PyGP is a genetic programming library for Python 3, written primarily for symbolic regression applications and based on the genetic programming principles outlined in A Field Guide to Genetic Programming by Poli, Langdon, and McPhee. It contains classes and functions for implementing a basic genetic programming implementation, a demo module demonstrating a GP run, and a command-line GP module for symbolic regression via the CLI. The latter two modules are scripts that can be executed from within their home directories by system shell commands, command-line Python, or a Python IDE.

####Library Contents

The pyGP library contains four modules for user use. The main pygp module contains the classes and functions needed for a simple GP program. The primitives module contains a preset primitive set for use in programs. The majorelements module contains functions which serve as larger components of a GP program, such as population initialization and an evolution loop. Lastly, the tools module contains functions which can be used at the top level to handle data for the user.

The demo directory contains the demo module, which demonstrates a run of GP and is liberally commented to explain the basics of a run. The directory also contains .csv files of sample data, which the demo module can use to find a solution function that matches the data they contain.

The cli-gp directory contains a symbolic regression program module which accepts user-defined control parameters of the GP run and displays its progress via the command line.

Finally, the tests directory contains various scripts for testing components of the library.

####Library Capabilities

At present, the function set of the library and demo/cli-gp programs encompasses Python's five built-in arity-2 mathematical operators, the four arithmetic operators addition ( + ), subtraction ( - ), multiplication( * ), and division ( / ), plus the exponentiation operator ( ** ). The terminal set includes the constants pi, e, and random constants in the range [0.0,1.0), plus whatever independent variables are entered by the user (which correspond to columns in a dataset). The provided programs compose polynomial and exponential solutions to provided datasets. A run may return an exact solution if the solution can be represented this way, but in general this cannot be guaranteed, and a run will return the closest possible approximate solution which can be constructed using arithmetic and exponential operations.

####General Use of GP Programs

The intended function of the demo and cli-gp programs is to construct the best possible solution to a set of numeric data. These programs are run as scripts from within their enclosing directories, and accept this data in the form of a .csv file located in the same directory; for n independent variables, this file must have n+1 columns of values, one column for each dependent variable and a column for dependent variable values, which must be the rightmost column. Each row should have a value for each of the problem's independent variables, and a value of the dependent variable corresponding to those independent variable values.

The user will enter a name for each of the independent variables, either in the command line when running cli-gp or into the module file as a string when running demo. There are no particular restrictions on the names of these variables, but they must be entered in the same left-to-right order as their corresponding columns in the .csv file- otherwise a run may return a solution expression where some of the variable names are transposed. The user will also enter values for the various parameters of the GP run. Once engaged, the run will proceed to evolve solutions and when one with a fitness below the target fitness is found, it will be returned and the run will be terminated.

For a more in-depth explanation of the steps in a GP run, see the annotated demo module. For even more in-depth explanations, see A Field Guide to Genetic Programming by Poli, Langdon, and McPhee, which can be found free in PDF form from the authors' website [here](http://www0.cs.ucl.ac.uk/staff/W.Langdon/ftp/papers/poli08_fieldguide.pdf).

####Note
This library is being developed as a personal project for educational purposes (mine and yours). Not everything may function as intended or expected, and this library should not be used for any mission-critical roles or applications where accurate results are essential (like your homework or spaceship navigation).
