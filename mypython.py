from random import choice, randint
from string import ascii_lowercase

#function to make a random string and also write it to a file
def scribe(target):
	file = open(target, "w")
	content = "".join([choice(ascii_lowercase) for i in range(10)])
	print(content)
	file.write(content + "\n")
	file.close()

#writing three files
scribe("THOR")
scribe("PERUN")
scribe("ZEUS")

#getting some random ints and finding the product
x = randint(1,42)
y = randint(1,42)
z = x*y
print(str(x) + "\n" + str(y) + "\n" + str(z))

