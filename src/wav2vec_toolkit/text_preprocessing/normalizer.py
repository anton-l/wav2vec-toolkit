import re
import string
from typing import Callable, List, Dict, Optional

from wav2vec_toolkit.text_preprocessing.lang import LANGUAGES


def chars_to_map(
    sentence: str,
    dictionary: Dict[str, str] = {}
) -> str:
    """Maps every character, words, and phrase into a proper one.

    Args:
        sentence (str): A piece of text.
        dictionary (dict, optional): A dictionary of chars, words, and phrase that your want to alter in the sentence.. Defaults to {}.

    Returns:
        str: [description]
    """
    pattern = "|".join(map(re.escape, dictionary.keys()))
    return re.sub(pattern, lambda m: dictionary[m.group()], str(sentence))


def chars_to_remove(
    sentence: str,
    chars_to_ignore_regex: str
) -> str:
    """Filters out specified characters from sentence

    Args:
        sentence (str): A piece of text.
        chars_to_ignore_regex (str): A regex of chars that you want to filter out from the sentence.

    Returns:
        str: The correct and meaningful sentence
    """
    sentence = re.sub(chars_to_ignore_regex, "", sentence).lower()
    return sentence


def word_level_normalizer(
    sentence: str,
    fn_callback=None
) -> str:
    """A world level of normalization using an external callback.

    It is handy for some languages that need to add a hierarchy of 
        normalization and filtering at the word level.

    Args:
        sentence (str): A piece of text.
        fn_callback (Callable[[str], str], optional): A word level callback function. Defaults to None.

    Returns:
        str: The correct and meaningful sentence
    """
    words = sentence.split(" ")
    normalized_words = []

    for word in words:
        if callable(fn_callback):
            word = fn_callback(word)
        normalized_words.append(word)

    return " ".join(normalized_words)


def text_level_normalizer(
    text: str,
    fn_callback=None
) -> str:
    """A text level of normalization using an external callback.

    It is handy for some languages that need to add a hierarchy of 
        normalization and filtering at the text level.

    Args:
        text (str): A piece of text.
        fn_callback (Callable, optional): A text level callback function. Defaults to None.

    Returns:
        str: The correct and meaningful sentence
    """
    if callable(fn_callback):
        text = fn_callback(text)

    return text


def normalizer(
    batch: Dict,
    lang: str = "default",
    text_normalizer: bool = True,
    word_normalizer: bool = True,
    lower_normalizer: bool = True,
    return_dict: bool = True,
    remove_extra_space: bool = True,
    remove_last_space: bool = True,
    text_key: str = "sentence",
    dictionary: Dict[str, str] = None,
    chars_to_ignore: List[str] = None,
    word_level_action=None,
    text_level_action=None,
):
    """A general normalizer for every language

    Args:
        batch (Dict): A batch of input.
        lang (str, optional): Your dataset language. Defaults to "default".
        text_normalizer (bool, optional): Whether to use a text normalizer or not. Defaults to True.
        word_normalizer (bool, optional): Whether to use a word normalizer or not. Defaults to True.
        lower_normalizer (bool, optional): Whether to make lowercase a text or not. Defaults to True.
        return_dict (bool, optional): Whether to return dictionary of batch or not just the text. Defaults to True.
        remove_extra_space (bool, optional): Whether to remove extra spaces or not. Defaults to True.
        remove_last_space (bool, optional): Whether to add an extra space at the end or not. Defaults to True.
        text_key (str, optional): Get the key name for text in the batch. Defaults to "sentence".
        dictionary (Dict[str, str], optional): A dictionary of chars, words, phrase to map. Defaults to None.
        chars_to_ignore (List[str], optional): A list of chars to filter out. Defaults to None.
        word_level_action (Callable, optional): A callback function for word level normalization. Defaults to None.
        text_level_action (Callable, optional): A callback function for text level normalization. Defaults to None.
    """

    lang = LANGUAGES[lang] if lang in LANGUAGES else LANGUAGES["default"]

    if not chars_to_ignore or not isinstance(chars_to_ignore, list):
        chars_to_ignore = lang["chars_to_ignore"]

    if not dictionary or not isinstance(dictionary, dict):
        dictionary = lang["dictionary"]

    if not text_level_action or not callable(text_level_action):
        text_level_action = lang["text_level_action"]

    if not word_level_action or not callable(word_level_action):
        word_level_action = lang["word_level_action"]

    text = batch[text_key].strip()

    if lower_normalizer:
        text = text.lower()

    # Dictionary mapping
    if len(dictionary) > 0:
        text = chars_to_map(text, dictionary)

    # Remove specials
    if len(chars_to_ignore) > 0:
        chars_to_ignore = f"""[{"".join(chars_to_ignore)}]"""
        text = chars_to_remove(text, chars_to_ignore)

    if text_normalizer:
        text = text_level_normalizer(text, text_level_action)

    if word_normalizer:
        text = word_level_normalizer(text, word_level_action)

    # Remove extra spaces
    if remove_extra_space:
        text = re.sub(" +", " ", text)

    if remove_last_space:
        text = text.strip()
    else:
        text = text.strip() + " "

    if not return_dict:
        return text

    batch[text_key] = text
    return batch
