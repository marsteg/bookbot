print("hello world")

def print_book():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def count_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        return len(words)
    
def count_characters():
    with open("books/frankenstein.txt") as f:
        letters_count = {}
        file_contents = f.read()
        lower_case = file_contents.lower()
        # for each letter in the alphabet i want to count how many times it appears in the text
        for letter in lower_case:
            if letter.isalpha() == True:
                if letter in letters_count:
                    letters_count[letter] += 1
                else:
                    letters_count[letter] = 1
        return letters_count

def sort_on(dict):
    return dict["num"]

def main():
   # print_book()
    
    print("--- Begin report of books/frankenstein.txt ---")
    print("Number of words: ", count_words())
    chars = count_characters()
    lchars = []
    for k, v in chars.items():
        lchars.append({"char": k, "num": v})

    lchars.sort(reverse=True, key=sort_on)
    for item in lchars:
        print(item["char"], item["num"])

    print("--- End report ---")

main()