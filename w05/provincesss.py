def main():
    text_list = read_list("provinces.txt")
    print(text_list)
def read_list(provinces):
    text_list = []

    with open(provinces, "rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)
    return text_list

main()