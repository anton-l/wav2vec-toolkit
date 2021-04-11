from typing import Any

import hazm

from wav2vec_toolkit.text_preprocessing.normalizer import NormalizerOperation


normalizer = hazm.Normalizer()


class Normalizer(NormalizerOperation):
    _whitelist = r"[0-9a-Z۰۱۲۳۴۵۶۷۸۹ءآئابتثجحخدذرزسشصضطظعغفقلمنهوپچژکگیە\-\u200c]+"
    _dictionary = {
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
        "\u200d": " ",
        "\u200e": " ",
        "\u200f": " ",
        "\ufeff": " ",
    }

    def text_level_normalizer(self, sentence: str, *args: Any, **kwargs: Any) -> str:
        text = super(Normalizer, self).text_level_normalizer(sentence, *args, **kwargs)
        text = normalizer.normalize(text)
        return text
