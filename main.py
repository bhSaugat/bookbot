from stats import get_book_text, occurences, listed_chars, sort_on
import sys
def main():
  if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
  else:
       book_path = sys.argv[1]
  char_list = listed_chars(occurences(book_path))
  char_list.sort(reverse=True, key=sort_on)
  print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...\n----------- Word Count ----------\nFound {get_book_text(book_path)} total words\n--------- Character Count -------")
  for char in char_list:
    print(f"{char["char"]}: {char["num"]}")
    

main()