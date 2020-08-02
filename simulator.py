"""
Spring Internship with Prof. Sinha
Mayank Hirani 2020
mayank.hirani@icloud.com
"""

import random

# Main simulator class
class Simulator():

	# Get the values needed, generate the sequences, insert the patterns
	def __init__(self):

		self.num_of_sequences = None

		self.patlen = None

		self.get_input()

		self.create_pattern()

		self.sequences = open('sequences.txt', 'w+')

		self.sequences_pattern = open('sequences_pattern.txt', 'w+')

		self.create_sequences()

		self.sequences.close()

		self.sequences_pattern.close()

		print(self.pattern)

	# Receive the user input for the number of sequences and the length of the pattern	
	def get_input(self):

		# Keep receiving the number of sequences until it is an integer greater than 0
		while isinstance(self.num_of_sequences, int) == False:

			self.num_of_sequences = input("Number of DNA Sequences: ")

			try:
				self.num_of_sequences = int(self.num_of_sequences)

				if self.num_of_sequences < 1:
					self.num_of_sequences = None

			except ValueError:
				pass

		# Keep receiving the length of the pattern until it is between 2 and 1000, inclusive
		while isinstance(self.patlen, int) == False:

			self.patlen = input("Length of Repeating Pattern: ")

			try:
				self.patlen = int(self.patlen)

				if self.patlen < 2 or self.patlen > 1000:
					self.patlen = None

			except ValueError:
				pass

	# Create normal sequences and sequences with patterns and write them to designated files
	def create_sequences(self):

		for sequence_counter in range(self.num_of_sequences):

			sequence = ""

			for x in range(1000):
				sequence += random.choice(['T', 'C', 'G', 'A'])

			self.sequences.write(sequence + '\n')

			sequence = self.insert_pattern(sequence)

			self.sequences_pattern.write(sequence + '\n')

	# Input a sequence and output a sequence with the pattern inserted
	def insert_pattern(self, sequence):

		# Starting index of the patter
		pat_start = random.randint(0, len(sequence) - self.patlen + 1)

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

if __name__ == '__main__':

	simulator = Simulator()











