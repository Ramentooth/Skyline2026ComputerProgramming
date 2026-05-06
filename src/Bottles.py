#!/usr/bin/python3

Bottles = 99
for bottles in range(99,0,-1):
	print(bottles, "bottles of water on the wall", bottles, "bottles of water")
	bottles = bottles -1
	print("take one down and pass it around,", bottles, "bottles of water on the wall.")

