import sys
from stats import count_word, count_letters, pretty_report
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    
    if len(sys.argv) == 2:
        book = get_book_text(sys.argv[1])
        wordcount = count_word(book)
        word_output = f"Found {wordcount} total words"
        count_letters_var = count_letters(book)
        pretty_report_var = pretty_report(count_letters_var)
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(word_output)
        print("--------- Character Count -------")
        for letter in pretty_report_var:
            if letter["char"].isalpha():
                a_out = letter["char"]
                b_out = letter["num"]
                print(f"{a_out}: {b_out}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    
main()
