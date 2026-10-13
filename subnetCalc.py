import ipaddress

def calculate_subnet(ip_input: str) -> None:
    """
    Parses, validates, and prints comprehensive network parameters
    for a given IP address with a CIDR prefix.
    """
    try:
        # strict=False allows network addresses with host bits set (e.g., 192.168.1.5/24)
        network = ipaddress.ip_network(ip_input, strict=False)
        
        print(f"\n{'='*40}")
        print(f" Network Summary: {network}")
        print(f"{'='*40}")
        print(f" IP Version:        IPv{network.version}")
        print(f" Network Address:   {network.network_address}")
        print(f" Broadcast Address: {network.broadcast_address}")
        print(f" Subnet Mask:       {network.netmask}")
        print(f" Wildcard Mask:     {network.hostmask}")
        print(f" Total IP Count:    {network.num_addresses}")
        
        # Calculate usable host range for IPv4
        if network.version == 4:
            if network.prefixlen >= 31:
                print(" Usable Host Range: N/A (Point-to-point /31 or host route /32)")
            else:
                hosts = list(network.hosts())
                print(f" Usable Host Range: {hosts[0]} - {hosts[-1]}")
                print(f" Total Usable Hosts: {len(hosts)}")
                
        print(f" Private IP:        {network.is_private}")
        print(f" Global/Public IP:  {network.is_global}")
        print(f"{'='*40}\n")
        
    except ValueError as e:
        print(f"\n[ERROR] Invalid network input: {e}")
        print("Please use standard CIDR notation (e.g., 192.168.1.0/24 or 2001:db8::/32).\n")

if __name__ == "__main__":
    print("=== Python IP Address Tracker & Subnet Calculator ===")
    user_input = input("Enter IP address with CIDR prefix: ").strip()
    calculate_subnet(user_input)
