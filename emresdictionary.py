from shutil import copy2 # The shutil module offers a number of high-level operations on files and collections of files.
import csv
import dict_funcs

# Creating a backup for the "dictionary file".
copy2("dutch.txt", "bakcup_dutch.txt")


# Reading the dictionary file into a CSV object and converting it to a dictionary
with open("dutch.txt", "r") as csvfile:
    my_csv_file = csv.reader(csvfile)
    my_dict = {}
    for row in my_csv_file:
        my_dict[row[0]] = row[1:]
    print "\nThere are " + str(len(my_dict)) + " words in the dictionary.\n"

# A simple menu for navigating.
menu = {}
menu['1']="Add word"
menu['2']="Lookup word"
menu['3']="Test"
menu['4']="Exit"
while True:
    options=menu.keys()
    options.sort()
    for entry in options:
        print entry, menu[entry]

    selection=raw_input("\nPlease Select : ")
    if selection =='1':
      dict_funcs.add_word(my_dict)
    elif selection == '2':
      dict_funcs.lookup(my_dict)
    elif selection == '3':
      dict_funcs.test()
    elif selection == '4':
        with open("dutch.txt", "wb") as csvfile:
            spamwriter = csv.writer(csvfile)
            for key in my_dict:
                spamwriter.writerow([key, my_dict[key][0], my_dict[key][1], my_dict[key][2]])
        break
    else:
      print "\nUnknown Option Selected!\n"



"""
with open('eggs.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam']) IJSTHEE
"""
# my_dict = csv.reader(csvfile, delimiter=' ', quotechar='|')






