import csv
from datetime import datetime #  # j

if __name__ == "__main__":
    # is required if this module would be run as a script, ie for testing purposes
    print "ali"

def csv2dict():
    # Reading the dictionary file into a CSV object and converting it to a dictionary
    with open("dutch.txt", "r") as csvfile:
        my_csv_file = csv.reader(csvfile)
        my_dict = {}
        for row in my_csv_file:
            my_dict[row[0]] = row[1:]
        print len(my_dict)

def how_many_to_test(a_dictionary):
    count = 0
    for key, value in a_dictionary.iteritems():
        date_object = datetime.strptime(value[1], "%Y-%m-%d")
        print (date_object - datetime.now()).days

def add_word(dict):
    word = raw_input("\nWord: ")
    if word in dict:
        print "\n" + word + " is already in the dictionary and means " + dict[word][0] + "\n"
    else:
        meaning = raw_input("\nMeaning: ")
        print " "
        creation = datetime.now().date()
        dict[word] = [meaning, creation, creation]

def lookup(dict):
    word = raw_input("\nWord to look up: ")
    if word in dict:
        print "\n" + word + " means " + dict[word][0] + "\n"
    else:
        print "\n" + word + " is not in the dictionary!\n"

def test():
    print "\nDon't know how to test your vocabulary!\n"
