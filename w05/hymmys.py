import csv
def main():
    with open("hymns.csv", "rt") as csv_file:
        reader = csv.reader(csv_file)

        for row_list in reader:
            print(row_list)

main()