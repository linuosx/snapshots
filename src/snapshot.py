from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.compute.models import Snapshot

def create_snapshot(compute_client: ComputeManagementClient, disk, target_rg: str, location: str, snapshot_name: str ):
    snapshot_params = Snapshot(
        location=location,
        creation_data={
            "create_option": "copy",
            "source_uri": disk.id
        }
    )
    
    async_snapshot = compute_client.snapshots.begin_create_or_update(
        target_rg,
        snapshot_name,
        snapshot_params
    )
    snapshot = async_snapshot.result()
    return snapshot
