import parser
import random
import sys 

def integrator(eq, a, b, num):
	"""Approximates the integral of a given function"""

	# Parse algebraic expression
	equation = parser.expr(eq).compile()

	sum = 0
	sample_list = []
	for step in range(0, num):
		# Sample the function within the given bounds, randomly.
		x = random.uniform(a,b)
		sum += float(eval(equation))
		sample_list.append(str(x))

	# Calculate the average value of the function.
	average = float((b-a)*sum/num)
	print("Integral approximation: " + str(average))
	return sample_list
# Check for appropriate number of input arguments.
if len(sys.argv) is not 5:
	print("Usage: python3 mc-integration.py f(x) lower_bound upper_bound number_of_points")
	sys.exit(0)

# Input arguments
eq = sys.argv[1]
a = int(sys.argv[2])
b = int(sys.argv[3])
num = int(sys.argv[4])

sample_list = integrator(eq, a, b, num)
sample_file = open('samples', 'w')

for sample in sample_list:
	sample_file.write(sample + "\n")
sample_file.close()
