import csv
import ipaddress
import os

def calculate_all_possible_subnets(start_ip, end_ip):

    """
      Calculates all possible subnets within the given IP range.

      Args:
          start_ip (str): Starting IP address.
          end_ip (str): Ending IP address.

      Returns:
          list: List of CIDR notation subnets.
      """

    start_int = int(ipaddress.ip_address(start_ip))
    end_int = int(ipaddress.ip_address(end_ip))

    all_possible_ranges = []

    for prefix_length in range(0, 33):  # Iterate over all possible subnet mask lengths
        subnet_mask = (0xFFFFFFFF << (32 - prefix_length)) & 0xFFFFFFFF
        num_addresses = 2 ** (32 - prefix_length)

        subnet_start = start_int & subnet_mask
        subnet_end = subnet_start + num_addresses - 1

        if subnet_start >= start_int and subnet_end <= end_int:
            subnet_network = ipaddress.ip_address(subnet_start)
            subnet_cidr = f"{subnet_network}/{prefix_length}"
            all_possible_ranges.append(subnet_cidr)

    return all_possible_ranges


def read_csv_and_generate_ip_ranges(filename):
    """
       Reads IP ranges from a CSV file and generates subnets.

       Args:
           filename (str): Path to the CSV file.

       Returns:
           list: List of CIDR notation subnets.
       """

    ip_ranges = []

    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header

        for row in reader:
            start_ip = row[0]
            end_ip = row[1]
            if not start_ip or not end_ip:  # Check if either IP is None or empty
                continue  # Skip this row if either IP is None or empty
            subnets = calculate_all_possible_subnets(start_ip, end_ip)
            ip_ranges.extend(subnets)

    return ip_ranges


def write_ip_ranges_to_csv(ip_ranges, output_filename):

    """
        Writes IP ranges to a CSV file.

        Args:
            ip_ranges (list): List of CIDR notation subnets.
            output_filename (str): Path to the output CSV file.
        """

    with open(output_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['IP Range'])  # Write header

        for ip_range in ip_ranges:
            writer.writerow([ip_range])


def getRange(country_file, country, country_output_folder):

    """
       Generates and writes subnet masks for IP ranges from a CSV file.

       Args:
           country_file (str): Path to the input CSV file.
           country (str): Country name (used for output filename).

       Returns:
           None
       """

    input_filename = os.path.join(country_output_folder, f'{country_file}')
    output_filename = os.path.join(country_output_folder, f'{country}_All_Subnet_Masks.csv')
    ip_ranges = read_csv_and_generate_ip_ranges(input_filename)
    write_ip_ranges_to_csv(ip_ranges, output_filename)
    print(f"All possible IP ranges with their subnet masks have been written to {output_filename}")
