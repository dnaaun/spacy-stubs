from ...language import Language
from typing import Any

class ArabicDefaults(Language.Defaults):
    lex_attr_getters: Any = ...
    tokenizer_exceptions: Any = ...
    stop_words: Any = ...
    suffixes: Any = ...
    writing_system: Any = ...

class Arabic(Language):
    lang: str = ...
    Defaults: Any = ...