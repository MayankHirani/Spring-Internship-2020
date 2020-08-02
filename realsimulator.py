"""
Spring Internship with Prof. Sinha
Mayank Hirani 2020
mayank.hirani@icloud.com
"""

# Import everything from simulator for the class
import simulator
from importlib import reload
reload(simulator)
from simulator import *

# Import random for probabilities
import random

# Import matplotlib for graphing
import matplotlib.pyplot as plt

# Import pandas dataframe for plotting heatmap
from pandas import DataFrame

# Import numpy for making DataFrame
import numpy as np

# Main simulator class
class RealSimulator():

	# Get the values needed, generate the sequences, insert the patterns
	def __init__(self):

		# ----- Stats -----
		# Chance of pattern appearing in a sequence
		self.p = 1
		# Chance for error in pattern
		self.e = 0
		# Number of sequences
		self.num_of_sequences = 100
		# Length of Pattern
		self.patlen = 10

		# ----- Data ------
		# This will be dictionary of accuracy
		self.p_data = {}
		self.e_data = {}

		self.vary_stats()

		print('P Results:', self.p_data)
		print('E Results:', self.e_data)

		# ----- Data Plotting -----
		self.plot_data(self.p_data, 'P Data')
		self.plot_data(self.e_data, 'E Data') 

	# General run, create pattern, create sequences, insert pattern
	def run(self):

		self.create_pattern()

		self.sequences_pattern = 'sequences_pattern.txt'

		self.create_sequences()

		return self.determine_accuracy(self.run_pattern_finder())

	# Specific run, for each stat it will be varied and use the run() command
	def vary_stats(self):

		# Number of times run for each variable
		num = 1

		# For whatever variable is being tested, a list of all successful/unsuccessful runs
		self.general_data = []
		'''
		# P
		for p in range(0, 101): # Default (90, 101)

			self.general_data = []

			self.p = p / 100

			# How many times you want to run with same stat value
			for x in range(num):

				self.general_data.append(self.run())

			self.p_data[self.p] = self.general_data.count(1)

		self.p = 1	# Reset value for p to default (1)
		
		# E
		for e in range(0, 101): # Default (10, 61)

			self.general_data = []

			self.e = e / 100

			for x in range(num):

				self.general_data.append(self.run())

			self.e_data[self.e] = self.general_data.count(1)

		self.e = 0	# Reset value for e to default (0)
		'''
		
		# Pattern Length
		# Removed because the pattern length does not affect the accuracy (except for values 1-6)
		
		# Number of Sequences
		# Removed because the number of sequences does not affect the accuracy (except for values 1-10)
		
		
		# Varying two variables (p and e) at once and recording data in heat map
		self.plot_heatmap(num)


	# Create normal sequences and sequences with patterns and write them to designated files
	def create_sequences(self):

		f = open(self.sequences_pattern, 'w+')

		for sequence_counter in range(self.num_of_sequences):

			sequence = ""

			for x in range(1000):
				sequence += random.choice(['T', 'C', 'G', 'A'])

			# Only insert for chance p
			prob = random.random()
			if prob <= self.p:
				sequence = self.insert_pattern(sequence)

			f.write(sequence + '\n')

		f.close()

	# Input a sequence and output a sequence with the pattern inserted
	def insert_pattern(self, sequence):

		# Starting index of the patter
		pat_start = random.randint(0, len(sequence) - self.patlen + 1)

		# With chance e, alter the pattern
		prob = random.random()
		if prob < self.e:

			sequence = sequence[0:pat_start] + self.alter_pattern() + sequence[pat_start+self.patlen:]
		
		else:
			# Before pattern + Pattern + Ending part
			sequence = sequence[0:pat_start] + self.pattern + sequence[pat_start+self.patlen:]

		return sequence

	# Function to create the pattern
	def create_pattern(self):

		self.pattern = ''

		for x in range(self.patlen):

			self.pattern += random.choice(['T', 'C', 'G', 'A'])

		self.pattern_file = open('pattern.txt', 'w+')

		self.pattern_file.write(self.pattern)

		self.pattern_file.close()

	# Used to alter the pattern by 1 letter for chance e
	def alter_pattern(self):

		altered_pattern = list(self.pattern)

		index = random.randint(0, self.patlen - 1)

		# Choose a random letter that is not its own
		letter = self.pattern[index]
		while letter == self.pattern[index]:
			letter = random.choice(['T', 'C', 'G', 'A'])

		altered_pattern[index] = letter
		altered_pattern = ''.join(altered_pattern)

		return altered_pattern

	# Determine the accuracy by comparing the pattern found to right pattern (exact match)
	def determine_accuracy(self, pattern_found):

		if pattern_found == self.pattern:

			return 1

		else:

			return 0











	# -----------------------------------------------------------------------------
	# Pattern Finder Section

		

	# Generate a dictionary of the frequency of all potential patterns present
	# in all the sequences
	def run_pattern_finder(self):

		self.pattern_counts = {}

		for sequence in open(self.sequences_pattern):

			for index in range(0, 1000 - self.patlen + 1):

				pat = sequence[ index : index + self.patlen ]

				if pat in self.pattern_counts:

					self.pattern_counts[pat] += 1

				else:

					self.pattern_counts[pat] = 1

		return max(self.pattern_counts, key=self.pattern_counts.get)











	# -----------------------------------------------------------------------------
	# Plotting Section



	# Function for plotting the data from dictionary form

	def plot_data(self, data, type):

		# Convert the dictionary to usable form
		lists = sorted(data.items())
		x, y = zip(*lists)

		# Plot the data
		plt.plot(x, y)

		plt.xlabel(type)
		plt.ylabel('Accuracy out of 100')
		plt.show()

	# Function for plotting the data into a heatmap
	def plot_heatmap(self, num):

		# Each row is a value of p, each column is a value of e
		rows = []; col = []

		self.heatmap_data = np.zeros((101, 101))

		for indexp, p in enumerate(range(0, 101, 1)):

			self.p = p / 100
			
			# Add the values for the x axis labels and y axis labels
			rows.append(str(self.p))
			col.append(str(self.p))

			for indexe, e in enumerate(range(0, 101, 1)):

				self.e = e / 100

				print(self.p, self.e)

				self.general_data = []

				for x in range(num):

					self.general_data.append(self.run())

				self.heatmap_data[indexp][indexe] = self.general_data.count(1)

		# Create a DataFrame of the results
		self.heatmap_data = DataFrame(self.heatmap_data, index=rows, columns=col)

		# Plot the DataFrame as a heatmap
		plt.pcolor(self.heatmap_data)

		# Set intervals for x and y axis
		plt.yticks(np.arange(0.5, len(self.heatmap_data.index), 1), self.heatmap_data.index)
		plt.xticks(np.arange(0.5, len(self.heatmap_data.columns), 1), self.heatmap_data.columns, rotation=90)

		# Set labels
		plt.xlabel('E Value')
		plt.ylabel('P Value')

		# The colorbar on the side showing what colors mean what
		colorbar = plt.colorbar()
		colorbar.ax.set_ylabel('Accuracy out of ' + str(num))

		# Save the plot file as PNG type
		plt.savefig('heatmap')

		# Final Plot
		plt.show()

		



if __name__ == '__main__':

	simulator = RealSimulator()

