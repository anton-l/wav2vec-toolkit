"""
Main entrypoint for finetuning

It could be a function that wraps the huggingface Trainer and picks appropriate finetuning
parameters depending on the language

E.g.

from wav2vec_toolkit.finetune import finetune

finetune(base_model="facebook/wav2vec-xlsr", dataset="common_voice", language="fr", max_epochs=100)
"""
