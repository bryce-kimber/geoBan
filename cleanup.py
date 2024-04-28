import os


def cleanupBlocklistCheck(country_file, name, country_output_folder):
    country_file = os.path.join(country_output_folder, country_file)
    # Check if the specified country file exists
    if os.path.isfile(country_file):
        print(f"Removing {country_file}")  # Print a message indicating the file is being removed
        os.remove(country_file)  # Remove the file
    else:
        print(f"{country_file} does not exist")  # Print a message if the file does not exist

    # Create the subnet file name based on the provided possibleSubnets value
    subnet_file = os.path.join(country_output_folder, f'{name}_All_Subnet_Masks.csv')
    # Check if the subnet file exists
    if os.path.isfile(subnet_file):
        print(f"Removing {subnet_file}")  # Print a message indicating the file is being removed
        os.remove(subnet_file)  # Remove the file
    else:
        print(f"{subnet_file} does not exist")  # Print a message if the file does not exist

def cleanupBanlistCheck(country_file, country_output_folder):
    country_file = os.path.join(country_output_folder, country_file)
    # Check if the specified country file exists
    if os.path.isfile(country_file):
        print(f"Removing {country_file}")  # Print a message indicating the file is being removed
        os.remove(country_file)  # Remove the file
    else:
        print(f"{country_file} does not exist")  # Print a message if the file does not exist