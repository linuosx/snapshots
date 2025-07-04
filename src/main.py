from auth import get_compute_client
from config import SNAPSHOT_CONFIF
from snapshot import create_snapshot

import logging

def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename='/var/log/snapshots/snapshot.log',
        filemode='a'
    )
    compute_client = get_compute_client(SNAPSHOT_CONFIF["SUBSCRIPTION_ID"])
    vm = compute_client.virtual_machines.get(SNAPSHOT_CONFIF["SOURCE_RG"], SNAPSHOT_CONFIF["VM_NAME"])

    disk_ids = [vm.storage_profile.os_disk.managed_disk.id]

    if vm.storage_profile.data_disks:
        for disk in vm.storage_profile.data_disks:
            disk_ids.append(disk.managed_disk.id)

    index = 0
    for disk_id in disk_ids:
        logging.info(f"Procesando disco: {disk_id}")
        disk_name = disk_id.split("/")[-1]
        disk = compute_client.disks.get(SNAPSHOT_CONFIF["SOURCE_RG"], disk_name)
        create_snapshot(compute_client, disk, SNAPSHOT_CONFIF["TARGET_RG"], SNAPSHOT_CONFIF["LOCATION"], SNAPSHOT_CONFIF["SNAPSHOT_NAME"].format("OS" if "OsDisk" in disk_name else "Data" + str(index)))
        logging.info(f"Snapshot creado para el disco: {disk_name}")
        index += 1

if __name__ == "__main__":
    main()
