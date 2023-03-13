import re

from pprint import pprint

import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  contacts_dict = {}

for contact_list in contacts_list:
    edit_num = r"+7(\2)\3-\4-\5 \6"
    contact_list[5] = re.sub(r'(\+*?[78])[ ]*?\(?(\d\d\d)\)*?[\s-]*?(\d\d\d)-*?(\d\d)-*?(\d\d)[\s\(]*(доб. \d\d\d\d)*[\)]?', edit_num, contact_list[5])
    fio = ' '.join(contact_list[:3]).split()
    contact_list[:len(fio)] = fio
    name_surname = ' '.join(contact_list[:2])
    if contacts_dict.get(name_surname):
        contacts_dict[name_surname] = [
            contacts_dict[name_surname][i] if contacts_dict[name_surname][i]
            else contact_list[i] for i in range(7)
        ]

    else:
        contacts_dict[name_surname] = contact_list
contacts_list = list(contacts_dict.values())
pprint(contacts_list)

with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')

    datawriter.writerows(contacts_list)