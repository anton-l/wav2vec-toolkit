from typing import Any
from wav2vec_toolkit.text_preprocessing.normalizers import NormalizerOperation


class Normalizer(NormalizerOperation):
    _whitelist = r"[0-9\w]+"
    _dictionary = {}
    _do_lowercase = True
    _text_key_name = "sentence"

    def text_level_normalizer(self, sentence: str, *args: Any, **kwargs: Any) -> str:
        text = super().text_level_normalizer(sentence, *args, **kwargs)

        # DO OTHER OPERATIONS REGARDING YOURS, COMES HERE
        # text = ...

        return text