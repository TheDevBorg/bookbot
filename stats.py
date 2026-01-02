def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    text = text.lower()
    list_of_characters = set()
    for charater in text:
        list_of_characters.add(charater)
    character_count = {}
    for character in list_of_characters:
        character_count[character] = text.count(character)
    return character_count

def sort_on(items):
    return items[1]

def sort_character_count(characters):
    chart_list = []
    for character, count in characters.items():
        if not character.isalpha():
            continue
        chart_list.append((character, count))

    chart_list.sort(reverse=True, key=sort_on)
    return chart_list