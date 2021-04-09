CHARS_TO_IGNORE = [
    '،',
    '…',
    ',',
    '«',
    '(',
    '"',
    '؛',
    'ٔ',
    '""',
    '%',
    '_',
    '»',
    ';',
    ':',
    '؟',
    '”',
    '“',
    '.',
    '–',
    '-',
    '„',
    '�',
    '!',
    '‘',
    "'",
    '٬',
    ')',
    '?',
    "'ٔ",
    '#',
]
DICTIONARY = {
    "\u200c": " ",
    "\u200d": " ",
    "\u200e": " ",
    "\u200f": " ",
    "\ufeff": " ",
    "\u0307": " ",
}


def word_level_action(word):
    return word


def text_level_action(text):
    return text
