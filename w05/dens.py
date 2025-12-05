import csv
def main():
    dentists_list = read_compound_list("dentist.csv")
    print(dentists_list)
def read_compound_list(dentists):
    compound_list = []
    with open("dentists.csv", "rt") as csv_file:
        reader = csv.reader(csv_file)
        for row_list in reader:
            if len(row_list) != 0:
                compound_list.append(row_list)
    return compound_list

main()