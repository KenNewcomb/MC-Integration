import parser
import random
import sys 

def integrator(eq, a, b, num):
	equation = parser.expr(eq).compile()

	sum = 0
	for step in range(0, num):
		x = random.uniform(a,b)
		sum += float(eval(equation))
	
	average = float((b-a)*sum/num)
	print("Integral approxmiation: " + str(average))

eq = sys.argv[1]
a = int(sys.argv[2])
b = int(sys.argv[3])
num = int(sys.argv[4])

integrator(eq, a, b, num)
