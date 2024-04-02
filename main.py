def main():
    wc =  0
    chars = {}
    book = "books/frankenstein.txt"
    
    wc, chars = read_file(book)

    print_report(book, wc, chars)

def read_file(book):
    wc =  0
    chars = {}
    with open(f"./{book}") as f:
        content = f.read()
        wc = len(content.split())
        for c in content:
            c = c.lower()
            if c >= 'a' and c <= 'z':
                if c in chars:
                    chars[c] += 1
                else:
                    chars[c] = 0
    return wc, chars

def sort_on(dict):
    return dict["appearances"]

def print_report(book, wc, chars):
    print(f"--- Begin report of {book} ---")
    print(f"{wc} words found in the document\n")
    list_of_dicts = [{"char": char, "appearances": chars[char]} for char in chars]
    list_of_dicts.sort(reverse=True, key=sort_on)

    for dict in list_of_dicts:
        print(f"The '{dict['char']}' character was found {dict['appearances']} times")
    print("--- End report ---")

main()