import numpy as np
from decimal import Decimal
'''
Hours studied | Hours slept  --- Test Score
2 | 9 --- 92
1 | 5 --- 86
3 | 6 --- 89
4 | 8 --- ?
'''

def input_preprocess():
		X = np.array(([2, 9], [1, 5], [3, 6]), dtype = float)
		y = np.array(([92], [86], [89]), dtype = float)
		xPredicted = np.array(([4,8]), dtype=float)

		#Scale the i/p and o/p variables
		X = X / np.amax(X, axis = 0)
		y = y / 100
		xPredicted = xPredicted / np.amax(xPredicted, axis=0) # maximum of xPredicted (our input data for the prediction)
		return X, y, xPredicted

def init_nn():
	input_size = 2
	output_size = 1
	hidden_size = 3
	wih = np.random.randn(input_size, hidden_size) # inital weights from input layer to hidden layer
	who = np.random.randn(hidden_size, output_size) # inital weights from hidden layer to output layer
	return wih, who

def sigmoid(x):
	return 1 / (1 + np.exp(-x))

def sigmoid_prime(x): #derivative of sigmoid function
	return x * (1 - x)

def feed_forward(X, wih, who):
	x_dot_wih = np.dot(X, wih)
	hiddenop = sigmoid(x_dot_wih)
	hiddenop_dot_who = np.dot(hiddenop, who)
	o = sigmoid(hiddenop_dot_who)
	return o, hiddenop

def feed_backward(X, y, finalop, hiddenop, wih, who): #backpropagation
	op_error = y - finalop #error at output layer
	op_delta = op_error * sigmoid_prime(finalop) #applying derivative of sigmoid to feedforward output

	hd_error = op_delta.dot(who.T) #error at hidden layer
	hd_delta = hd_error * sigmoid_prime(hiddenop)

	wih += X.T.dot(hd_delta)
	who += hiddenop.T.dot(op_delta)

def train(X, y, wih, who):
	final_output, hidden_output = feed_forward(X, wih, who)
	feed_backward(X, y ,final_output, hidden_output, wih, who)

def predict(xPredicted, wih, who):
	print("Predicted data based on trained weights: ")
	print("Input (scaled): \n" + str(xPredicted))
	a, b = feed_forward(xPredicted, wih, who)
	print("Output: \n" + str(a))
	 

def main():

	X, y, xPredicted = input_preprocess()
	wih, who = init_nn()
	print_list = [0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 99999]
	for i in range(100000): 
		if i in print_list: 
			print("Iteration: " + str(i))
			print("Input (Scaled): \n" + str(X))
			print("Actual Output: \n" + str(y))
			a,b = feed_forward(X, wih, who)
			print("Predicted Output: \n" + str(a))
			print("Loss: \n" + str(Decimal(np.mean(np.square(y - a))))) # mean sum squared loss
			print("\n-----------------------------------------------------------")
		train(X, y, wih, who)
	predict(xPredicted, wih, who)

if __name__ == '__main__':
	main()