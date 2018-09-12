import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.neural_network import MLPClassifier
import random

"""
Builds a model to classify hand-written digits into their
numerical representation. Trained using a neural network.
"""
class CharacterClassifier:
	def __init__(self):
		self.clf = MLPClassifier()
	def train(self, data_f, data_t):
		self.clf.fit(data_f, data_t)
	def predict(self, data):
		return self.clf.predict(data)

digits = datasets.load_digits()
digits_data = digits['data']
digits_target = digits['target']

data = [(digits_data[i], digits_target[i]) for i in range(len(digits_data))]
random.shuffle(data)

training = data[:len(data)//2]
training_features = [f for (f, t) in training]
training_targets = [t for (f, t) in training]

test = data[len(data)//2::]
test_features = [f for (f, t) in test]
test_targets = [t for (f, t) in test]

c = CharacterClassifier()
c.train(training_features, training_targets)
print(sum(c.predict(test_features) == test_targets) / len(test_features))