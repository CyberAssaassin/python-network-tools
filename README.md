# Python IP Address Tracker & Subnet Calculator

A lightweight, production-ready Python command-line tool that parses, validates, and calculates essential network parameters for any IPv4 or IPv6 subnet using Python's built-in `ipaddress` module.

## Features
* Validates user input using standard CIDR notation.
* Computes network address, broadcast address, netmask, and wildcard mask.
* Calculates total IP addresses and usable host ranges (IPv4).
* Identifies whether an address is private or public/global.
* Robust error handling for invalid subnet entries.

## Requirements
* Python 3.x (No external dependencies required).

## Usage
Run the script from your terminal:
```bash
python subnet_calc.py

Example Output

=== Python IP Address Tracker & Subnet Calculator ===
Enter IP address with CIDR prefix: 192.168.1.0/24

========================================
 Network Summary: 192.168.1.0/24
========================================
 IP Version:        IPv4
 Network Address:   192.168.1.0
 Broadcast Address: 192.168.1.255
 Subnet Mask:       255.255.255.0
 Wildcard Mask:     0.0.0.255
 Total IP Count:    256
 Usable Host Range: 192.168.1.1 - 192.168.1.254
 Total Usable Hosts: 254
 Private IP:        True
 Global/Public IP:  False
========================================
