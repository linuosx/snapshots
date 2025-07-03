from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

def get_compute_client(subscription_id: str) -> ComputeManagementClient:
    credential = DefaultAzureCredential()
    return ComputeManagementClient(credential, subscription_id)
