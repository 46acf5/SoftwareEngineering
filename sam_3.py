def file_statistics(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    num_lines = len(lines)
    num_letters = 0
    num_words = 0

    for line in lines:
        words = line.split()
        num_words += len(words)
        num_letters += sum(c.isalpha() for c in line)

    print(f"Input file contains:")
    print(f"{num_letters} letters")
    print(f"{num_words} words")
    print(f"{num_lines} lines")


file_statistics('input.txt')
