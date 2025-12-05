import csv
def main():
    PHONE_INDEX = 2
    dentists_dict = read_dictionary("dentists.csv", PHONE_INDEX)
    print(dentists_dict)
def read_dictionary(dentists, key_column_index):
    dictionary = {}
    with open("dentists.csv", "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list
    return dictionary

main()