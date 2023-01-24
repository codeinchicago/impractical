import sys
import math
from collections import defaultdict
import matplotlib.pyplot as plt

#Benford's law percentages for leading digits 1-9
BENFORD = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]

def load_data(filename):
    '''Open a text file & return a list of strings.'''
    with open(filename) as f:
        return f.read().strip().split('\n')