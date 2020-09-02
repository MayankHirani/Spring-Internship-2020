"""
Spring Internship with Prof. Sinha & Shounak Bhogale (Summer part starting July 2020)
Mayank Hirani
mayank.hirani@icloud.com
"""

# An advanced algorithm for finding patterns, it first creates a one hot matrix,
# turns it into a profile matrix, makes that into a position weight matrix,
# and finally calculates the IC from it. This does this for every segment in every
# sequence, and the highest IC generated is saved as the found pattern.

import functions
from importlib import reload
reload(functions)
from functions import *

import random



class IC_Calculator():

	def __init__(self):

		# Chance of each base appearing in a position
		self.qb = 0.25

	# Run all functions to calculate the Information Content
	def run(self):
		
		self.create_sequences()
		# self.write_patterns()
		# self.create_one_hot_matrices()
		# self.create_profile_matrix()
		# self.create_pwm()
		# self.calculate_ic()
		# self.create_sequences()
		self.create_pairs()
		

	
	# Write the patterns to a file
	def write_patterns(self):

		self.patterns = open('patterns.txt', 'w+')
		
		for x in range(100):
			
			pattern = ''

			for y in range(10):

				pattern += random.choice(['A', 'C', 'T', 'G'])

			self.patterns.write(pattern + '\n')

		self.patterns.close()

	# Read through a file and create a dictionary with the one-hot matrices
	def create_one_hot_matrices(self):

		self.matrices_dict = functions.create_one_hot_matrices('sequences.txt')

		#print(self.matrices_dict)

	# Create a profile matrix from the one-hot matrix
	def create_profile_matrix(self):

		self.profile_matrix = functions.create_profile_matrix(self.matrices_dict)		

		#print(self.profile_matrix)

	# Create a pwm from the profile matrix
	def create_pwm(self):

		self.pwm = functions.create_pwm(self.profile_matrix)

		print(self.pwm)
	
	# Calculate the information content of the pwm
	def calculate_ic(self):

		self.ic = functions.calculate_ic(self.pwm, self.qb)

		print(self.ic)

	# Write the sequences to run the calculations
	def create_sequences(self):

		functions.create_sequences()

	# Iterate through each segment of each sequence and calculate the ic
	def create_pairs(self):

		functions.find_pattern('sequences.txt')


	
ic_calculator = IC_Calculator()

ic_calculator.run()



