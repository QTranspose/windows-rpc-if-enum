## windows-rpc-if-enum
By abusing `ServerAlive2()` method in DCOM Remote Protocol, an attacker can gather information about hostname and all interfaces of a windows machine running RPC service, without needing any authentication. For detailed reading refer to [here](https://airbus-cyber-security.com/the-oxid-resolver-part-1-remote-enumeration-of-network-interfaces-without-any-authentication/).

## Usage
```
python3 windows-rpc-if-enum.py <target>
```
![example](img/example.svg)

## Dependencies
[Impacket](https://github.com/SecureAuthCorp/impacket)
```
sudo apt install python3-impacket (Kali/Parrot/Ubuntu/Debian)
```
or
```
pip3 install --user impacket
```
