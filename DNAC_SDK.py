from dnacentersdk import DNACenterAPI

DNAC_URL = "https://sandboxdnac2.cisco.com:443"
DNAC_USER = "devnetuser"
DNAC_PASS = "Cisco123!"

dnac = DNACenterAPI(username= DNAC_USER, password= DNAC_PASS, base_url= DNAC_URL)


"""From this point on, in order to access the subsequent API calls, you don’t have to worry about managing 
    your token validity, API headers or Rate-Limit handling. The SDK does that for you.

    Another great feature about the SDK is that it represents all returned JSON objects as native Python objects 
    so you can access all of the object’s attributes using native dot.syntax!"""

try:
    devices = dnac.devices.get_device_list(family='Switches and Hubs')
        
    for device in devices.response:
        print(f"Hostname: {device.hostname:25} Serial Number: {device.serialNumber} \
            Endereço IP: {device.managementIpAddress}      Uptime: {device.upTime}")
except ApiError as e:
    print(e)