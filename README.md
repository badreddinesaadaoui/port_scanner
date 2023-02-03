Description :

This script allows you to perform a port scan using the nmap library. You can specify the IP address, scan type, verbosity level, scan time, and ports to scan. The output of the scan will be saved to a file in the your_scans folder.

Requirements:

    - Python 3
    - nmap library
 
Usage :

    1- Run the script in your terminal by typing python nmap_scanner.py
    2- Enter the IP address to be scanned
    3- Enter the scan type (S, U, T, A, W, M, N)
    4- Enter the verbosity level (v, vv)
    5- Enter the scan time (1-5)
    6- Enter the ports to be scanned (e.g. 1-21,22,80,443)
    7- Enter the file name for the scan output
    8- The scan results will be saved to the your_scans folder with the specified file name.
 
Note :

    - The your_scans folder will be created if it doesn't exist.
    - The output file will be saved in plain text format.
 
Contributions :

Contributions are welcome. If you have an idea for a new feature or have found a bug, please open an issue or submit a pull request.
