# Task 2

# Extend Phonebook application

# Functionality of Phonebook application:

# Add new entries 
# Search by first name 
# Search by last name 
# Search by full name
# Search by telephone number
# Search by city or state
# Delete a record for a given telephone number
# Update a record for a given telephone number #not working nd don't know how to make it work
# An option to exit the program #no need as it's all functions
 

# The first argument to the application should be the name of the phonebook. Application should load JSON data, if it is present in the folder with application, else raise an error. After the user exits, all data should be saved to loaded JSON.


import json
import sys
sys.path.append("/home/illia/Documents/python-basic1/homework_for_lesson_11")
print(sys.path)



def phonebook_open(phonebook):
    with open (phonebook, 'r') as file:
        f = json.load(file)
        print(f)


phonebook_open("homework_for_lesson_11/phonebook.json")


def new_entries(first_name, last_name, telephone_number, city, file_name):
    new_entry = {"first_name": first_name, "last_name": last_name, "telephone_number":telephone_number, "city":city}
    with open(file_name, "r+") as file:
        file_data = json.load(file)
        file_data.append(new_entry)
        json.dump(file_data, file)
        print(f"this is the file with new entries: {file_data}")

# new_entries("Petro", "Shevchenko", 255-356-1, "Zmerynka", "homework_for_lesson_11/phonebook.json")


def first_name_search(first_name, file_name):
    results = []
    try:
        with open (file_name, "r") as file:
            file_data = json.load(file)
        for entry in file_data:
            if entry["first_name"].lower() == first_name.lower():
                results.append(entry)
    except:
        FileNotFoundError("File wasn't found")

    print(results)


first_name_search("john", "homework_for_lesson_11/phonebook.json")

def last_name_search(last_name, file_name):
    results = []
    try:
        with open (file_name, "r") as file:
            file_data = json.load(file)
        for entry in file_data:
            if entry["last_name"].lower() == last_name.lower():
                results.append(entry)
    except:
        FileNotFoundError("File wasn't found")

    print(results)

last_name_search("Shevchenko", "homework_for_lesson_11/phonebook.json")


def phone_search(phone_number, file_name):
    results = []
    try:
        with open (file_name, "r") as file:
            file_data = json.load(file)
        for entry in file_data:
            if entry["telephone_number"] == phone_number:
                results.append(entry)
    except:
        FileNotFoundError("File wasn't found")

def city_search(city, file_name):
    results = []
    try:
        with open (file_name, "r") as file:
            file_data = json.load(file)
        for entry in file_data:
            if entry["city"].lower() == city.lower():
                results.append(entry)
    except:
        FileNotFoundError("File wasn't found")

def delete_by_number(number, file_name):
    with open(file_name, "r+") as file:
        file_data = json.load(file)
        for i in file_data:
            if i["telephone_number"] == number:
                deleted = i
                print(f'this was deleted {deleted}')
                i.clear()
        json.dump(file_data, file)


# def update_by_number(number, what_to_update, file_name):          
#     with open(file_name, "r+") as file:
#         file_data = json.load(file)
#         for i in file_data:
#             if i["telephone_number"] == number:
#                 i.update({what_to_update})
#                 print(i)
#         json.dump(file_data, file)

# # update_by_number(9876543210, {"city":"Rzhyshchiv"}, "homework_for_lesson_11/phonebook.json")