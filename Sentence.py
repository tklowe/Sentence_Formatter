def replace_words(sentence, replacements):
    for old_word, new_word in replacements.items():
        sentence = sentence.replace(old_word, new_word)
    return sentence

original_sentence = input("Enter a sentence: ")

replacements = {}
while True:
    old_word = input("Enter a word or phrase to replace (or press Enter to finish): ")
    if not old_word:
        break
    new_word = input(f"Enter the replacement for '{old_word}': ")
    replacements[old_word] = new_word

formatted_sentence = replace_words(original_sentence, replacements)
print("Formatted Sentence:")
print(formatted_sentence)
