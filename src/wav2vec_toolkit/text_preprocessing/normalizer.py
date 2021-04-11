import re
import textwrap
from typing import Any, Dict

from wav2vec_toolkit.utils import load_module_from_lang


class NormalizerOperation:
    """A general normalizer for every language"""

    _whitelist = r"\w+"
    _dictionary = {}

    def __init__(
        self,
        text_key_name: str = "sentence",
        whitelist: str = None,
        dictionary: Dict[str, str] = None,
        do_lowercase: bool = True,
        do_text_normalization: bool = True,
        do_lastspace_removing: bool = True,
    ) -> None:
        self.text_key_name = text_key_name
        self.whitelist = whitelist if whitelist and isinstance(whitelist, str) else self._whitelist
        self.dictionary = dictionary if dictionary and isinstance(dictionary, dict) else self._dictionary
        self.do_lowercase = do_lowercase
        self.do_text_normalization = do_text_normalization
        self.do_lastspace_removing = do_lastspace_removing

    def chars_to_map(self, sentence: str) -> str:
        """Maps every character, words, and phrase into a proper one.

        Args:
            sentence (str): A piece of text.
        """
        if not len(self.dictionary) > 0:
            return sentence

        pattern = "|".join(map(re.escape, self.dictionary.keys()))
        return re.sub(pattern, lambda m: self.dictionary[m.group()], str(sentence))

    def chars_to_preserve(
        self,
        sentence: str,
    ) -> str:
        """Keeps specified characters from sentence

        Args:
            sentence (str): A piece of text.
        """
        try:
            tokenized = re.findall(self.whitelist, sentence, re.IGNORECASE)
            return " ".join(tokenized)
        except Exception as error:
            print(
                textwrap.dedent(
                    f"""
                    Bad characters range {self.whitelist},
                    {error}
                    """
                )
            )
            exit()

    def text_level_normalizer(self, sentence: str, *args: Any, **kwargs: Any) -> str:
        """A text level of normalization.
        It is handy for some languages that need to add a hierarchy of
        normalization and filtering at the text level.

        Args:
            sentence (str): A piece of text.
        """
        text = sentence
        return text

    def __call__(self, batch: Dict, return_dict: bool = True, *args: Any, **kwargs: Any) -> Any:
        """Normalization caller

        Args:
            batch (Dict): A batch of input.
            return_dict (bool, optional): Whether to return dictionary of batch or not just the text. Defaults to True.. Defaults to True.
        """

        if self.text_key_name not in batch:
            raise KeyError(
                textwrap.dedent(
                    f"""
                    keyname {self.text_key_name} not existed in the batch dictionary,
                    the batch dictionary consists of the following keys {list(batch.keys())},
                    you can easily add a new keyname by passing the `text_key_name` into Normalizer.
                    """
                )
            )

        text = batch[self.text_key_name].strip()
        text = self.chars_to_map(text)
        text = self.chars_to_preserve(text)

        if self.do_text_normalization:
            text = self.text_level_normalizer(text, *args, **kwargs)

        text = text.strip()
        if not self.do_lastspace_removing:
            text = text + " "

        if not return_dict:
            return text

        batch[self.text_key_name] = text
        return batch


def normalizers(lang: str):
    normalizer_cls, _ = load_module_from_lang(lang)
    return normalizer_cls
