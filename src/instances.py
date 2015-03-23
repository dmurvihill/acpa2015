import boto
import boto.ec2

ami_ubuntu = 'ami-29ebb519'
ec2 = boto.ec2.connect_to_region('us-west-2')

def start_instance():
    ''' Start an EC2 instance using the default settings that we care about '''
    return ec2.run_instances(ami_ubuntu, instance_type='t2.micro').instances[0]

def terminate_instance(id):
    ''' Wrapper for the EC2 terminate instance command '''
    return ec2.terminate_instances(id)

