from difflib import SequenceMatcher


def get_similarity(text: str, target_text: str) -> float:
    return SequenceMatcher(None, text, target_text).ratio()


def are_similar_text(text: str, target_text: str, limit: float = 0.8) -> bool:
    return get_similarity(text, target_text) > limit
