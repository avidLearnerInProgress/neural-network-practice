#implementation of BAM
import pprint

def init_BAM(data):
	ab = []
	for ele in data:
		ab.append([generate_bipolar_form(ele[0]), generate_bipolar_form(ele[1])])

	x_length = len(ab[0][1])
	y_length = len(ab[0][0])

	_bam = [] #initialise empty bam array
	temp = []
	for ele in range(y_length):
		temp = [0] * x_length
		_bam.append(temp)

	return ab, x_length, y_length, _bam

def create_BAM(ab, _bam):
	for ele in ab:
		X = ele[0]
		Y = ele[1]
		for ix, xi in enumerate(X):
			for iy, yi in enumerate(Y):
				_bam[ix][iy] += xi * yi
	return _bam

def get_associations(A, _bam, x_length, y_length):
	A = multiply_vec(A, _bam, x_length, y_length)
	return threshold(A)

def multiply_vec(vec, _bam, x_length, y_length):
	result = [0] * x_length
	for x in range(x_length):
		for y in range(y_length):
			result[x] += vec[y] * _bam[y][x]
	return result

def generate_bipolar_form(vec):
	result = []
	for ele in vec:
		if ele == 0:
			result.append(-1)
		else:
			result.append(1)
	return result

def threshold(vec):
	result = []
	for ele in vec:
		if ele < 0:
			result.append(0)
		else:
			result.append(1)
	return result


def main():
	A = [[1, 0, 1, 0, 1, 0], [1, 1, 0, 0]]
	B = [[1, 1, 1, 0, 0, 0], [1, 0, 1, 0]]

	data_associations = [A, B]
	ab, x_length, y_length, bam = init_BAM(data_associations)
	bam_matrix = create_BAM(ab, bam)
	pp = pprint.PrettyPrinter(indent = 4)
	print("Bam Matrix: ")
	pp.pprint(bam_matrix)
	print("\n")
	print("[1, 0, 1, 0, 1, 0] :- ", get_associations([1, 0, 1, 0, 1, 0], bam_matrix, x_length, y_length))
	print("\n")
	print("[1, 1, 1, 0, 0, 0] :- ", get_associations([1, 1, 1, 0, 0, 0], bam_matrix, x_length, y_length))

if __name__ == '__main__':
	main()