"""
Spring Internship with Prof. Sinha & Shounak Bhogale (Summer part starting July 2020)
Mayank Hirani
mayank.hirani@icloud.com
"""

# Read through 100 patterns of length 8-12
# qb = 0.25 (chance of each base appearing in a position)
# Make one-hot matrices of the patterns
# Create a profile matrix
# Make a PWM for the profile matrix
# Calculate the Information Content from the PWM


import functions
from importlib import reload
reload(functions)
from functions import *


import random



class IC_Calculator():

	def __init__(self):

		# Chance of each base appearing in a position
		self.qb = 0.25

		
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

		self.matrices_dict = functions.create_one_hot_matrices('patterns.txt')

		print(self.matrices_dict)

	# Create a profile matrix from the one-hot matrix
	def create_profile_matrix(self):

		self.profile_matrix = functions.create_profile_matrix(self.matrices_dict)		

		print(self.profile_matrix)

	# Create a pwm from the profile matrix
	def create_pwm(self):

		self.pwm = functions.create_pwm(self.profile_matrix)

		print(self.pwm)
	
	# Calculate the information content of the pwm
	def calculate_ic(self):

		self.ic = functions.calculate_ic(self.pwm, self.qb)

		print(self.ic)


ic_calculator = IC_Calculator()

ic_calculator.write_patterns()
ic_calculator.create_one_hot_matrices()
ic_calculator.create_profile_matrix()
ic_calculator.create_pwm()
ic_calculator.calculate_ic()



