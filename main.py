import asyncio
import requests
from bleak import BleakScanner

async def scan_devices():
    devices = await BleakScanner.discover()
    return devices

def post_mac_addresses(mac_addresses):
    url = 'https://fling.test/device-macs'
    data = mac_addresses
    response = requests.post(url, json=data)
    if response.status_code == 201:
        print("MAC addresses successfully posted to the API.")
    else:
        print("HERE IS THE DATA EXAMPLE:")
        print(data)
        print("!!!!!!!!!!!!")
        print("Failed to post MAC addresses to the API. Status code:", response.status_code)
        #print(response.content)

if __name__ == "__main__":
    print("Scanning for nearby Bluetooth devices...")
    loop = asyncio.get_event_loop()
    nearby_devices = loop.run_until_complete(scan_devices())

    print("Found {} devices:".format(len(nearby_devices)))
    mac_addresses = [str(device.address) for device in nearby_devices]  # Convert UUID objects to strings

    for device in nearby_devices:
        print("   {} - {}".format(str(device.address), device.name))  # Convert UUID object to string

    if mac_addresses:
        print("Posting MAC addresses to the API...")
        post_mac_addresses(mac_addresses)
    else:
        print("No MAC addresses found to post.")
