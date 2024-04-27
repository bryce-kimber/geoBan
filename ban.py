import csv
import math


def ip_to_int(ip):

    """
       Converts an IP address (in dotted decimal format) to an integer.

       Args:
           ip (str): The IP address in the format 'x.x.x.x'.

       Returns:
           int: The corresponding integer representation of the IP address.
       """

    octets = map(int, ip.split('.'))
    return sum(octet << (i * 8) for i, octet in enumerate(reversed(list(octets))))


def int_to_ip(int_ip):

    """
        Converts an integer to an IP address (in dotted decimal format).

        Args:
            int_ip (int): The integer representation of an IP address.

        Returns:
            str: The IP address in the format 'x.x.x.x'.
        """

    return '.'.join(str((int_ip >> (i * 8)) & 0xFF) for i in reversed(range(4)))


def calculate_subnet_mask(start_ip, end_ip):

    """
        Calculates the subnet mask length (CIDR notation) based on a range of IP addresses.

        Args:
            start_ip (str): The starting IP address.
            end_ip (str): The ending IP address.

        Returns:
            int: The subnet mask length (e.g., 24 for a /24 subnet).
        """

    num_addresses = ip_to_int(end_ip) - ip_to_int(start_ip) + 1
    return 32 - int(math.log2(num_addresses))


def read_csv_and_generate_ip_ranges(filename):
    ip_ranges = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header
        for row in reader:
            if len(row) >= 2 and row[0] and row[1]:  # Check if both IPs are present and not empty
                start_ip = row[0].strip()  # Assuming start IPs are in column A
                end_ip = row[1].strip()  # Assuming end IPs are in column B
                subnet_mask = calculate_subnet_mask(start_ip, end_ip)
                ip_ranges.append(f"{start_ip}/{subnet_mask}")

    return ip_ranges


def calculateBanRanges(country_file, name):
    filename = f'{country_file}'  # Replace with your CSV file name
    outputfile = f'{name}_ranges_to_block.csv'
    ip_ranges = read_csv_and_generate_ip_ranges(filename)

    # Write the list to a CSV file
    with open(f'{outputfile}', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['IP Range'])  # Write header
        for ip_range in ip_ranges:
            writer.writerow([ip_range])

    print(f"IP ranges have been written to {outputfile}")
