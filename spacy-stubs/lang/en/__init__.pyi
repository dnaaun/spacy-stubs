from ...language import Language
from typing import Any

class EnglishDefaults(Language.Defaults):
    lex_attr_getters: Any = ...
    tokenizer_exceptions: Any = ...
    tag_map: Any = ...
    stop_words: Any = ...
    morph_rules: Any = ...
    syntax_iterators: Any = ...
    single_orth_variants: Any = ...
    paired_orth_variants: Any = ...

class English(Language):
    lang: str = ...
    Defaults: Any = ...