# pyGP

PyGP is a genetic programming library for Python 3, written primarily for symbolic regression applications and based on the genetic programming principles outlined in A Field Guide to Genetic Programming by Poli, Langdon, and McPhee. It contains classes and functions for implementing a basic genetic programming implementation, a demo module demonstrating a GP run, and a command-line GP module for symbolic regression via the CLI.

####Library Contents

The pyGP library contains four modules for user use. The main pygp module contains the classes and functions needed for a simple GP program. The primitives module contains a preset primitive set for use in programs. The majorelements module contains functions which serve as larger components of a GP program, such as population initialization and an evolution loop. Lastly, the tools module contains functions which can be used at the top level to handle data for the user.

The demo directory contains the demo module, which demonstrates a run of GP and is liberally commented to explain the basics of a run. The directory also contains .csv files of sample data, which the demo module can use to find a solution function that matches the data they contain.

The cli-gp directory contains a symbolic regression program module which accepts user-defined control parameters of the GP run and displays its progress via the command line.

Finally, the tests directory contains various scripts for testing components of the library.
