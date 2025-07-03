from decouple import config
from datetime import datetime
# Configuración del entorno
SNAPSHOT_CONFIF = {
    "SUBSCRIPTION_ID" : config("SUBSCRIPTION_ID"),
    "SOURCE_RG" : config("SOURCE_RG"),
    "TARGET_RG" : config("TARGET_RG"),
    "VM_NAME" : config("VM_NAME"),
    "LOCATION" : config("LOCATION", default="eastus"),  # Default to eastus if not set
}

SNAPSHOT_CONFIF["SNAPSHOT_NAME"] = f"snapshot-{SNAPSHOT_CONFIF['VM_NAME']}-{{}}-{datetime.now().strftime('%Y%m%d-%H%M%S')}"