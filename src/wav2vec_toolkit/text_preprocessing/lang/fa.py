"""
Credit: m3hrdadfi
https://huggingface.co/m3hrdadfi/wav2vec2-large-xlsr-persian-v2
"""

import re
import string

import hazm


_normalizer = hazm.Normalizer()


chars_to_ignore = [
    ",",
    "?",
    ".",
    "!",
    "-",
    ";",
    ":",
    '""',
    "%",
    "'",
    '"',
    "�",
    "#",
    "!",
    "؟",
    "?",
    "«",
    "»",
    "،",
    "(",
    ")",
    "؛",
    "'ٔ",
    "٬",
    "ٔ",
    ",",
    "?",
    ".",
    "!",
    "-",
    ";",
    ":",
    '"',
    "“",
    "%",
    "‘",
    "”",
    "�",
    "–",
    "…",
    "_",
    "”",
    "“",
    "„",
    "ā",
    "š",
    # "ء",
]

# In case of farsi
chars_to_ignore = chars_to_ignore + list(string.ascii_lowercase + string.digits)

chars_to_mapping = {
    "ك": "ک",
    "دِ": "د",
    "بِ": "ب",
    "زِ": "ز",
    "ذِ": "ذ",
    "شِ": "ش",
    "سِ": "س",
    "ى": "ی",
    "ي": "ی",
    "أ": "ا",
    "ؤ": "و",
    "ے": "ی",
    "ۀ": "ه",
    "ﭘ": "پ",
    "ﮐ": "ک",
    "ﯽ": "ی",
    "ﺎ": "ا",
    "ﺑ": "ب",
    "ﺘ": "ت",
    "ﺧ": "خ",
    "ﺩ": "د",
    "ﺱ": "س",
    "ﻀ": "ض",
    "ﻌ": "ع",
    "ﻟ": "ل",
    "ﻡ": "م",
    "ﻢ": "م",
    "ﻪ": "ه",
    "ﻮ": "و",
    "ﺍ": "ا",
    "ة": "ه",
    "ﯾ": "ی",
    "ﯿ": "ی",
    "ﺒ": "ب",
    "ﺖ": "ت",
    "ﺪ": "د",
    "ﺮ": "ر",
    "ﺴ": "س",
    "ﺷ": "ش",
    "ﺸ": "ش",
    "ﻋ": "ع",
    "ﻤ": "م",
    "ﻥ": "ن",
    "ﻧ": "ن",
    "ﻭ": "و",
    "ﺭ": "ر",
    "ﮔ": "گ",
    # "ها": "  ها", "ئ": "ی",
    "a": " ای ",
    "b": " بی ",
    "c": " سی ",
    "d": " دی ",
    "e": " ایی ",
    "f": " اف ",
    "g": " جی ",
    "h": " اچ ",
    "i": " آی ",
    "j": " جی ",
    "k": " کی ",
    "l": " ال ",
    "m": " ام ",
    "n": " ان ",
    "o": " او ",
    "p": " پی ",
    "q": " کیو ",
    "r": " آر ",
    "s": " اس ",
    "t": " تی ",
    "u": " یو ",
    "v": " وی ",
    "w": " دبلیو ",
    "x": " اکس ",
    "y": " وای ",
    "z": " زد ",
    "\u200c": " ",
    "\u200d": " ",
    "\u200e": " ",
    "\u200f": " ",
    "\ufeff": " ",
}


def multiple_replace(text, chars_to_mapping):
    pattern = "|".join(map(re.escape, chars_to_mapping.keys()))
    return re.sub(pattern, lambda m: chars_to_mapping[m.group()], str(text))


def remove_special_characters(text, chars_to_ignore_regex):
    text = re.sub(chars_to_ignore_regex, "", text).lower() + " "
    return text


def normalize(text):
    chars_to_ignore_regex = f"""[{"".join(chars_to_ignore)}]"""
    text = text.lower().strip()

    text = _normalizer.normalize(text)
    text = multiple_replace(text, chars_to_mapping)
    text = remove_special_characters(text, chars_to_ignore_regex)
    text = re.sub(" +", " ", text)
    text = text.strip() + " "

    return text
