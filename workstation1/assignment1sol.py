import re
# text = 'TTAATTTACTCACTGGCTA'
# dna_match = "AATTTAGGCTAAATTTAGGCTA"
# p = re.findall(r'AATTTA[ATCG]{1,10}GGCTA', dna_match)
# print(p)


def dna_match(s: str) -> bool:
    # check if the string contains valid letters
    if not set(s).issubset({"A", "C", "G", "T"}):
        return False
    dna_pattern = r"AATTTA[ACGT]{0,10}GGCTA"
    if "AATTTA" in s:
        result = s.count("AATTTA") == len(re.findall(dna_pattern, s))
        return bool(result)
    return True
    # return bool(re.findall(r'AATTTA[ATCG]{47}GGCTA', s))


# collect_email_from_text
# email_pattern = r"[\w\"\.\+-]+@[\w]+(?:[\.\"+-][\w]+)+"
# text = "__e--mail@123.123.123.123"
# email = re.findall(email_pattern, text)
# if email:
#     with open(doc: , mode='w') as d:
# regex pattern to find all valid emails
# email = r"[\w\"-+]+[\"+-.\w]*@[\w]+(?:[\.\"+-][\w]+)+"
# "’__e--mail@123.123.123.123’"
# '’"email"@domain.com’'
# '’john.doe+1@gmail.com’'
# '’jane@do-e.uk.com’'


def collect_email_from_text(text: str, filename: str) -> None:
    # regex pattern to find all valid emails
    email_pattern = r"[\w\"\.\+-]+@[\w]+(?:[\.\"+-][\w]+)+"
    emails = re.findall(email_pattern, text)
    # if atleast one email is found, open the output file in write mode
    if emails:
        with open(filename, 'w') as f:
            f.write(f"The number of emails extracted is {len(emails)}")
            for email in emails:
                f.write("\n" + email)
    else:
        with open(filename, 'w') as f:
            # if no emails are found, write only this line
            f.write("The number of emails extracted is 0")
