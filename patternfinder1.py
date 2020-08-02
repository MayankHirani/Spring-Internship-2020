"""
Spring Internship with Prof. Sinha
Mayank Hirani 2020
mayank.hirani@icloud.com
"""

# Method 1: Brute Force method that goes through each possible pattern of the first sequence
# and runs through all the sequences, counting the frequency of each one

# Import everything from simulator for the class
import simulator
from importlib import reload
reload(simulator)
from simulator import *

# Main pattern finder class
class PatternFinder():

	# Find all potential patterns and count frequency for each one
	def __init__(self):

		self.sequences_pattern = [x.strip() for x in open('sequences_pattern.txt')]

		self.first_sequence = self.sequences_pattern[0]

		self.possible_patterns = set()

		self.find_patterns()

		self.count_patterns()

		# Print the pattern with the highest occurence
		print(max(self.pattern_counts, key=self.pattern_counts.get))
		

	# Generate a set of all potential patterns present in the 1st sequence
	def find_patterns(self):

		for index in range(0, 1000 - simulator.patlen + 1):

			pat = self.first_sequence[ index : index + simulator.patlen ]

			self.possible_patterns.add(pat)


	# For each pattern, iterate through every character in every sequence,
	# if the same pattern is found, increase the frequency by 1
	def count_patterns(self):

		self.pattern_counts = {}

		for pattern in self.possible_patterns:

			self.pattern_counts[pattern] = 0

			for sequence in self.sequences_pattern:

				for index in range(0, 1000 - simulator.patlen + 1):

					if pattern == sequence[ index : index + simulator.patlen ]:

						self.pattern_counts[pattern] += 1
			


# Overide the simulator object from the simulator file to one here
simulator = Simulator()
patternfinder = PatternFinder()

