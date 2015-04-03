import boto
import boto.ec2

ami_ubuntu = 'ami-29ebb519'
ec2 = boto.ec2.connect_to_region('us-west-2')

def start_instance(type='t2.micro', placement=None):
    ''' Start an EC2 instance using the default settings that we care about '''
    return start_instances(1,type,placement)[0]

def start_instances(n, type='t2.micro', zone=None):
    ''' Start multiple EC2 instances using the default settings that we care
    about '''
    return ec2.run_instances(ami_ubuntu, instance_type=type,
                             min_count=n, max_count=n,
                             placement=zone).instances

def terminate_instance(id):
    ''' Wrapper for the EC2 terminate instance command '''
    return ec2.terminate_instances(id)

