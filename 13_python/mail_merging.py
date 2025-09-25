PLACEHOLDER = "[P_name]"

with open("./13_python/invitation_name.txt") as invitation_name:
    names = invitation_name.readlines()

with open("./13_python/Names.docx") as Names:
    letter_content = Names.read()

for person in names:
    person = person.strip()
    new_letter = letter_content.replace(PLACEHOLDER, person)
    print(new_letter)
    print("-" * 40)