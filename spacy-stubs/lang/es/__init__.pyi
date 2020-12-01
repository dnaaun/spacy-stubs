from ...language import Language
from typing import Any

class SpanishDefaults(Language.Defaults):
    lex_attr_getters: Any = ...
    tokenizer_exceptions: Any = ...
    tag_map: Any = ...
    stop_words: Any = ...
    syntax_iterators: Any = ...

class Spanish(Language):
    lang: str = ...
    Defaults: Any = ...