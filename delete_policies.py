import boto3

def delete_policy(policy_arn):
    iam_client = boto3.client('iam')
    try:
        iam_client.delete_policy(PolicyArn=policy_arn)
        print(f"Policy '{policy_arn}' successfully deleted.")
    except Exception as e:
        print(f"Error deleting policy '{policy_arn}': {str(e)}")

def execute(account_id):

# List of policies to delete
    policies_to_delete = [
        f'arn:aws:iam::{account_id}:policy/CloudHealth',
        f'arn:aws:iam::{account_id}:policy/doitintl_cmp',
        f'arn:aws:iam::{account_id}:policy/AWSStrategic',
        f'arn:aws:iam::{account_id}:policy/AccessToCostExplorer'
        # Add more policy ARNs here...
    ]

    for policy_arn in policies_to_delete:
        delete_policy(policy_arn)









