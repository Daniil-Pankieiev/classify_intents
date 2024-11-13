from utils.similarity import get_top_similar_sentences


def test_get_top_similar_sentences(mocker):
    mock_query = mocker.patch('utils.api_client.query', return_value=[0.9, 0.5, 0.3])
    source_sentence = "test"
    sentences = ["sentence1", "sentence2", "sentence3"]

    top_sentences = get_top_similar_sentences(source_sentence, sentences, top_n=2)
    assert top_sentences == [('sentence1', 0.3635050058364868), ('sentence2', 0.3578748106956482)]

