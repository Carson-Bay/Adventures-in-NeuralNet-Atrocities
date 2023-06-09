import numpy as np


class Model:
    def __init__(self):
        self._input_size = 0
        self._hidden_sizes = list()
        self._output_size = 0
        self.weights = []
        self.biases = []
        self.transfer_function = None

    def set_input_size(self, size:int):
        self._input_size = size
        return self

    def add_hidden_layer(self, size:int):
        self._hidden_sizes.append(size)
        return self

    def set_output_size(self, size:int):
        self._output_size = size
        return self

    def set_transfer_function(self, func):
        self.transfer_function = func
        return self

    def build_model(self): 
        # Initialize weights
        previous_size = self._input_size
        for i in self._hidden_sizes:
            self.weights.append(np.random.uniform(-0.5, 0.5, (i, previous_size)))
            self.biases.append(np.zeros((i, 1)))
            previous_size = i
        
        self.weights.append(np.random.uniform(-0.5, 0.5, (self._output_size, previous_size)))
        self.biases.append(np.zeros((self._output_size, 1)))
        return self

    def evaluate(self, input_data):
        # Basic feedforward network
        # TODO: create process for multiple transfer functions or specific output functions

        if self.transfer_function == None:
            return

        intermediate = input_data
        for i in range(len(self.weights)):
            intermediate = self.transfer_function(self.biases[i] + self.weights[i] @ input_data)
        return intermediate

