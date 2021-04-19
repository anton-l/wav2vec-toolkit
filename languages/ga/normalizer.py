from typing import Any

from wav2vec_toolkit.text_preprocessing.normalizers import NormalizerOperation


def is_upper_vowel(letter):
    return letter in ["A", "E", "I", "O", "U", "Á", "É", "Í", "Ó", "Ú"]


def irish_lower_word(word):
    if len(word) > 1 and word[0] in ["n", "t"] and is_upper_vowel(word[1]):
        return word[0] + "-" + word[1:].lower()
    else:
        return word.lower()


class Normalizer(NormalizerOperation):
    _whitelist = r"[0-9a-záéíóú\-]+"
    _dictionary = {}
    _do_lowercase = False
    _text_key_name = "sentence"

    def text_level_normalizer(self, sentence: str, *args: Any, **kwargs: Any) -> str:
        text = super(Normalizer, self).text_level_normalizer(sentence, *args, **kwargs)
        text = " ".join([irish_lower_word(w) for w in text.split(" ")])
        return text
