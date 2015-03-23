import boto
import boto.ec2 as ec2
import instances

n = 3
default_types = ['t2.micro', 't2.small', 't2.medium']

def collect_data(n, types):
    print("TYPE\t\t IP")
    for t in types:
        all_instances = instances.start_instances(n, type=t)
        for instance in all_instances:
            print(instance.instance_type,"\t",instance.private_ip_address)
            instances.terminate_instance(instance.id)

collect_data(n, default_types)

