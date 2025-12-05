def main():
    text_list = read_list("provinces.txt")
    print(text_list)
    alberta_count = text_list.count("Alberta")
    print(f"Alberta appears {alberta_count} times")
def read_list(provinces):
    text_list = []
    with open("provinces.txt", "rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            clean_line = clean_line.replace("AB", "Alberta")
            text_list.append(clean_line)
            
    return text_list
main()