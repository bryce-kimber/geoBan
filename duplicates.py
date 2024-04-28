import csv
import json
import os


def read_csv(filename):
    data_list = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header
        for row in reader:
            data_list.append(tuple(row))  # Convert each row to a tuple and append to the list
    return data_list


def search(list1, list2):  # Looks for duplicates between the two files
    set1 = set(list1)
    set2 = set(list2)
    duplicates = set1.intersection(set2)
    return list(duplicates)


def write_matches_to_csv(output_file, duplicate_entries):  # Writes matches to csv
    with open(f'{output_file}', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Blocklist Matches'])  # Write header
        for entry in duplicate_entries:
            writer.writerow(entry)


def findMatches(country, country_output_folder):
    # Specify the filenames for the CSV files
    filename1 = os.path.join(country_output_folder, f'{country}_All_Subnet_Masks.csv')
    config_file = 'config.json'
    output_file = os.path.join(country_output_folder, f'{country}_Blocked_Matches.csv')

    # Check if the configuration file exists
    if os.path.isfile(config_file):
        with open(config_file, 'r') as f:  # open config file
            config = json.load(f)
        filename2 = config.get('block_list_path', '')
        confirmation = input(f"Is {filename2} the correct location of your block list? (yes/no): ")  # verify file path
        while confirmation.lower() not in ['yes', 'no']:
            confirmation = input("Please respond with either 'yes' or 'no': ")
        if confirmation.lower() == 'no':
            filename2 = input("Please enter the correct file path of the block list: ")  # prompt user for correct file path
            config['block_list_path'] = filename2  # change file path in config file
            with open(config_file, 'w') as f:
                json.dump(config, f)
    else:
        filename2 = input("Please enter the file path of the block list: ")  # create file path config file
        config = {'block_list_path': filename2}
        with open(config_file, 'w') as f:
            json.dump(config, f)

    # Read data from both CSV files
    data_list1 = read_csv(filename1)
    data_list2 = read_csv(filename2)

    # Find duplicates between the two lists
    duplicate_entries = search(data_list1, data_list2)

    # Print duplicates and their count
    if duplicate_entries:
        print("Matches:")
        for entry in duplicate_entries:
            print(entry)
        print(f"Total number of matches: {len(duplicate_entries)}")

        # Write duplicates to a CSV file
        write_matches_to_csv(output_file, duplicate_entries)
        print(f"Matches saved to {output_file}")
    else:
        print("No matches found.")
