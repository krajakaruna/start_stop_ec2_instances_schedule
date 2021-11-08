import boto3
region = "us-east-1"
client = boto3.client('ec2', region_name=region)


def lambda_handler():
    response = client.describe_instances(
        Filters=[{
            'Name': 'tag:daily_stop',
            "Values" : ['yes']
         }, ],
        MaxResults = 100
    )

    instance_list = []

    for group in response['Reservations']:
        for instance in group['Instances']:

# Check whether the instance is in running state
            state = instance['State']
            if state['Name'] == "running":
                instance_list.append(instance['InstanceId'])
    
# stop the instances
    response2 = client.stop_instances(
        InstanceIds= instance_list
    )

    print(response2)

#lambda_handler()