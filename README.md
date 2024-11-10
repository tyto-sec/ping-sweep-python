# Ping Sweep Script

This Python script performs a customizable ping sweep on a specified network, allowing users to define payload size, delays, timeout, and ICMP packet type. By adjusting parameters, users can control the sweep’s network load and packet properties, making it suitable for various testing scenarios.

## Features

- **Customizable Payload Size**: Allows setting the size of the ICMP packet payload.
- **Adjustable Delays**: Supports minimum and maximum delays between pings for flexibility in network load.
- **Timeout Control**: Allows setting a timeout duration to wait for each ICMP response.
- **ICMP Timestamp Option**: Offers the ability to send ICMP timestamp requests instead of standard echo requests.

## Prerequisites

- **Python 3**: The script requires Python 3.
- **Scapy**: Install with `pip install scapy`.
- **Network Permissions**: Sending ICMP packets typically requires root or administrator privileges.

## Usage

Run the script with the target network in CIDR notation. You can specify additional options to customize the sweep.

```bash
sudo python3 ping_sweep.py <network> [-M <max_delay>] [-m <min_delay>] [-t <timeout>] [-s <size>] [-ts]
```

### Arguments

- **network**: Network address in CIDR notation (e.g., `192.168.1.0/24`).
- **-M, --max_delay**: Maximum delay between pings in seconds (default is 0).
- **-m, --min_delay**: Minimum delay between pings in seconds (default is 0).
- **-t, --timeout**: Timeout in seconds to wait for an ICMP response (default is 0.3).
- **-s, --size**: Size of the random payload in bytes (default is 60).
- **-ts, --timestamp**: Use ICMP timestamp requests instead of echo requests.


## Notes

- **Permissions**: ICMP requests often require root privileges, so you may need to run the script with `sudo`.
- **Network Load Management**: Use the `-M` and `-m` delay options to adjust the script’s impact on the network.

## Author

Written by tyto.
