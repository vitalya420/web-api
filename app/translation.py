# translation.py

import gettext
import os

# The first one is default value
SUPPORTED_LANGUAGES = ["en", "uk"]


class Translations(dict):
    def load_translations(self, lang: str):
        if lang not in self:
            try:
                translation = gettext.translation(
                    "messages",
                    localedir=os.path.join(os.getcwd(), "locales"),
                    languages=[lang],
                )
                self[lang] = translation
            except FileNotFoundError:
                self[lang] = gettext.NullTranslations()


translations = Translations()

for lang in SUPPORTED_LANGUAGES:
    translations.load_translations(lang)
