import os
from typing import List


def get_settings_path():
    path_ = os.path.join(os.getcwd(), "app/settings", f'{os.getenv("conf", "prod")}.py')
    return path_


def match_best_language(header_value: str, supported_languages: List[str]):
    languages = header_value.split(",")
    parsed_languages = []

    for lang in languages:
        parts = lang.split(";")
        lang_code = parts[0].strip()
        q_value = (
            float(parts[1].split("=")[1])
            if len(parts) > 1 and "q=" in parts[1]
            else 1.0
        )
        parsed_languages.append((lang_code, q_value))

    parsed_languages.sort(key=lambda x: x[1], reverse=True)

    for lang_code, _ in parsed_languages:
        if lang_code in supported_languages:
            return lang_code
    return supported_languages[0]
