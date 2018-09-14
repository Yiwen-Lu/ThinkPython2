# Exercise 2.2.1
import math

def volume(r):
	return 4/3 * math.pi * r**3

if __name__ == "__main__":
    radius = 5
    print("the volume of a sphere with radius 5 is %d" % volume(radius))
