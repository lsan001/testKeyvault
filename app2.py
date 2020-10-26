import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
#from azure.identity import ManagedIdentityCredential
 
VAULT_URL = os.environ['VAULT_URL']
SECRET_NAME = 'test-me'
 
# default azure client first tries to auth with service principal credentials using env variables
# if they are not available it will try to use managed identity
credential = DefaultAzureCredential()
client = SecretClient(vault_url=VAULT_URL, credential=credential)
 
retrieved_secret = client.get_secret(SECRET_NAME)
 
print(retrieved_secret.value)
