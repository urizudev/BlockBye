import os
import winreg

# Set the DNS server addresses
dns_server1 = "8.8.8.8"
dns_server2 = "8.8.4.4"

# Registry key for network adapter settings
key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters", 0, winreg.KEY_WRITE)

# Set the DNS server addresses
winreg.SetValueEx(key, "NameServer", 0, winreg.REG_SZ, dns_server1 + "," + dns_server2)

# Close the registry key
winreg.CloseKey(key)


