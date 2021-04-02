"""
Default text preprocessing for languages not defined in text_processing.lang
"""


def normalize(text, keep_apostrophes=False):
    text = text.lower()

    keep_chars = []

    if keep_apostrophes:
        # normalize apostrophes
        sent = text.replace("’", "'")
        keep_chars.append("'")

    # replace non-alpha characters with space
    sent = "".join(ch if ch.isalpha() or ch in keep_chars else " " for ch in text)

    # remove repeated spaces
    text = " ".join(sent.split())

    return text
