"""
This could be a unified WER eval function that takes a target language as an argument

E.g.

from wav2vec_toolkit.finetune import finetune
from wav2vec_toolkit.text_preprocessing.lang import fa

finetune(model="username/wav2vec-xlsr-fa",
         dataset="common_voice",
         split="test",
         language="fa",
         text_preprocessing=fa.normalize)
"""
