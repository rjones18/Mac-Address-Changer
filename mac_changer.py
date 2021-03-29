#!/usr/bin/env python

import subprocess

interface = input("interface > ")
new_mac = input('New Mac > ')

print(f"{interface} MAC Address has been successfully changed to {new_mac}.")
subprocess.call('ifconfig ' + interface + ' down', shell=True)
subprocess.call('ifconfig ' + interface + ' hw ether ' + new_mac, shell=True)
subprocess.call('ifconfig ' + interface + ' up', shell=True)
subprocess.call('ifconfig ', shell=True)
