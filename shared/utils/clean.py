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
