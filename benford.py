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

def count_first_digits(data_list):
    #Count first digits in list of numbers; return counts & frequency.
    first_digits = defaultdict(int) #default value of int is 0
    for sample in data_list:
        if sample == '':
            continue
        try:
            int(sample)
        except ValueError as e:
            print(e, file=sys.stderr)
            print("Samples must be integers. Exiting", file=sys.stderr)
            sys.exit(1)
        first_digits[sample[0]] += 1
        #check for missing digits
        keys = [str(digit) for digit in range(1,10)]
        for key in keys:
            if key not in first_digits:
                first_digits[key] = 0
        data_count = [v for (k,v) in sorted(first_digits.items())]
        total_count = sum(data_count)
        data_pct = [(i / total_count) * 100 for i in data_count]
        return data_count, data_pct, total_count

    \