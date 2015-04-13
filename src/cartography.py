import argparse
import boto
import time
import boto.ec2 as ec2
import instances

def parse_args(connection):
    default_types = ['t2.micro', 't2.small', 't2.medium']
    available_zones = [z.name for z in connection.get_all_zones()]
    default_zones = available_zones
    available_types = \
        ['t2.micro', 't2.small', 't2.medium', 'm3.medium',
         'm3.large', 'm3.xlarge', 'm3.2xlarge']
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', default=3, type=int,
            help='number of samples to take at each interval',
            dest='num_samples')
    parser.add_argument(
        '--zones', '-z', default=default_zones, nargs='+',
        choices=available_zones,
        help='AWS availability zones to create instances in') 
    parser.add_argument(
        '--types', '-t', default=default_types, nargs='+',
        choices=available_types,
        help='AWS instance types to create') 
    return parser.parse_args()

def collect_data(connection, n, types, zones):
    print("ZONE\t\t TYPE\t\t IP\t\t")
    all_instances = []
    for (z,t) in [(z,t) for z in zones for t in types]:
        try:
            zone_type_instances = instances.start_instances(n, ec2=connection, type=t, zone=z)
            for instance in zone_type_instances:
                print(instance.placement,"\t",instance.instance_type,"\t",instance.private_ip_address)
                instances.terminate_instance(instance.id)
            all_instances.append(zone_type_instances)
        except boto.exception.BotoServerError as e:
            zone_type_instances = []
        time.sleep(1)

connection = ec2.connect_to_region('us-west-2')

args = parse_args(connection)
collect_data(connection, args.num_samples, args.types, args.zones)

