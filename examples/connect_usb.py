# Requires: sudo pip3 install metawear
# usage: sudo python3 scan_connect.py
from mbientlab.metawear import MetaWearAsyncio
from mbientlab.metawear.cbindings import *
from bleak import BleakScanner
import asyncio
import serial

async def main():
    selection = -1
    while selection == -1:
        print("scanning for devices...")

        devices = await BleakScanner.discover()

        i = 0
        for device in devices:
            print("[",i,"]", device)
            i+= 1

        msg = "Select your device (-1 to rescan): "
        selection = int(input(msg))

    address = list(devices)[selection].address
    print("Connecting to %s..." % (address))
    device = MetaWearAsyncio(address)
    await device.usb.connect()

    print("Connected to " + device.address + " over USB")
    print("Device information: " + str(device.info))

    await device.disconnect_asyncio()
    print("Disconnected")

asyncio.run(main())
