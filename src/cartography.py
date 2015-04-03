import argparse
import boto
import time
import boto.ec2 as ec2
import instances

n = 3
default_types = ['t2.micro', 't2.small', 't2.medium']
default_zones = ['us-west-2a', 'us-west-2b', 'us-west-2c']

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', default=3, type=int,
            help='number of samples to take at each interval',
            dest='num_samples')
    return parser.parse_args()

def collect_data(n, types, zones):
    print("ZONE\t\t TYPE\t\t IP\t\t")
    all_instances = []
    for (z,t) in [(z,t) for z in zones for t in types]:
        try:
            zone_type_instances = instances.start_instances(n, type=t, zone=z)
            for instance in zone_type_instances:
                print(instance.placement,"\t",instance.instance_type,"\t",instance.private_ip_address)
                instances.terminate_instance(instance.id)
            all_instances.append(zone_type_instances)
        except boto.exception.BotoServerError as e:
            zone_type_instances = []
        time.sleep(1)

args = parse_args()
collect_data(args.num_samples, default_types, default_zones)

