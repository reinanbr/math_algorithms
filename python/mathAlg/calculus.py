# ReinanBr 22:43 18.02.23
# CalculusAlgorithm

import sys

dx = sys.float_info.epsilon


class Calculus:

	def __init__(self,func):
		self.func = func

	def derivative(self,x,dx=dx):
		df = self.func(x+dx)-self.func(x)
		return df/dx

	def integrate(self,space:tuple,N=2000):
		b,a = space
		ab = a-b
		dx = ab/N
		f = self.func(b)
		for i in range(int(N)):
			f += i*self.func(b+dx)*dx
		return f


