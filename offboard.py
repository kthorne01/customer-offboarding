import detach_and_delete_roles
import delete_policies
import delete_ips

import boto3

sts = boto3.client('sts')
organization = boto3.client('organizations')

def extract_master_account():
    try:
        caller_account_id =  sts.get_caller_identity()['Account']
        management_account_id =  organization.describe_organization()['Organization']['MasterAccountId']
        assert caller_account_id == management_account_id
        return int(caller_account_id)
    except Exception as e:
         print(f"{str(e)}")

def main():
    account_id = extract_master_account()
   
    # Execute the functions from each script in the desired order
    detach_and_delete_roles.execute(account_id)
    delete_policies.execute(account_id)
    delete_ips.execute(account_id)

if __name__ == "__main__":
    main()