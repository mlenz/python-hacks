#!/usr/bin/python

# usage: python letters.py valid_letters [required_letters] [min_length]
# prints a list of words composed only of valid letters, sorted by length;
# all required letters must appear, if any. Letter counts are respected.
# example: python letters.py zywwarridb wyz -> wizardry

import sys

words = open("/usr/share/dict/words", "r")
letters = sorted(sys.argv[1])
required = sorted(sys.argv[2]) if len(sys.argv) > 2 else ""
min_length = int(sys.argv[3]) if len(sys.argv) > 3 else 3
assert set(required).issubset(set(letters))
matches = []

for word in words.readlines():
	word = word.rstrip('\n').lower()
	cword = sorted(word)
	w, v, r = 0, 0, 0
	while v < len(letters) and w < len(cword):
		if letters[v] == cword[w]:
			if r < len(required) and required[r] == cword[w]:
				r = r + 1
			w = w + 1
		v = v + 1
	if w == len(cword) and len(word) >= min_length and r == len(required):
		matches.append(word)

matches.sort(key=lambda s:len(s))
for match in matches:
	print match
