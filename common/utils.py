import pickle 
import numpy as np

def store_data(filename, input_data, output_data):
    with open(filename, "wb") as fout:
        pickle.dump(input_data, fout)
        pickle.dump(output_data, fout)

def load_data(filename):
    with open(filename, "rb") as fout:
        input_data = pickle.load(fout)
        output_data = pickle.load(fout)
        return input_data, output_data

# Send args in as weights then biases from input to output
def store_model(filename, *args):
    with open(filename, "wb") as fout:
        for i in args:
            pickle.dump(i, fout)

def load_model(filename, layers):
    output = []
    with open(filename, "rb") as fin:
        for i in range(2*(layers-1)):
            output.append(pickle.load(fin))
    return output
