import scraper as scraper
import ranges as ranges
import duplicates as du
import cleanup as clean
import ban

#  main user input options
EXIT = 'EXIT'
BACK = 'BACK'
YES = 'YES'
NO = 'NO'
CONTINUE = 'CONTINUE'


def get_user_input(prompt, valid_inputs):  # validate and modify user input
    while True:
        user_input = input(prompt).upper()
        if user_input in valid_inputs:
            return user_input
        else:
            print("Invalid input. Please try again.")


def main_menu(menu):
    # Example menu options
    first_menu = {
        1: "Find IP ranges to block",
        2: "Verify IP block list",
    }
    for key, value in first_menu.items():  # display menu options
        print(f"{key}. {value}")

    while True:
        option = input("Enter the number of the main menu option you want to select (or 'exit' to exit): ")

        if option.lower() == "exit":
            exit()
        elif option.isdigit() and int(option) in first_menu:
            if option == str(1):
                sub_menu3(menu)  # open menu 3
            elif option == str(2):
                sub_menu1(menu)  # open menu 1

            print(f"Selected option: {first_menu[int(option)]}")
        else:
            print("Invalid choice. Please enter a valid option number or 'exit'.")


def sub_menu1(menu):
    while True:
        for letter in sorted(menu.keys()):  # display menu options
            print(letter)
        option = get_user_input("Enter the letter of the main menu option you want to select (or 'back' to return to "
                                "the previous menu): ",
                                list(menu.keys()) + [BACK])
        if option == BACK:
            main_menu(menu)  # go back to main menu
        elif option in menu:
            sub_menu2(menu, option)  # go to menu 2


def sub_menu2(menu, option):
    while True:
        for i, (name, url) in enumerate(menu[option], start=1):  # display menu options
            print(f"  {i}. {name}")
        sub_option = get_user_input(
            "Enter the number of the country option you want to select (or 'back' to return to the previous menu): ",
            [str(i) for i in range(1, len(menu[option]) + 1)] + [BACK])
        if sub_option == BACK:
            sub_menu1(menu)  # go back to previous menu
        else:
            process_country(menu[option][int(sub_option) - 1])  # run function to get and process country data


def sub_menu3(menu):
    while True:
        for letter in sorted(menu.keys()):  # display menu options
            print(letter)
        option = get_user_input("Enter the letter of the main menu option you want to select (or 'back' to return to "
                                "the previous menu): ",
                                list(menu.keys()) + [BACK])
        if option == BACK:
            main_menu(menu)  # got to the main menu
        elif option in menu:
            sub_menu4(menu, option)  # go to menu 4


def sub_menu4(menu, option):
    while True:
        for i, (name, url) in enumerate(menu[option], start=1):  # display menu options
            print(f"  {i}. {name}")
        sub_option = get_user_input(
            "Enter the number of the country option you want to select (or 'back' to return to the previous menu): ",
            [str(i) for i in range(1, len(menu[option]) + 1)] + [BACK])
        if sub_option == BACK:
            sub_menu3(menu)  # go back to previous menu
        else:
            process_country_for_ban(menu[option][int(sub_option) - 1])  # run function to get and process country data


def process_country(country):
    name, url = country
    country_file = scraper.scrape(name, url)  # scrape site to get country data
    print("Storing table of IPs in " + country_file)
    ranges.getRange(country_file, name)  # get all possible IP ranges based on scraped data
    du.findMatches(name)  # compare user block list to country IP ranges
    cleanup_files(country_file, name)  # prompt user to delete tmp files
    continue_or_exit()


def process_country_for_ban(country):
    name, url = country
    country_file = scraper.scrape(name, url)  # scrape site to get country data
    print("Saving scraped data to " + f"{country_file}")
    ban.calculateBanRanges(country_file, name)  # calculate the largest possible CIDR ranges
    cleanup_files(country_file, name)  # prompt user to delete tmp files
    continue_or_exit()


def cleanup_files(country_file, name):
    while True:
        cleanup = get_user_input(
            f"Do you want to delete the files {country_file} and {name}_ALL_Subnet_Masks.csv? This will not delete the "
            f"results file {name}_Blocked_Matches.csv. Please answer 'yes' or 'no' ",
            [YES, NO])
        if cleanup == YES:  # delete tmp files
            print("Cleaning up...")
            clean.cleanup(country_file, name)
            break
        elif cleanup == NO:  # keep tmp files
            print("Very well...")
            break


def continue_or_exit():
    while True:
        want_to_continue = get_user_input("Do you want to continue or exit? Please enter 'continue' or 'exit' ",
                                          [CONTINUE, EXIT])
        if want_to_continue == CONTINUE:
            main()
        elif want_to_continue == EXIT:
            exit()


