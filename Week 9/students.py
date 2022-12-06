import csv
csv_list = "students.csv"
def read_dict(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.
    students = open("students.csv", "r")
    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    with open(filename, 'r') as students:
        group = csv.reader(students)
        processed = {}
        for row in group:
            processed["student"] = row
        print(processed)

read_dict(csv_list)