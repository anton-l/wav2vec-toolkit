import os
import sys
import textwrap

import pkg_resources


BASE_PATH = "wav2vec_toolkit"
LANG_PATH = "languages"
LANG_MODULE_REQUIREMENTS = ["normalizer.py", "README.md", "requirements.txt"]


def get_file_path(name: str):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), name))


def parse_requirements(filename: str):
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


def load_module_from_lang(lang: str):
    lang_mod_path = f"{BASE_PATH}/{LANG_PATH}/{lang}"
    lang_path = "/".join(lang_mod_path.split("/")[-2:])
    for path in LANG_MODULE_REQUIREMENTS:
        _path = get_file_path(os.path.join(lang_path, path))
        if not os.path.exists(_path):
            raise FileNotFoundError(
                textwrap.dedent(
                    f"""
                    The filename {path} not existed in `{lang}` directory {_path},
                    you can easily add a new language by instructions mentioned at repo.
                    https://github.com/anton-l/wav2vec-toolkit/tree/master#adding-new-languages
                    """
                )
            )

    requirements_txt = get_file_path(os.path.join(lang_path, "requirements.txt"))
    dependencies = parse_requirements(requirements_txt)
    try:
        pkg_resources.require(dependencies)
    except pkg_resources.VersionConflict as error:
        print(
            textwrap.dedent(
                f"""
                {error.dist} is installed but {error.req} is required,
                fastest solution `pip install -r lang/{lang}/requirements.txt`,
                you can easily add a new language by instructions mentioned at repo.
                https://github.com/anton-l/wav2vec-toolkit/tree/master#adding-new-languages
                """
            )
        )
        raise

    except pkg_resources.DistributionNotFound as error:
        print(
            textwrap.dedent(
                f"""
                The '{error.req}' distribution was not found and is required by {error.requirers_str},
                fastest solution `pip install -r lang/{lang}/requirements.txt`,
                you can easily add a new language by instructions mentioned at repo.
                https://github.com/anton-l/wav2vec-toolkit/tree/master#adding-new-languages
                """
            )
        )
        raise

    try:
        module = __import__(lang_mod_path.replace("/", "."), fromlist=["Normalizer"])
    except ModuleNotFoundError:
        print(
            textwrap.dedent(
                f"""
                something wrong happened with your language {lang},
                you can easily add a new language by instructions mentioned at repo.
                https://github.com/anton-l/wav2vec-toolkit/tree/master#adding-new-languages
                """
            )
        )
        raise

    normalizer = module.Normalizer if getattr(module, "Normalizer") else None
    return normalizer
