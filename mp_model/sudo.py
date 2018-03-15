# -*- coding: utf-8 -*-
"""
@author: chirag
"""
def threshold(x):
	if x >= 0:
		return 1
	else:
		return 0

def mcp_neuron(w, b, i):

	inputs = i
	weights = w
	bias = b

	def activate():
		_sum = 0
		for x,y in zip(inputs, weights):
			_sum += (x*y)
		print("Sum: "+str(_sum))
		return threshold(_sum + bias)

	return activate()


def main():

	try:
		n = int(input("Total neurons to test: "))
		for i in range(0, n):
			
			raw_str1 = str(input("Enter input parameters: "))
			input_params = raw_str1.split(' ')
			input_params = [int(x) for x in input_params]

			raw_str2 = str(input("Enter input weights: "))
			input_weights = raw_str2.split(' ')
			input_weights = [float(x) for x in input_weights]

			input_bias = float(input("Enter bias: "))

			#print(input_weights)
			#print(input_params)
			#print(input_bias)

			print("Result after thresholding: "+str(mcp_neuron(input_weights, input_bias, input_params)))
			print("--------------------")

	except Exception as e:
		print("Error..\n"+ str(e))


if __name__ == '__main__':
	main()


'''
Test:
[1 0 1]
([0.2, 0.7, 0.3], -1.5)
([0.4, 0.6, 0.9], -0.8)
([0.7, 0.4, -0.9], -0.6)
'''