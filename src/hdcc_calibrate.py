from subprocess import call,Popen

n = 3
zerofile = open("zerovalues.dat", 'w+')
onefile = open("onevalues.dat", 'w+')

for i in range(n):
    call(['sudo', './seeker', '/dev/sda'], stdout=zerofile)
for i in range(n):
    p1 = Popen(['sudo', './seeker', '/dev/sda'], stdout=onefile)
    call(['sudo', './seeker', '/dev/sda'], stdout=None)
    p1.wait()

zerofile.close()
onefile.close()

