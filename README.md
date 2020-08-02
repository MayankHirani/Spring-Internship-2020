
Spring Internship with Prof. Sinha and Shounak Bhogale (Starting Feb 2020)
Mayank Hirani
mayank.hirani@icloud.com





Things to do by next week
(Written July 29)
• Reformat the PWM so it is same as profile matrix and calculate information content
• Read the sequences --> Make one-hot matrixes of them --> Create profile matrix --> Make PWM from profile matrix --> Calculate Information content
• 100 Sequences of length 100, pattern length = 10, 0-3 errors --> write sequences in file --> read sequences --> Calculate best information content from the 2 sequences
• Deal with zeros from Wbk


Algorithm:

• Sites where proteins interact with DNA
• DNA mismatches allow for proteins to interact with the DNA
• Score for mismatches shows how mismatched a pattern is
• Goal is to find the motiff/pattern
• 2D matrix with weights on each character (PWM Position Weight Matrix)
Pattern Indexes:        _ _ _ _ _ _
Character Probability
T                       x y z a b c
C                       . . . . . .
G            			. . . . . .
A 						. . . . . .
each value in the matrix is the probability that the index of the pattern is that corresponding character

Position Weight Matrix
• With all the possible patterns, there is a matrix created, the profile matrix

			A C T G C A
			A T T G C A
pattern	   	A C T G C G
			A C G T C G
				\/
		A   4 0 0 0 0 2
profile	C   0 3 0 0 4 0
matrix	T   0 1 3 1 0 0
		G   0 0 1 3 0 2
				\/
consensus	A C T G C N


• One-hot matrix: For each position in a sequence, a list can be made, with the positions indicating T, C, G, or A.
this way, letters do not have to be used, only numbers, and they can be easily worked with.

					C A G

[ [ 0, 1, 0, 0 ], [ 1, 0, 0, 0 ], [ 0, 0, 0, 1] ]

Using: [ A, C, T, G ]

Information Content

From the position weight matrix, the probabilities from the frequencies that determine the probability of each character at each position

Wbk = Probability that base b is at a position k
qb = probability of base b normally appearing in the sequence (theoretically 0.25)
Information Content: A constant that determines the goodness of the PWM for the pattern





------------ OLD ------------


Steps to a Pattern Finder in DNA sequences

1. Make a data set of a variable number of data sequences, each 1000 characters in length. In each sequence, insert a special string pattern of variable length.

2. Create a program that find the pattern that is repeating in each sequence.

3. Compare the pattern found to the pattern planted to confirm that the program works.





Realistic Simulator

• Pattern may only be present in p% of sequences
• Pattern may contain one error (random character changed not original character)
• e% of error when planting
• Generate data on different p and e values
• [Important] Accuracy of results based on parameters tested on 100 times --> vary one parameter at a time, and calculate resulting accuracy
• Measure timing on 4 separate plots
• Compare accuracy between both existing methods

pat_len = 8
p = 80%
e = 20%
seq_num = 100

x - axis : variation in parameter
y - axis : either accuracy or timing




Old Tasks (Written June 10)
• Wrap up and make comments
• Write a report on everything we did (Introduction --> Methods (Explain algorithms) --> Results --> Discussion)
• Over summer (after June 12th), start working on more advanced topics with motiffs
• Think about modifying patternfinder to account for error, measure accuracy

