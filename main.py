from stats import num_of_words
from stats import num_of_char
from stats import sorted_list
import sys

c = 0
for r in sys.argv:
    c += 1
if c != 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
	with open(file_path) as f:
		file_contents = f.read()
	return file_contents


def main():
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    words = num_of_words(text)
    chars = num_of_char(text)
    sorted_char = sorted_list(chars)
    print(
         f"""============ BOOKBOT ============\n
Analyzing book found at {file_path}...
----------- Word Count ----------
Found {words} total words
--------- Character Count ------""")
    for r in sorted_char:
        if r["char"].isalpha():
            print(f"{r['char']}: {r['num']}")
    

    print("============= END ===============")

main()

