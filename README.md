# Sudoku

An early-stage Python Sudoku project that aims to read hand-drawn digits with a machine-learning classifier.

## Overview

The idea is a Sudoku board where you write digits by hand and a trained model recognises them. The repository holds the first two building blocks, as separate scripts that are not yet connected:

- [`character_classifier.py`](character_classifier.py) trains and evaluates a handwritten-digit classifier.
- [`sudoku_viewer.py`](sudoku_viewer.py) opens a Tkinter drawing canvas, the start of the game's user interface.

There is no Sudoku logic yet (no puzzle generation, board validation or solver).

## Machine learning

`character_classifier.py`:

- **Model**: scikit-learn's `MLPClassifier` (a multi-layer perceptron neural network) with default settings, wrapped in a small `CharacterClassifier` class with `train` and `predict` methods.
- **Dataset**: scikit-learn's built-in digits dataset (`sklearn.datasets.load_digits`): 1,797 8 x 8 greyscale images of the digits 0 to 9. This is not MNIST.
- **Evaluation**: the samples are shuffled and split 50/50 into training and test sets. The script trains on the first half and prints the accuracy on the second. Because the shuffle is unseeded, the figure varies a little between runs.
- **Trained model**: none is included. The model is retrained in memory on every run and not saved.

## Drawing canvas

`sudoku_viewer.py` opens a 640 x 640 white canvas. Hold the left mouse button and drag to draw. When you release the button, the drawing is cleared and replaced by a random digit from 0 to 9.

The random digit is a placeholder for the classifier's prediction: the viewer does not yet import or call the classifier.

## Tech stack

- Python 3
- scikit-learn (`MLPClassifier` and the digits dataset)
- NumPy and Matplotlib, imported by the classifier script (Matplotlib is not used yet)
- Tkinter, from the Python standard library, for the canvas

## Getting started

### Prerequisites

- Python 3 with Tkinter (included in most Python installations; some Linux distributions package it separately, for example as `python3-tk`)

The repository has no `requirements.txt`. Install the classifier's dependencies directly:

```bash
pip install scikit-learn numpy matplotlib
```

### Run

Train the classifier and print its test accuracy:

```bash
python character_classifier.py
```

Open the drawing canvas:

```bash
python sudoku_viewer.py
```

## Project structure

```
character_classifier.py   # MLP digit classifier trained and tested on scikit-learn's digits dataset
sudoku_viewer.py          # Tkinter drawing canvas, the start of the game UI
```

## Status

This is a first commit from 2018 and the project is incomplete:

- The classifier and the canvas are not connected.
- The viewer is meant to create a 9 x 9 grid of cells, but `[SudokuCell(self.root)] * 81` builds one cell and repeats the reference, so only a single canvas appears.
- The classifier is trained on 8 x 8 images, while the canvas is 640 x 640, so drawings would need downscaling before the model could classify them.
