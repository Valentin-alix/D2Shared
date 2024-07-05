import unidecode


def clean_item_name(name: str) -> str:
    return (
        unidecode.unidecode(name, "utf-8")
        .replace(" ", "_")
        .replace(".", "")
        .replace("'", "_")
        .replace("-", "_")
        .replace('"', "")
        .replace("/", "_")
        .lower()
    )


def clean_line_text(text: str) -> str:
    normalized_text = (
        unidecode.unidecode(text, "utf-8")
        .replace(" ", "")
        .replace("\n", "")
        .replace(".", "")
        .lower()
    )
    return normalized_text
