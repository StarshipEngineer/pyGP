# Import modules
import pygp

# Define the function and terminal sets
functions = []
terminals = []
primitives = functions + terminals

# Import your data to fit
filename = "datafile.csv"
data = pygp.dataread(filename)

# Construct an initial population

# Select inidividuals from the population, test their fitness,
# and use them to populate the next generation

