# Add new language

If you want to add a new language, you just need to create a folder with the iso code of your language (for example, `ru`), and the folder must consist of the following files:

```bash
languages
├── ru
│   ├── README.md
│   ├── __init__.py
│   ├── normalizer.py
│   └── requirements.txt
```

Or you can just use our template as below:
```bash
mkdir languages/{YOUR_ISO_CODE_LANGUAGE}
cp templates/language/* languages/{YOUR_ISO_CODE_LANGUAGE}
```

The `__init__.py` have to import your normalizer as below:

```python
from .normalizer import Normalizer
```

The `normalizer.py` consists of the normalization procedure related to your specific language.

- `_whitelist`: The acceptable characters related to your language.
- `_dictionary`: A dictionary of words, characters, or phrases that you want to find and replace before whitelisting.
- `_do_lowercase`: Whether to do lowercase or not.
- `_text_key_name`: The key name of text in the batch input related to `load_dataset` architecture of your audio dataset.
- `text_level_normalizer()`: A method to add some extra normalization operations at the text level of your language. For example, a spelling correction.

```python
from spellchecker import SpellChecker
from typing import Any
from wav2vec_toolkit.text_preprocessing.normalizers import NormalizerOperation


russian = SpellChecker(language='ru')

class Normalizer(NormalizerOperation):
    _whitelist = r"[0-9шиюынжсяплзухтвкйеобмцьёгдщэарчфъ\-]+"
    _dictionary = {}
    _do_lowercase = True
    _text_key_name = "sentence"
    def text_level_normalizer(self, sentence: str, *args: Any, **kwargs: Any) -> str:
        text = super(Normalizer, self).text_level_normalizer(sentence, *args, **kwargs)
        
        # DO OTHER OPERATIONS REGARDING YOURS, COMES HERE
        words = text.split()
        new_text = []
        for word in words:
            misspelled = spell.unknown([word])
            if misspelled != set():
                new_text.append(spell.correction(word))
            else:
                new_text.append(word)

        text = " ".join(new_text)
        return text
```

If you need to use extra libraries or packages regarding your normalization, you must fill in these requirements in the `requirements.txt`. For instance:

```text
pyspellchecker==0.6.2
```