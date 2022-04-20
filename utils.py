from random import randrange


def randpoint(h, w):
	return randrange(0, h), randrange(0, w)


def print_bad_choice():
	print('bad choice')