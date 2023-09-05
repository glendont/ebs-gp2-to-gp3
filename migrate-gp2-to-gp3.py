import boto3

def get_volume_ids():
    ec2 = boto3.client('ec2', region_name='ap-south-1')  # Replace with your region
    
    # Use filters to narrow down the volumes you want to upgrade
    filters = [
        {'Name': 'volume-type', 'Values': ['gp2']},  # Replace with your criteria
        # Add more filters as needed
    ]
    
    response = ec2.describe_volumes(Filters=filters)
    volume_ids = [volume['VolumeId'] for volume in response['Volumes']]
    
    return volume_ids

def lambda_handler(event, context):
    volume_ids = get_volume_ids()
    
    ec2 = boto3.client('ec2', region_name='your-region')  # Replace with your region
    
    for volume_id in volume_ids:
        response = ec2.modify_volume(VolumeId=volume_id, VolumeType='gp3')
        print(f"Volume {volume_id} modification triggered.")

    return "All volume modifications triggered."
