from mathAlg import Calculus

def p(x):
	return x

cp = Calculus(p)

print(cp.derivative(7))
print(cp.integrate((0,2)))
