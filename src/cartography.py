import boto
import boto.ec2 as ec2
import instances

def collect_data(n):
    print("TYPE\t\tIP")
    all_instances = instances.start_instances(n)
    for instance in all_instances:
        print(instance.instance_type,"\t\t",instance.private_ip_address)
        instances.terminate_instance(instance.id)

