import nmap
import os

# Ask for user input for IP address
ip_address = input("Enter IP address: ")

# Ask for user input for scan type
scan_type = input("Enter scan type (S, U, T, A, W, M, N): ")

# Ask for user input for verbosity
verbosity = input("Enter verbosity level (v, vv, vvv): ")

# Ask for user input for scan time
scan_time = input("Enter scan time (1-5): ")

# Ask for user input for ports to scan
ports = input("Enter ports to scan (e.g. 1-21,22,80,443): ")

# Initialize the nmap scanner
nm = nmap.PortScanner()

# Run the scan
nm.scan(ip_address, arguments=f"-s{scan_type} -{verbosity} -p{ports} -T{scan_time}")

# Create a folder named "your_scans" if it doesn't exist
if not os.path.exists("your_scans"):
    os.makedirs("your_scans")

# Ask for user input for file name
file_name = input("Enter the file name: ")
filename = f"your_scans/{file_name}.txt"

# Save the scan output to a file in the "your_scans" folder
with open(filename, 'w') as f:
    f.write(nm.get_nmap_last_output().decode('utf-8'))

# Print success message
print(f"Scan results saved to your_scans/{file_name}.txt")
