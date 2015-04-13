from statistics import mean, stdev
import numpy as np

def getLists():
    return (
            np.fromfile(open("zerovalues.dat", 'r'), sep='\n'),
            np.fromfile(open("onevalues.dat", 'r'), sep='\n'))

def compute_stats(list):
    return (mean(list), min(list), max(list), stdev(list))

print("MEAN\tMIN\tMAX\tSTDEV")
for l in getLists():
    print("%.2f\t%.2f\t%.2f\t%.2f" % compute_stats(l))

