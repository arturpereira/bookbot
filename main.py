def main():
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---")
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    print(f"{word_count} words were found in the document.\n")
    character_count = get_character_count(text)
    sorted_character_count = {k: v for k, v in sorted(character_count.items(), key=lambda x: x[1], reverse=True)}
    for k, v in sorted_character_count.items():
        print(f"The '{k}' character was found {v} times")
    print("--- End report ---")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    character_count = {}
    text_lower = text.lower()
    for c in text_lower:
        if c.isalpha():
            character_count[c] = character_count.get(c, 0) + 1
    return character_count
    
    
main()