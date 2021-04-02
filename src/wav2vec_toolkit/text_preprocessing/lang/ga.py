def is_upper_vowel(letter):
    return letter in ['A', 'E', 'I', 'O', 'U', 'Á', 'É', 'Í', 'Ó', 'Ú']

def irish_lower_word(word):
    if len(word) > 1 and word[0] in ['n', 't'] and is_upper_vowel(word[1]):
        return word[0] + '-' + word[1:].lower()
    else:
        return word.lower()

def irish_lower(sentence):
    return " ".join([irish_lower_word(w) for w in sentence.split(" ")])

def remove_special_characters(text, chars_to_ignore_regex):
    text = text + ' '
    # ' and - are only significant inside a word
    text = text.replace('’', '\'')
	text = text.replace('\' ', ' ').replace(' \'', ' ')
	text = text.replace('- ', ' ').replace(' -', ' ')
    text = re.sub(chars_to_ignore_regex, "", text)
    return text

def normalize(text):
    chars_to_ignore_regex = r'[,\?\.\!\;\:\"\“\%\‘\”\(\)\*—–]'
    text = irish_lower(text)
    text = remove_special_characters(text, chars_to_ignore_regex)
    text = re.sub(" +", " ", text)
    text = text.strip() + " "

    return text