def main():

    # list of available countries
    names = ['Afghanistan', 'Aland Islands', 'Albania ', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla',
             'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia ', 'Austria',
             'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin',
             'Bermuda', 'Bhutan', 'Bolivia (Plurinational State of)', 'Bonaire, Sint Eustatius and Saba',
             'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory',
             'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada',
             'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo',
             'Congo (Democratic Republic of the)', 'Cook Islands', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba',
             'Curacao', 'Cyprus', 'Czechia', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador',
             'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia',
             'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana',
             'French Polynesia', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland',
             'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti',
             'Holy See', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia',
             'Iran (Islamic Republic of)', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan',
             'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea (Democratic People's Republic of)",
             'Korea (Republic of)', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon',
             'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'North Macedonia',
             'Madagascar', 'Malawi', 'Maldives', 'Mali', 'Marshall Islands', 'Martinique', 'Mauritius', 'Mayotte',
             'Micronesia (Federated States of)', 'Moldova (Republic of)', 'Mongolia', 'Montenegro', 'Morocco',
             'Mozambique', 'Namibia', 'Nauru', 'Netherlands', 'New Caledonia', 'Nicaragua', 'Niger', 'Niue',
             'Norfolk Island', 'Norway', 'Oman', 'Palau', 'Palestine, State of', 'Papua New Guinea', 'Paraguay',
             'Philippines', 'Pitcairn', 'Portugal', 'Puerto Rico', 'Reunion', 'Romania', 'Rwanda', 'Saint Barthelemy',
             'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines',
             'San Marino', 'Sao Tome and Principe', 'Senegal', 'Serbia', 'Sierra Leone', 'Singapore', 'Slovakia',
             'Slovenia', 'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sudan', 'Suriname', 'Eswatini', 'Sweden',
             'Syrian Arab Republic', 'Taiwan (Province of China)', 'Tanzania, United Republic of', 'Thailand', 'Togo',
             'Tokelau', 'Trinidad and Tobago', 'Tunisia', 'Turkmenistan', 'Turks and Caicos Islands', 'Uganda',
             'Ukraine', 'United Kingdom of Great Britain and Northern Ireland', 'United States of America', 'Uruguay',
             'Uzbekistan', 'Venezuela (Bolivarian Republic of)', 'Virgin Islands (British)', 'Virgin Islands (U.S.)',
             'Yemen', 'Zambia', '']

    # URLs to scrape
    urls = ['https://lite.ip2location.com/afghanistan-ip-address-ranges',
            'https://lite.ip2location.com/aland-islands-ip-address-ranges',
            'https://lite.ip2location.com/albania-ip-address-ranges',
            'https://lite.ip2location.com/algeria-ip-address-ranges',
            'https://lite.ip2location.com/american-samoa-ip-address-ranges',
            'https://lite.ip2location.com/andorra-ip-address-ranges',
            'https://lite.ip2location.com/angola-ip-address-ranges',
            'https://lite.ip2location.com/anguilla-ip-address-ranges',
            'https://lite.ip2location.com/antarctica-ip-address-ranges',
            'https://lite.ip2location.com/antigua-and-barbuda-ip-address-ranges',
            'https://lite.ip2location.com/argentina-ip-address-ranges',
            'https://lite.ip2location.com/armenia-ip-address-ranges',
            'https://lite.ip2location.com/aruba-ip-address-ranges',
            'https://lite.ip2location.com/australia-ip-address-ranges',
            'https://lite.ip2location.com/austria-ip-address-ranges',
            'https://lite.ip2location.com/azerbaijan-ip-address-ranges',
            'https://lite.ip2location.com/bahamas-ip-address-ranges',
            'https://lite.ip2location.com/bahrain-ip-address-ranges',
            'https://lite.ip2location.com/bangladesh-ip-address-ranges',
            'https://lite.ip2location.com/barbados-ip-address-ranges',
            'https://lite.ip2location.com/belarus-ip-address-ranges',
            'https://lite.ip2location.com/belgium-ip-address-ranges',
            'https://lite.ip2location.com/belize-ip-address-ranges',
            'https://lite.ip2location.com/benin-ip-address-ranges',
            'https://lite.ip2location.com/bermuda-ip-address-ranges',
            'https://lite.ip2location.com/bhutan-ip-address-ranges',
            'https://lite.ip2location.com/bolivia-(plurinational-state-of)-ip-address-ranges',
            'https://lite.ip2location.com/bonaire-sint-eustatius-and-saba-ip-address-ranges',
            'https://lite.ip2location.com/bosnia-and-herzegovina-ip-address-ranges',
            'https://lite.ip2location.com/botswana-ip-address-ranges',
            'https://lite.ip2location.com/bouvet-island-ip-address-ranges',
            'https://lite.ip2location.com/brazil-ip-address-ranges',
            'https://lite.ip2location.com/british-indian-ocean-territory-ip-address-ranges',
            'https://lite.ip2location.com/brunei-darussalam-ip-address-ranges',
            'https://lite.ip2location.com/bulgaria-ip-address-ranges',
            'https://lite.ip2location.com/burkina-faso-ip-address-ranges',
            'https://lite.ip2location.com/burundi-ip-address-ranges',
            'https://lite.ip2location.com/cabo-verde-ip-address-ranges',
            'https://lite.ip2location.com/cambodia-ip-address-ranges',
            'https://lite.ip2location.com/cameroon-ip-address-ranges',
            'https://lite.ip2location.com/canada-ip-address-ranges',
            'https://lite.ip2location.com/cayman-islands-ip-address-ranges',
            'https://lite.ip2location.com/central-african-republic-ip-address-ranges',
            'https://lite.ip2location.com/chad-ip-address-ranges',
            'https://lite.ip2location.com/chile-ip-address-ranges',
            'https://lite.ip2location.com/china-ip-address-ranges',
            'https://lite.ip2location.com/colombia-ip-address-ranges',
            'https://lite.ip2location.com/comoros-ip-address-ranges',
            'https://lite.ip2location.com/congo-ip-address-ranges',
            'https://lite.ip2location.com/congo-(democratic-republic-of-the)-ip-address-ranges',
            'https://lite.ip2location.com/cook-islands-ip-address-ranges',
            'https://lite.ip2location.com/costa-rica-ip-address-ranges',
            'https://lite.ip2location.com/cote-divoire-ip-address-ranges',
            'https://lite.ip2location.com/croatia-ip-address-ranges',
            'https://lite.ip2location.com/cuba-ip-address-ranges',
            'https://lite.ip2location.com/curacao-ip-address-ranges',
            'https://lite.ip2location.com/cyprus-ip-address-ranges',
            'https://lite.ip2location.com/czechia-ip-address-ranges',
            'https://lite.ip2location.com/denmark-ip-address-ranges',
            'https://lite.ip2location.com/djibouti-ip-address-ranges',
            'https://lite.ip2location.com/dominica-ip-address-ranges',
            'https://lite.ip2location.com/dominican-republic-ip-address-ranges',
            'https://lite.ip2location.com/ecuador-ip-address-ranges',
            'https://lite.ip2location.com/egypt-ip-address-ranges',
            'https://lite.ip2location.com/el-salvador-ip-address-ranges',
            'https://lite.ip2location.com/equatorial-guinea-ip-address-ranges',
            'https://lite.ip2location.com/eritrea-ip-address-ranges',
            'https://lite.ip2location.com/estonia-ip-address-ranges',
            'https://lite.ip2location.com/ethiopia-ip-address-ranges',
            'https://lite.ip2location.com/falkland-islands-(malvinas)-ip-address-ranges',
            'https://lite.ip2location.com/faroe-islands-ip-address-ranges',
            'https://lite.ip2location.com/fiji-ip-address-ranges',
            'https://lite.ip2location.com/finland-ip-address-ranges',
            'https://lite.ip2location.com/france-ip-address-ranges',
            'https://lite.ip2location.com/french-guiana-ip-address-ranges',
            'https://lite.ip2location.com/french-polynesia-ip-address-ranges',
            'https://lite.ip2location.com/gabon-ip-address-ranges',
            'https://lite.ip2location.com/gambia-ip-address-ranges',
            'https://lite.ip2location.com/georgia-ip-address-ranges',
            'https://lite.ip2location.com/germany-ip-address-ranges',
            'https://lite.ip2location.com/ghana-ip-address-ranges',
            'https://lite.ip2location.com/gibraltar-ip-address-ranges',
            'https://lite.ip2location.com/greece-ip-address-ranges',
            'https://lite.ip2location.com/greenland-ip-address-ranges',
            'https://lite.ip2location.com/grenada-ip-address-ranges',
            'https://lite.ip2location.com/guadeloupe-ip-address-ranges',
            'https://lite.ip2location.com/guam-ip-address-ranges',
            'https://lite.ip2location.com/guatemala-ip-address-ranges',
            'https://lite.ip2location.com/guernsey-ip-address-ranges',
            'https://lite.ip2location.com/guinea-ip-address-ranges',
            'https://lite.ip2location.com/guinea-bissau-ip-address-ranges',
            'https://lite.ip2location.com/guyana-ip-address-ranges',
            'https://lite.ip2location.com/haiti-ip-address-ranges',
            'https://lite.ip2location.com/holy-see-ip-address-ranges',
            'https://lite.ip2location.com/honduras-ip-address-ranges',
            'https://lite.ip2location.com/hong-kong-ip-address-ranges',
            'https://lite.ip2location.com/hungary-ip-address-ranges',
            'https://lite.ip2location.com/iceland-ip-address-ranges',
            'https://lite.ip2location.com/india-ip-address-ranges',
            'https://lite.ip2location.com/indonesia-ip-address-ranges',
            'https://lite.ip2location.com/iran-(islamic-republic-of)-ip-address-ranges',
            'https://lite.ip2location.com/iraq-ip-address-ranges',
            'https://lite.ip2location.com/ireland-ip-address-ranges',
            'https://lite.ip2location.com/isle-of-man-ip-address-ranges',
            'https://lite.ip2location.com/israel-ip-address-ranges',
            'https://lite.ip2location.com/italy-ip-address-ranges',
            'https://lite.ip2location.com/jamaica-ip-address-ranges',
            'https://lite.ip2location.com/japan-ip-address-ranges',
            'https://lite.ip2location.com/jersey-ip-address-ranges',
            'https://lite.ip2location.com/jordan-ip-address-ranges',
            'https://lite.ip2location.com/kazakhstan-ip-address-ranges',
            'https://lite.ip2location.com/kenya-ip-address-ranges',
            'https://lite.ip2location.com/kiribati-ip-address-ranges',
            'https://lite.ip2location.com/korea-(democratic-peoples-republic-of)-ip-address-ranges',
            'https://lite.ip2location.com/korea-(republic-of)-ip-address-ranges',
            'https://lite.ip2location.com/kuwait-ip-address-ranges',
            'https://lite.ip2location.com/kyrgyzstan-ip-address-ranges',
            'https://lite.ip2location.com/lao-peoples-democratic-republic-ip-address-ranges',
            'https://lite.ip2location.com/latvia-ip-address-ranges',
            'https://lite.ip2location.com/lebanon-ip-address-ranges',
            'https://lite.ip2location.com/lesotho-ip-address-ranges',
            'https://lite.ip2location.com/liberia-ip-address-ranges',
            'https://lite.ip2location.com/libya-ip-address-ranges',
            'https://lite.ip2location.com/liechtenstein-ip-address-ranges',
            'https://lite.ip2location.com/lithuania-ip-address-ranges',
            'https://lite.ip2location.com/luxembourg-ip-address-ranges',
            'https://lite.ip2location.com/macao-ip-address-ranges',
            'https://lite.ip2location.com/north-macedonia-ip-address-ranges',
            'https://lite.ip2location.com/madagascar-ip-address-ranges',
            'https://lite.ip2location.com/malawi-ip-address-ranges',
            'https://lite.ip2location.com/maldives-ip-address-ranges',
            'https://lite.ip2location.com/mali-ip-address-ranges',
            'https://lite.ip2location.com/marshall-islands-ip-address-ranges',
            'https://lite.ip2location.com/martinique-ip-address-ranges',
            'https://lite.ip2location.com/mauritius-ip-address-ranges',
            'https://lite.ip2location.com/mayotte-ip-address-ranges',
            'https://lite.ip2location.com/micronesia-(federated-states-of)-ip-address-ranges',
            'https://lite.ip2location.com/moldova-(republic-of)-ip-address-ranges',
            'https://lite.ip2location.com/mongolia-ip-address-ranges',
            'https://lite.ip2location.com/montenegro-ip-address-ranges',
            'https://lite.ip2location.com/morocco-ip-address-ranges',
            'https://lite.ip2location.com/mozambique-ip-address-ranges',
            'https://lite.ip2location.com/namibia-ip-address-ranges',
            'https://lite.ip2location.com/nauru-ip-address-ranges',
            'https://lite.ip2location.com/netherlands-ip-address-ranges',
            'https://lite.ip2location.com/new-caledonia-ip-address-ranges',
            'https://lite.ip2location.com/nicaragua-ip-address-ranges',
            'https://lite.ip2location.com/niger-ip-address-ranges',
            'https://lite.ip2location.com/niue-ip-address-ranges',
            'https://lite.ip2location.com/norfolk-island-ip-address-ranges',
            'https://lite.ip2location.com/norway-ip-address-ranges',
            'https://lite.ip2location.com/oman-ip-address-ranges',
            'https://lite.ip2location.com/palau-ip-address-ranges',
            'https://lite.ip2location.com/palestine-state-of-ip-address-ranges',
            'https://lite.ip2location.com/papua-new-guinea-ip-address-ranges',
            'https://lite.ip2location.com/paraguay-ip-address-ranges',
            'https://lite.ip2location.com/philippines-ip-address-ranges',
            'https://lite.ip2location.com/pitcairn-ip-address-ranges',
            'https://lite.ip2location.com/portugal-ip-address-ranges',
            'https://lite.ip2location.com/puerto-rico-ip-address-ranges',
            'https://lite.ip2location.com/reunion-ip-address-ranges',
            'https://lite.ip2location.com/romania-ip-address-ranges',
            'https://lite.ip2location.com/rwanda-ip-address-ranges',
            'https://lite.ip2location.com/saint-barthelemy-ip-address-ranges',
            'https://lite.ip2location.com/saint-kitts-and-nevis-ip-address-ranges',
            'https://lite.ip2location.com/saint-lucia-ip-address-ranges',
            'https://lite.ip2location.com/saint-pierre-and-miquelon-ip-address-ranges',
            'https://lite.ip2location.com/saint-vincent-and-the-grenadines-ip-address-ranges',
            'https://lite.ip2location.com/san-marino-ip-address-ranges',
            'https://lite.ip2location.com/sao-tome-and-principe-ip-address-ranges',
            'https://lite.ip2location.com/senegal-ip-address-ranges',
            'https://lite.ip2location.com/serbia-ip-address-ranges',
            'https://lite.ip2location.com/sierra-leone-ip-address-ranges',
            'https://lite.ip2location.com/singapore-ip-address-ranges',
            'https://lite.ip2location.com/slovakia-ip-address-ranges',
            'https://lite.ip2location.com/slovenia-ip-address-ranges',
            'https://lite.ip2location.com/somalia-ip-address-ranges',
            'https://lite.ip2location.com/south-africa-ip-address-ranges',
            'https://lite.ip2location.com/south-sudan-ip-address-ranges',
            'https://lite.ip2location.com/spain-ip-address-ranges',
            'https://lite.ip2location.com/sudan-ip-address-ranges',
            'https://lite.ip2location.com/suriname-ip-address-ranges',
            'https://lite.ip2location.com/eswatini-ip-address-ranges',
            'https://lite.ip2location.com/sweden-ip-address-ranges',
            'https://lite.ip2location.com/syrian-arab-republic-ip-address-ranges',
            'https://lite.ip2location.com/taiwan-(province-of-china)-ip-address-ranges',
            'https://lite.ip2location.com/tanzania-united-republic-of-ip-address-ranges',
            'https://lite.ip2location.com/thailand-ip-address-ranges',
            'https://lite.ip2location.com/togo-ip-address-ranges',
            'https://lite.ip2location.com/tokelau-ip-address-ranges',
            'https://lite.ip2location.com/trinidad-and-tobago-ip-address-ranges',
            'https://lite.ip2location.com/tunisia-ip-address-ranges',
            'https://lite.ip2location.com/turkmenistan-ip-address-ranges',
            'https://lite.ip2location.com/turks-and-caicos-islands-ip-address-ranges',
            'https://lite.ip2location.com/uganda-ip-address-ranges',
            'https://lite.ip2location.com/ukraine-ip-address-ranges',
            'https://lite.ip2location.com/united-kingdom-of-great-britain-and-northern-ireland-ip-address-ranges',
            'https://lite.ip2location.com/united-states-of-america-ip-address-ranges',
            'https://lite.ip2location.com/uruguay-ip-address-ranges',
            'https://lite.ip2location.com/uzbekistan-ip-address-ranges',
            'https://lite.ip2location.com/venezuela-(bolivarian-republic-of)-ip-address-ranges',
            'https://lite.ip2location.com/virgin-islands-(british)-ip-address-ranges',
            'https://lite.ip2location.com/virgin-islands-(u.s.)-ip-address-ranges',
            'https://lite.ip2location.com/yemen-ip-address-ranges',
            'https://lite.ip2location.com/zambia-ip-address-ranges']

    # create menu
    menu = {}
    for name, url in zip(names, urls):
        first_letter = name[0].upper()
        if first_letter not in menu:
            menu[first_letter] = []
        menu[first_letter].append((name, url))

    # start user interactive menu
    main_menu(menu)


if __name__ == "__main__":
    main()
