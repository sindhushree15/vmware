import requests
import urllib3
from vmware.vapi.vsphere.client import create_vsphere_client
session = requests.session()

# Disable cert verification for demo purpose. 
# This is not recommended in a production environment.
session.verify = False

# Disable the secure connection warning for demo purpose.
# This is not recommended in a production environment.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print("Connecting to vCenter...");
# Connect to a vCenter Server using username and password
try:
    vsphere_client = create_vsphere_client(server='https://localhost:8080/', username='sindhu', password='sindhu$123', session=session)
except Exception as e:
  print("An exception occurred")
  print(e)
# List all VMs inside the vCenter Server
#vsphere_client.vcenter.VM.list()