import random

def Generation():
	ascii = [chr(x) for x in range(65,91)] + [chr(x) for x in range(97,123)] + [chr(x) for x in range(48,58)]
	password = ""
	for o in range(random.randint(8,14)):
		password += random.choice(ascii)
	return password
Generation()