def read_company_names_produce_details() -> None:
    """Reads a file with company names, and then creates and writes to another
    file a few details of each company. The details it provides are the company's
    row in the file, the company's name, and its acronym.
    """
    companies = open("Companies.csv").read()
    company_file = open("company_file.csv", "w")
    company_list = companies.split("\n")
    count = 0
    cut_out = ["and", "if", "or", "at", "but", "for"]

    for company in company_list:
        if company == "":
            continue
        count += 1
        acronym = ""
        split_company = company.split()
        for word in split_company:
            if word not in cut_out:
                if len(split_company) >= 3:
                    acronym += word[0].upper()
                else:
                    if word == split_company[0]:
                        acronym += word[:2].upper()
                    else:
                        acronym += word[0].upper()

        total_list = [str(count), company, acronym, "\n"]
        new_total_list = ", ".join(total_list)
        company_file.write(new_total_list)

    company_file.close()


read_company_names_produce_details()