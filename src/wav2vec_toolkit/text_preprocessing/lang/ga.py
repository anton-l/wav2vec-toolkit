CHARS_TO_IGNORE = [
    ',',
    '?',
    '.',
    '!',
    ';',
    ':',
    '"',
    '“',
    '%',
    '‘',
    '”',
    '(',
    ')',
    '*',
    '—',
    '–',
]
DICTIONARY = {
    "\u0307": " ",
}


def is_upper_vowel(letter):
    return letter in ['A', 'E', 'I', 'O', 'U', 'Á', 'É', 'Í', 'Ó', 'Ú']


def word_level_action(word):
    if len(word) > 1 and word[0] in ['n', 't'] and is_upper_vowel(word[1]):
        return word[0] + '-' + word[1:].lower()
    else:
        return word.lower()


def text_level_action(text):
    return text
