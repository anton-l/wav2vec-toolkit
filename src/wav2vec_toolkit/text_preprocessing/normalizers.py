import re
import sys
import textwrap
from typing import Any, Dict, Optional

from wav2vec_toolkit.utils import load_module_from_lang


class NormalizerOperation:
    """A general normalizer for every language"""

    _whitelist = r"\w+"
    _dictionary = {}
    _text_key_name: str = "sentence"
    _do_lowercase: bool = True

    def __init__(
        self,
        whitelist: str = None,
        dictionary: Dict[str, str] = None,
    ) -> None:
        self.text_key_name = self._text_key_name
        self.whitelist = whitelist if whitelist and isinstance(whitelist, str) else self._whitelist
        self.dictionary = dictionary if dictionary and isinstance(dictionary, dict) else self._dictionary
        self.do_lowercase = self._do_lowercase

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
            raise

    def text_level_normalizer(self, sentence: str, *args: Any, **kwargs: Any) -> str:
        """A text level of normalization.
        It is handy for some languages that need to add a hierarchy of
        normalization and filtering at the text level.

        Args:
            sentence (str): A piece of text.
        """
        text = sentence
        return text

    def __call__(
        self,
        batch: Dict,
        return_dict: bool = True,
        do_lastspace_removing: bool = True,
        text_key_name: Optional[str] = None,
        do_lowercase: Optional[bool] = None,
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        """Normalization caller

        Args:
            batch (Dict): A batch of input.
            text_key_name (str, optional): The key name of text in the batch input.
            return_dict (bool, optional): Whether to return dictionary of batch or not just the text. Defaults to True.
            do_lastspace_removing (bool, optional): Whether to add extra space at the end of text or not. Defaults to True.
            do_lowercase (bool, optional): Whether to do lowercase or not. Defaults to None.
        """

        text_key_name = text_key_name if text_key_name else self.text_key_name
        do_lowercase = do_lowercase if isinstance(do_lowercase, bool) else self.do_lowercase

        if text_key_name not in batch:
            raise KeyError(
                textwrap.dedent(
                    f"""
                    keyname {text_key_name} not existed in the batch dictionary,
                    the batch dictionary consists of the following keys {list(batch.keys())},
                    you can easily add a new keyname by passing the `text_key_name` into Normalizer.
                    """
                )
            )

        text = batch[text_key_name].strip()

        if do_lowercase:
            text = text.lower()

        text = self.chars_to_map(text)
        text = self.chars_to_preserve(text)
        text = self.text_level_normalizer(text, *args, **kwargs)

        text = text.strip()
        if not do_lastspace_removing:
            text = text + " "

        if not return_dict:
            return text

        batch[text_key_name] = text
        return batch


def normalizers(lang: str) -> NormalizerOperation:

    _normalizer = load_module_from_lang(lang)()
    return _normalizer
