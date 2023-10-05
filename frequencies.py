"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
	frequencies = {}

	for item in items:
		name = str(item)
		frequencies[name] = frequencies.get(name, 0) + 1

	return frequencies

print(frequencies([1,1,2]))
