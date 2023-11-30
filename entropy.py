import numpy as np
from math import log, e

def entropy(probabilities, base):
  ent = 0.

  # Compute entropy
  base = e if base is None else base
  for i in probabilities:
    ent -= i * log(i, base)

  return ent

def entropy_of_text(labels, base=None):
  """ Computes entropy of label distribution. """

  n_labels = len(labels)

  if n_labels <= 1:
    return 0

  value,counts = np.unique(labels, return_counts=True)
  probs = counts / n_labels
  n_classes = np.count_nonzero(probs)

  if n_classes <= 1:
    return 0
  return entropy(probs, base)