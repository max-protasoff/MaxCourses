import json


def menu():
    while True:
        command = input('''
Choose action:
0 - exit
1 - find a person name by a number of a document
2 - find on which shelf is your document by a document number
3 - show all documents
4 - add a new document
5 - delete a document
6 - move a document to another shelf
7 - add a new shelf
''')
        if command == '0':
            break
        elif command == '1':
            print("This document number belongs to:", person_by_docnum())
        elif command == '2':
            print(find_shelf_by_docnum())
        elif command == '3':
            show_all_docs()
        elif command == '4':
            add_document()
        elif command == '5':
            delete_doc()
        elif command == '6':
            move_doc_to_shelf()
        elif command == '7':
            add_shelf()






def person_by_docnum():
    try:
        docnum = input('Enter the number of a document: ')
    except Exception:
        print('Invalid input')

    with open('documents.json', 'r', encoding="UTF-8") as file:
        doc_dict = json.load(file)

    for item in doc_dict:
        if item.get("number")== docnum:
            return item.get("name")


def find_shelf_by_docnum():
    try:
        docnum = input('Enter the number of a document: ')
    except Exception:
        print('Invalid input')

    with open('directories.json', 'r', encoding="UTF-8") as file:
        directories_dict = json.load(file)

    for shelf, doc_list in directories_dict.items():
        if docnum in doc_list:
            return "This document is on a shelf N " + str(shelf)
    return "No such document found"

def show_all_docs():
    with open('documents.json', 'r', encoding="UTF-8") as file:
        doc_dict = json.load(file)
    for item in doc_dict:
        print("Document type is:", item["type"], "| document number is", item["number"], "| belongs to", item["name"])


def add_document():
    try:
        doc_type = input("Enter a document type: ")
        doc_num = input("Enter a document number: ")
        doc_person = input("Enter who does this document belongs to: ")
        doc_shelf = input("On which shelf do you want to put this document: ")
    except Exception:
        print("Invalid input")

    with open('directories.json', 'r', encoding="UTF-8") as file:
        directories_dict = json.load(file)

    if str(doc_shelf) in directories_dict.keys():
        directories_dict[str(doc_shelf)].append(str(doc_num))

        with open('directories.json', 'w', encoding="UTF-8") as file:
            json.dump(directories_dict, file, ensure_ascii=False, indent=4)

        with open('documents.json', 'r', encoding="UTF-8") as file:
            doc_list = json.load(file)
        doc_list.append({"type": doc_type, "number": doc_num, "name": doc_person})

        with open('documents.json', 'w', encoding="UTF-8") as file:
            json.dump(doc_list, file, ensure_ascii=False, indent=4)
        print('Document added on shelf N', doc_shelf)

    else:
        print('Something went wrong')


def delete_doc():
    doc_num = input("Enter document number: ")

    with open('directories.json', 'r', encoding="UTF-8") as file:
        directories_dict = json.load(file)

    for shelf, docs_on_shelf in directories_dict.items():
        if doc_num in docs_on_shelf:
            directories_dict[shelf].remove(doc_num)
            with open('directories.json', 'w', encoding="UTF-8") as file:
                json.dump(directories_dict, file, ensure_ascii=False, indent=4)

            with open('documents.json', 'r', encoding="UTF-8") as file:
                doc_list = json.load(file)

            for item in doc_list:
                if item["number"] == doc_num:
                    doc_list.remove(item)

            with open('documents.json', 'w', encoding="UTF-8") as file:
                json.dump(doc_list, file, ensure_ascii=False, indent=4)
            print('Document deleted')

        else:
            print("No such document found")


def move_doc_to_shelf():
    with open('directories.json', 'r', encoding="UTF-8") as file:
        directories_dict = json.load(file)

    doc_num = input("Enter document number: ")
    new_shelf = input("Enter a new shelf number: ")
    if new_shelf not in directories_dict.keys():
        print("No such shelf found")
    else:
        counter = 0
        for docs_on_shelf in directories_dict.values():
            if doc_num in docs_on_shelf:
                docs_on_shelf.remove(doc_num)

        directories_dict[new_shelf].append(doc_num)

        with open('directories.json', 'w', encoding="UTF-8") as file:
            json.dump(directories_dict, file, ensure_ascii=False, indent=4)

        print("Successfully moved document N", doc_num, "to shelf N", new_shelf)


def add_shelf():
    with open('directories.json', 'r', encoding="UTF-8") as file:
        directories_dict = json.load(file)

    print("You already have these shelves")
    for shelf in directories_dict.keys():
        print(shelf)
    new_shelf = input("Enter a number of a new shelf: ")

    if new_shelf in directories_dict.keys():
        print("Shelf with this number already exists")
    else:
        directories_dict[new_shelf] = []

        with open('directories.json', 'w', encoding="UTF-8") as file:
            json.dump(directories_dict, file, ensure_ascii=False, indent=4)

        print("Shelf successfully created")

menu()
