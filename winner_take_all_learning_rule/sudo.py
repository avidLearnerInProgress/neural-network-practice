import numpy as np

def print_func(weight_vector_list, sum_arr, max_ele, location, loop_var):
		print("i: "+ str(loop_var))
		print("Summation array: ")
		print(sum_arr)
		print("Winner element: "+ str(max_ele))
		print("Location of winner element: "+ str(location))
		print("Weight vectors are: ")
		print(weight_vector_list)
		print("-------------------\n")


def compute():
		
	try:
		n = int(input("Enter dimension of input vector: "))
		input_vector,input_list = [],[]
		alpha = 1 #Learning constant(c)
		raw_str = str(input("Enter elements of input vector: "))
		input_vector = raw_str.split(' ')
		for ele in input_vector:
			input_list.append(float(ele))
		#print(input_list)

		p = int(input("Enter number of neuron units: "))
		weight_vector_list = []
		print("Enter weights for each input to neuron units:")
		for i in range(0,p):
			w = []
			weight_raw_str = str(input("Weights for input " + str(i+1) + ": "))
			weight_input_vector = weight_raw_str.split(' ')
			for ele in weight_input_vector:
				w.append(float(ele))
			weight_vector_list.append(w)
		print("Initial Weight Vector List:")
		print(weight_vector_list)

		for iterate in range(0,n):
			result = []
			for ele in weight_vector_list:
				net = np.transpose(np.asarray(ele)).dot(np.asarray(input_list))
				result.append(net)
			winner_arr=np.array(result)
			#print(winner_arr)
			#print(max(winner_arr))
			location=np.argmax(winner_arr) #location of max ele in result
			#print(location)

			for i in range(0,n):
				update = alpha*(input_list[i] - weight_vector_list[location][i])
				print("Update value: "+ str(update))
				weight_vector_list[location][i] += update
			#print(weight_vector_list)
			print_func(weight_vector_list, winner_arr, max(winner_arr), location, iterate)
			
	except Exception as e:
		print("Error.. "+(str(e)))

if __name__ == '__main__':
	compute()