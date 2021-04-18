from typing import Any

from wav2vec_toolkit.text_preprocessing.normalizers import NormalizerOperation


class Normalizer(NormalizerOperation):
    _whitelist = r"[0-9a-z\-]+"
    _dictionary = {}
    _do_lowercase = True
    _text_key_name = "sentence"
