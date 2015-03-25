# acpa2015
Class project for ECE 579C: Applied Cryptography and Physical Attacks

An early-stage implementation of a cloud co-location attack on Amazon AWS.

This tool requires [boto](http://docs.pythonboto.org/en/latest/getting_started.html).
We assume that you have created a file called ~/.boto in which you store your
  AWS access key.

To start an instance, import the module "instances" and then run
startOneDefaultInstance().

To get IP address information for a micro instance:
```
$ python cartography.py
```

We assume that Windows usage is possible, but we have not tried it. Sorry.

