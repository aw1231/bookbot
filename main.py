def main():
    input = "books/frankenstein.txt"
    with open(input) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        character_count = count_characters(file_contents)
        print(f"--- Begin report of {input} ---")
        print(f"{word_count} words found in the document")
        print()
        for character in character_count:
            print(f'The \"{character["letter"]}\" character was found {character["count"]} times')
        print("--- End report ---")
def count_words(input):
    words = input.split()
    return len(words)
def sort_on(dict):
    return dict["count"]
def count_characters(input):
    lowered_input = input.lower()
    input_list = []
    for character in lowered_input:
        input_list.append(character)
    input_dict = {}
    for character in input_list:
        if character not in input_dict and character.isalpha():
            input_dict[character] = 1
        elif character.isalpha():
            input_dict[character] += 1
    dict_list = []
    for character in input_dict:
        dict_list.append({"letter": character, "count": input_dict[character]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
main()