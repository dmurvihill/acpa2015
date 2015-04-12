import statdigest
import numpy as np

# size of bins in milliseconds
precision = .2

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

zerofile = open("zerohist.dat", "w+")
onefile = open("onehist.dat", "w+")

for (hist, file) in zip([zerohist, onehist],[zerofile, onefile]):
    file.write("BIN\tCOUNT\n")
    for i in range(1, len(bins)):
       file.write("%.1f-%.1f\t%d\n" % (bins[i-1], bins[i], hist[i-1]))

