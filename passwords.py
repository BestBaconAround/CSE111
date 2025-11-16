def word_in_file(word, filename, case_sensitive=False):
    with open(filename, "r", encoding="UTF-8") as file:
        words = file.read().splitlines()

    if not case_sensitive:
        word = word.lower()
        words = [w.lower() for w in words]

    return word in words


def word_has_character(word, character_list):
    for char in word:
        if char in character_list:
            return True
    return False


def word_complexity(word):
    LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    DIGITS=["0","1","2","3","4","5","6","7","8","9"]
    SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]
    

    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1

    return complexity


def password_strength(password, min_length=10, strong_length=16):
    if word_in_file(password, "dictionary.txt"):
        print("Password is a dictionary word. Strength: 0")
        return 0

    if word_in_file(password, "top_passwords.txt"):
        print("Password is in the top password list. Strength: 0")
        return 0

    length = len(password)

    if length < min_length:
        print("Password is too short. Strength: 1")
        return 1

    complexity = word_complexity(password)
    strength = 1 + complexity

    if length >= strong_length:
        print("Password is very strong due to its length. Strength: 5")
        strength = 5
    else:
        print(f"Password length is acceptable ({length} characters).")

    if strength > 5:
        strength = 5

    print(f"Password complexity score: {complexity}")
    print(f"Final password strength: {strength}")
    return strength


def main():
    while True:
        password = input("Enter a password to test (Q to quit): ")
        if password.lower() == "q":
            print("Goodbye.")
            break

        strength = password_strength(password)
        print(f"Password strength: {strength}/5\n")


if __name__ == "__main__":
    main()
