from wav2vec_toolkit.utils import load_module_from_lang


def parameters(lang: str):
    _, parameters_cls = load_module_from_lang(lang)
    return parameters_cls
