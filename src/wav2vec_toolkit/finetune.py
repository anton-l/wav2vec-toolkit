"""
Main entrypoint for finetuning

It could be a function that wraps the huggingface Trainer and picks appropriate finetuning
parameters depending on the language

E.g.

from wav2vec_toolkit.finetune import finetune

finetune(base_model="facebook/wav2vec-xlsr", dataset="common_voice", language="fr", max_epochs=100)
"""

import os
from dataclasses import dataclass, field
from typing import Optional
from transformers import HfArgumentParser
import wandb


@dataclass
class FakeArguments:
    epochs: Optional[int] = field(
        default=1, metadata={"help": "Fake number of epochs"}
    )
    learning_rate: Optional[float] = field(
        default=0.001, metadata={"help": "Fake learning rate"}
    )
    dropout: Optional[float] = field(
        default=0.5, metadata={"help": "Fake learning rate"}
    output_dir: Optional[str]=field(
        default='', metadata={"help": "Fake output directory"}
    )

def main():
    parser=HfArgumentParser((FakeArguments,))

    # start a new run and log all args
    args=parser.parse_args()
    wandb.init(config=args, project='xlsr')

    # main loop
    fake_args, = parser.parse_args_into_dataclasses()
    import random, time
    time.sleep(5)
    test_wer=random.random()

    # logging will be automatically done by Trainer
    wandb.log({'test/wer': test_wer})

    # log model files as artifact
    artifact=wandb.Artifact(name=f"model-{wandb.run.id}", type="model", metadata={'wer': test_wer})
    for f in Path(training_args.output_dir).iterdir():
        if f.is_file():
            artifact.add_file(str(f))
    wandb.run.log_artifact(artifact)
