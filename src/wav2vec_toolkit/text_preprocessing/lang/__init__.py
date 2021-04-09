from wav2vec_toolkit.text_preprocessing.lang import (
    default,
    et,
    fa,
    ka,
    lt,
)

LANGUAGES = {
    "default": {
        "chars_to_ignore": default.CHARS_TO_IGNORE,
        "dictionary": default.DICTIONARY,
        "word_level_action": default.word_level_action,
        "text_level_action": default.text_level_action,
    },
    "et": {
        "chars_to_ignore": et.CHARS_TO_IGNORE,
        "dictionary": et.DICTIONARY,
        "word_level_action": et.word_level_action,
        "text_level_action": et.text_level_action,
    },
    "fa": {
        "chars_to_ignore": fa.CHARS_TO_IGNORE,
        "dictionary": fa.DICTIONARY,
        "word_level_action": fa.word_level_action,
        "text_level_action": fa.text_level_action,
    },
    "ka": {
        "chars_to_ignore": ka.CHARS_TO_IGNORE,
        "dictionary": ka.DICTIONARY,
        "word_level_action": ka.word_level_action,
        "text_level_action": ka.text_level_action,
    },
    "lt": {
        "chars_to_ignore": lt.CHARS_TO_IGNORE,
        "dictionary": lt.DICTIONARY,
        "word_level_action": lt.word_level_action,
        "text_level_action": lt.text_level_action,
    },
}
