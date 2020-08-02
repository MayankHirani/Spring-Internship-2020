"""
Spring Internship with Prof. Sinha
Mayank Hirani 2020
mayank.hirani@icloud.com
"""

# Method 2: Brute force method that goes through all the sequences, and keeps track of
# every possible pattern in one large dictionary

# Import everything from simulator for the class
import simulator
from importlib import reload
reload(simulator)
from simulator import *

# Main pattern finder class
class PatternFinder2():

	# Make a dictionary of frequencies and return the largest one
	def __init__(self):

		self.sequences_pattern = [x.strip() for x in open('sequences_pattern.txt')]

		self.pattern_counts = {}

		self.run()

		# Print the pattern with the highest occurence
		print(max(self.pattern_counts, key=self.pattern_counts.get))
		

	# Generate a dictionary of the frequency of all potential patterns present
	# in all the sequences
	def run(self):

		for sequence in self.sequences_pattern:

			for index in range(0, 1000 - simulator.patlen + 1):

				pat = sequence[ index : index + simulator.patlen ]

				if pat in self.pattern_counts:

					self.pattern_counts[pat] += 1

				else:

					self.pattern_counts[pat] = 1


			


# Overide the simulator object from the simulator file to one here
simulator = Simulator()
patternfinder2 = PatternFinder2()

