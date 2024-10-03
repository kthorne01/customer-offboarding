#deletes roles and detaches policies
#tested and worked on all roles and policies attached to them on Wednesday 8/16/23

import boto3

def detach_policies(role_to_policies_map):
    iam_client = boto3.client('iam')

    for role_name, policy_arns in role_to_policies_map.items():
        for policy_arn in policy_arns:
            try:
                iam_client.detach_role_policy(RoleName=role_name, PolicyArn=policy_arn)
                print(f"Policy '{policy_arn}' detached from role '{role_name}'.")
            except Exception as e:
                print(f"Error detaching policy '{policy_arn}' from role '{role_name}': {str(e)}")

def remove_inline_policies(role_to_inline_policies_map):
    iam_client = boto3.client('iam')

    for role_name, policy_names in role_to_inline_policies_map.items():
        for policy_name in policy_names:
            try:
                iam_client.delete_role_policy(RoleName=role_name, PolicyName=policy_name)
                print(f"Inline policy '{policy_name}' removed from role '{role_name}'.")
            except Exception as e:
                print(f"Error removing inline policy '{policy_name}' from role '{role_name}': {str(e)}")

def remove_roles(role_names):
    iam_client = boto3.client('iam')

    for role_name in role_names:
        try:
            iam_client.delete_role(RoleName=role_name)
            print(f"Role '{role_name}' successfully removed.")
        except Exception as e:
            print(f"Error removing role '{role_name}': {str(e)}")

# account_number = input("Enter your AWS account number: ")
def execute(account_id):

# Map roles to their respective policies
    role_to_policies_map = {
        'CloudHealth': [f'arn:aws:iam::{account_id}:policy/CloudHealth'],
        'doitintl_cmp': [f'arn:aws:iam::{account_id}:policy/doitintl_cmp'],
        'AWSAdmin': [f'arn:aws:iam::aws:policy/AdministratorAccess'],
        'AWSStrategic': [
            f'arn:aws:iam::{account_id}:policy/AWSStrategic',
            f'arn:aws:iam::aws:policy/AWSSupportAccess',
            f'arn:aws:iam::aws:policy/job-function/SupportUser',
            f'arn:aws:iam::aws:policy/job-function/Billing',
            f'arn:aws:iam::aws:policy/AWSSavingsPlansFullAccess'
        ],
        'DoiT-SSO-Administrator': [f'arn:aws:iam::aws:policy/AdministratorAccess'],
        'DoiT-SSO-Strategic': [
            f'arn:aws:iam::{account_id}:policy/AWSStrategic',
            f'arn:aws:iam::aws:policy/AWSSupportAccess',
            f'arn:aws:iam::aws:policy/job-function/SupportUser',
            f'arn:aws:iam::aws:policy/job-function/Billing',
            f'arn:aws:iam::aws:policy/AWSSavingsPlansFullAccess'
        ],
        'DoiT-SSO-Billing-and-Support': [
            f'arn:aws:iam::aws:policy/AWSSupportAccess',
            f'arn:aws:iam::aws:policy/job-function/ViewOnlyAccess',
            f'arn:aws:iam::aws:policy/AWSBillingReadOnlyAccess',
        ]
    }

    role_to_inline_policies_map = {
    'DoiT-SSO-Billing-and-Support': ['AccessToCostExplorer'],
    # ... (more roles and inline policies)
    }
        
    detach_policies(role_to_policies_map)
    remove_inline_policies(role_to_inline_policies_map)
    remove_roles(role_to_policies_map.keys())
    
    


