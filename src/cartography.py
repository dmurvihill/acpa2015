import boto
import boto.ec2 as ec2
import instances

instance = instances.start_instance()
print("Type:",instance.instance_type,"\t\tIP: ",instance.private_ip_address)
instances.terminate_instance(instance.id)

