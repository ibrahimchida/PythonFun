def read_company_names_produce_details() -> None:
    """Reads a file with company names, and then creates and writes to another
    file a few details of each company. The details it provides are the company's
    row in the file, the company's name, and its acronym. The acronym consists of the
    first letter of each word in the title, excluding the ones in the cut_out list.
    if the company name has 3 or more words, then the first letters are used. But if
    it has less then 3, then the first 2 letters of the first word in the title are
    used along with the first letter of the second word if there is one.
    """
    companies = open("Companies.csv").read()
    company_file = open("company_file.csv", "w")
    company_list = companies.split("\n")
    count = 0
    cut_out = ["and", "a", "at", "an", "for", "in", "to", "the"]   # list of words to exclude from capitalization.

    for company in company_list:
        if company == "":
            continue
        count += 1  # count increases for every company.
        acronym = ""
        split_company = company.split()      # splits company name into a list of words.
        for word in split_company:
            if word not in cut_out:  # checks if word is in the cut_out list.
                if len(split_company) >= 3:         # checks if company name has 3 or more words.
                    acronym += word[0].upper()  # concatenates the first letter of the word to the acronym string.
                else:
                    if word == split_company[0]:  # if the company name has less than 3 words, the program checks if
                        # the word being tested is the first one in the title.
                        acronym += word[:2].upper()           # if so, then the program concatenates the first 2
                        # letters of the first word to the acronym string.
                    else:
                        acronym += word[0].upper()  # if it's not, the program concatenates the fist letter of the
                        # word to the acronym string.

        total_list = [str(count), company, acronym]   # puts the stuff in one list
        new_total_list = ", ".join(total_list)
        company_file.write(f"{new_total_list} \n")  # writes to the new file.

    company_file.close()


read_company_names_produce_details()
