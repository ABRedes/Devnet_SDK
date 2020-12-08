import requests
from requests.auth import HTTPBasicAuth

DNAC_URL = "https://sandboxdnac2.cisco.com:443"
DNAC_USER = "devnetuser"
DNAC_PASS = "Cisco123!"


def get_auth_token(): 
    """ Building out Auth request. Using requests.post to make a call to the Auth Endpoint """ 
    
    url = '{}/dna/system/api/v1/auth/token'.format(DNAC_URL) 
    hdr = {'content-type' : 'application/json'} 
    
    resp = requests.post(url, auth=HTTPBasicAuth(DNAC_USER, DNAC_PASS), headers=hdr) 
    token = resp.json()['Token'] 
    
#    print("Token Retrieved: {}".format(token)) 
    return token 

token = get_auth_token()

def get_device_list(token): 

    # assign the authentication token to a header key value pair
    # 'x-auth-token'={{token}}
    hdr = {"x-auth-token": token}
    url = '{}/dna/intent/api/v1/network-device'.format(DNAC_URL)
    
    resp = requests.get(url, headers=hdr)

    return resp.json()

device_list = get_device_list(token) 

for device in device_list['response']:
    print(f'Hostname: {device["hostname"]} Serial Number: {device["serialNumber"]} Endereço IP: {device["managementIpAddress"]}')
