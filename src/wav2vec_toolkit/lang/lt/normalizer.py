from typing import Any

from wav2vec_toolkit.text_preprocessing.normalizer import NormalizerOperation


class Normalizer(NormalizerOperation):
    _whitelist = r"[0-9a-ząčęėįšųūž\-]+"
    _dictionary = {}
