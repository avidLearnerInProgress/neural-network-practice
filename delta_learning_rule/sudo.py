# -*- coding: utf-8 -*-
"""
@author: chirag
"""

import numpy as np
import time, math

def threshold(x):
	return round(((2 / (1 + math.exp(-x))) - 1), 3)

def print_func(loop_var, net, sig_net, sig_dash_net, teacher_signal, w, delta_w = None):
		print("i: "+ str(loop_var))
		print("net: "+ str(net))
		print("sig_net: "+ str(sig_net))
		print("sig_dash_net: "+ str(sig_dash_net))
		print("delta_w: "+ str(delta_w))
		print("teacher_signal: "+ str(teacher_signal))
		print("w: "+ str(w))
		print("-------------------\n")


def compute():
		
	try:
		n = int(input("Enter number of input vectors: "))

		x = []
		r = 0.1 #Learning rate

		for i in range(0,n):
			raw_str1 = str(input("Enter values for vector " + str(i+1) + ": "))
			input_vector = raw_str1.split(' ')
			#print(input_vector)
			ip_list = []
			for ele in input_vector:
				ip_list.append(float(ele))
			#print(ip_list)
			np_list = np.array(ip_list, dtype=np.float64)
			x.append(np_list)

		raw_str2 = str(input("Enter values for teacher signal: "))
		teacher_signal = raw_str2.split(' ')
		teacher_signal = [int(x) for x in teacher_signal]
		if len(teacher_signal) != n:
			print("Teacher Signal length Error..")
			time.sleep(3)
			exit()


		raw_str3 = str(input("Enter initial weight vector: "))
		w = raw_str3.split(' ')
		w_list = []
		for ele in w:
			w_list.append(round(float(ele), 3))
		np_wlist = np.array(w_list, dtype=np.float64)
		#print(np_wlist)

		delta_w = 0
		for i in range(0,n):
			
			net = round(np.transpose(np.asarray(w_list)).dot(np.asarray(x[i])), 3)
			#print(net)
			sig_net = threshold(net)
			sig_dash_net = round(0.5 * ( 1 - ((sig_net)**2)), 3)
			print(sig_dash_net)

			if sig_net != teacher_signal[i]:
				
				rounded_delta_w = []
				rounded_w_list = []

				delta_w = (r * (teacher_signal[i] - sig_net) * sig_dash_net * x[i])

				for ele in delta_w:
					rounded_delta_w.append(round(ele, 3))
				#print(delta_w)

				w_list = np.add(np.asarray(w_list), rounded_delta_w)
				for ele in w_list:
					rounded_w_list.append(round(ele, 3))
				w_list = rounded_w_list

			else:
				rounded_w_list = []
				for ele in w_list:
					rounded_w_list.append(round(ele, 3))
				w_list = rounded_w_list

			print_func(i, net, sig_net, sig_dash_net, teacher_signal[i], w_list, rounded_delta_w)
			
	except Exception as e:
		print("Error.. "+(str(e)))




if __name__ == '__main__':
	compute()