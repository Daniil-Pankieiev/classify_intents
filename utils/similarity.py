from utils.api_client import query
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_top_similar_sentences(source_sentence, sentences, top_n=3):
    """Fetches similarity scores for sentences and returns the top N similar sentences."""
    payload = {
        "inputs": {
            "source_sentence": source_sentence,
            "sentences": sentences
        }
    }
    output = query(payload)

    if "error" in output:
        logger.error(f"Error: {output['error']}")
        return []

    # Pair sentences with their similarity scores
    sentence_scores = list(zip(sentences, output))

    # Sort by similarity score, descending
    sentence_scores.sort(key=lambda x: x[1], reverse=True)

    return sentence_scores[:top_n]
