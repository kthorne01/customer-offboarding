import boto3

def delete_saml_providers(account_id, provider_names):
    iam_client = boto3.client('iam')
    
    for provider_name in provider_names:
        arn = f'arn:aws:iam::{account_id}:saml-provider/{provider_name}'
        try:
            iam_client.delete_saml_provider(SAMLProviderArn=arn)
            print(f"SAML provider '{arn}' successfully deleted.")
        except Exception as e:
            print(f"Error deleting SAML provider '{arn}': {str(e)}")

def execute(account_id):

# Replace with your actual SAML provider names
    provider_names = [
        'DoIT-AWS-SSO',
        'DoIT-AWS-SSO2',
        'DoIT-AWS-SSO3'
        # Add more provider names as needed
    ]

    delete_saml_providers(account_id, provider_names)
