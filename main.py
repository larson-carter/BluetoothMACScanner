import asyncio
from bleak import BleakScanner


async def scan_devices():
    devices = await BleakScanner.discover()
    return devices


if __name__ == "__main__":
    print("Scanning for nearby Bluetooth devices...")
    loop = asyncio.get_event_loop()
    nearby_devices = loop.run_until_complete(scan_devices())

    print("Found {} devices:".format(len(nearby_devices)))
    for device in nearby_devices:
        print("   {} - {}".format(device.address, device.name))
