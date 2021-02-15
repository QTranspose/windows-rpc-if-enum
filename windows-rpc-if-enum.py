#!/usr/bin/python3

import sys
from ipaddress import ip_address
from impacket.dcerpc.v5 import transport
from impacket.dcerpc.v5.dcomrt import IObjectExporter
from impacket.dcerpc.v5.rpcrt import RPC_C_AUTHN_LEVEL_NONE

try:
    target = sys.argv[1]
except:
    print("[!] Usage: python3 windows-rpc-if-enum.py <target>")
    exit()

rpctransport = transport.DCERPCTransportFactory(f"ncacn_ip_tcp:{target}")

dce = rpctransport.get_dce_rpc()
dce.set_auth_level(RPC_C_AUTHN_LEVEL_NONE)
try:
    dce.connect()
except:
    print("[!] Cannot connect to RPC service")
    exit()

exporter = IObjectExporter(dce)
bindings = exporter.ServerAlive2()

for binding in bindings:
    addr = binding['aNetworkAddr'].strip('\x00')
    try:
        ip_address(addr)
        print(f"[+] Target has IP address: {addr}")
    except:
        print(f"[+] Target has hostname: {addr}")
