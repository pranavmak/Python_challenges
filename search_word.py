def count_word_occurrences(filename, search_word):
    count = 0   # local variable

    with open(filename, "r") as file:
        for line in file:
            words = line.split()
            for word in words:
                if word.lower() == search_word.lower():
                    count += 1

    print(f"The word '{search_word}' appears {count} times.")


# -------- function call --------
file_name = "sample.txt"
word = "python"

count_word_occurrences(file_name, word)
