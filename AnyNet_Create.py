import requests
import json

###Creates a Branch to Branch (AnyNet) VPN tunnel

###Specify Static Values
TenantID= "10000"
AuthTOKEN= "Insert Token Here"
Site1_SiteID="Specify SITE ID"
Site1_WAN_IF="Specify SITE WANT INTERFACE ID"
Site2_SiteID="Specify SITE ID"
Site2_WAN_IF="Specify SITE WANT INTERFACE ID"
######################################

url = "https://api.elcapitan.cloudgenix.com/v3.4/api/tenants/{}/anynetlinks".format(TenantID)

payload = json.dumps({
    "name": "TESTANYNET",
    "admin_up": True,
    "description": "TEST DESC",
    "ep1_site_id": Site1_SiteID,
    "ep1_wan_if_id": Site1_WAN_IF,
    "ep2_site_id": Site2_SiteID,
    "ep2_wan_if_id": Site2_WAN_IF,
    "forced": True,
    "tags": None,
    "type": None,
    "vpnlink_configuration": None,
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'x-auth-token': AuthTOKEN
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

#######################################

