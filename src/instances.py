import boto
import boto.ec2

ami_ubuntu = 'ami-29ebb519'
boto.set_stream_logger('boto')
ec2 = boto.ec2.connect_to_region('us-west-2')

def startOneDefaultInstance():
    return ec2.run_instances(ami_ubuntu, instance_type='t2.micro')

