import statdigest
import numpy as np

# size of bins in milliseconds
precision = .04

def arbRound(num, resolution):
    return round(num / resolution) * resolution

(zerolist, onelist) = statdigest.getLists()

i = arbRound(min(zerolist), precision)-precision
max = arbRound(max(onelist), precision)+precision
bins = []
while i < max:
    bins.append(i)
    i += precision
bins.append(max)
(zerohist, _) = np.histogram(zerolist, bins)
(onehist, _) = np.histogram(onelist, bins)

outfile = open("hdcc_hist.dat", 'w+')

outfile.write("BIN\t\tZERO\tONE\n")
for i in range(1, len(bins)):
   outfile.write("%.2f-%.2f\t%d\t%d\n" %
            (bins[i-1], bins[i], zerohist[i-1], onehist[i-1]))

