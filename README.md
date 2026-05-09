# Network Ping Sweeper

Command line threaded network ping sweeper written in Python.

## Features
- Takes in a custom subnet entered by user 
- Uses threading to scan all hosts simultaneously
- Displays all active hosts found on the subnet
- Displays a summary of how many hosts were found and total elapsed time 

## Usage
```bash
python sweeper.py
```

Enter the subnet when prompted.

## Example Output
```
Enter subnet: 192.168.1.0/24
Scanning 192.168.1.0/24...
----------------------------------------
192.168.1.1 is ACTIVE
192.168.1.4 is ACTIVE
192.168.1.7 is ACTIVE
192.168.1.47 is ACTIVE
192.168.1.99 is ACTIVE
192.168.1.2 is ACTIVE
192.168.1.14 is ACTIVE
Scan completed in 3.05 seconds.
7 hosts found.
```

