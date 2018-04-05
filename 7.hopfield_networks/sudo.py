import matplotlib.pyplot as plt
import numpy as np

def get_symmetric_matrix(size): 
    result = np.random.randn(size, size) #initialise matrix with random values
    result = result - np.diag(np.diag(result)) #Extract diagonal from result matrix
    result = (result + result.T) / 2 
    return result

class HopfieldNetwork:
    def __init__(self, neurons):
        self.neurons = neurons
        self.states = np.random.choice((+1, -1), size=(self.neurons)) #generates random sample of size neurons(100) between 1 and -1 
        self.weights = get_symmetric_matrix(self.neurons)
        self.biases = np.random.randn(self.neurons)

    def update(self):
        i = np.random.randint(self.neurons)
        if np.dot(self.weights[i], self.states) + self.biases[i] >= 0:
            self.states[i] = +1
        else:
            self.states[i] = -1

    def get_energy(self):
        energy = 0
        for i in range(self.neurons):
            for j in range(self.neurons):
                energy -= 0.5 * self.weights[i][j] * self.states[i] * self.states[j]
            energy -= self.biases[i] * self.states[i]
        return energy

    def is_minimum(self):
        for i in range(self.neurons):
            if np.dot(self.weights[i], self.states) + self.biases[i] >= 0:
                if self.states[i] == -1:
                    return False
            else:
                if self.states[i] == +1:
                    return False
        return True

def main():
    neurons = 100
    hopfield_network = HopfieldNetwork(neurons)
    energy = [hopfield_network.get_energy()]
    while not hopfield_network.is_minimum():
        hopfield_network.update()
        energy.append(hopfield_network.get_energy())
    plt.plot(energy)
    plt.show()

if __name__ == '__main__':
    main()