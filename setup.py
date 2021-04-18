import pathlib
from setuptools import find_packages, setup


INSTALL_REQ = [
    "datasets>=1.5.0",
    "transformers>=4.4.2",
    "torchaudio",
    "soundfile",
    "audiomentations",

    # language-specific packages
    # "hazm",  # Farsi
]


EXTRAS_REQ = {
    "dev": [
        "black",
        "isort",
        "flake8==3.7.9",
    ],
}

languages_packages = [
    "wav2vec_toolkit/{}".format(p).replace("/", ".")
    for p
    in pathlib.Path("languages").glob("**")
]

setup(
    name="wav2vec_toolkit",
    version="0.0.1",
    package_dir={
        "wav2vec_toolkit": "src/wav2vec_toolkit",
        "wav2vec_toolkit.languages": "languages"
    },
    packages=find_packages(where="src") + languages_packages,
    include_package_data=True,
    url="https://github.com/anton-l/wav2vec-toolkit",
    license="Apache 2.0",
    author="The HuggingFace community",
    author_email="",
    description="A collection of scripts to preprocess ASR datasets and finetune language-specific Wav2Vec2 XLSR models",
    install_requires=INSTALL_REQ,
    extras_require=EXTRAS_REQ,
)
