import pytest


def test_word_count_with_words(client):
    response = client.post('/', data={'text': 'testing word count'})

    assert response.status_code == 200
    assert b"The text has <strong>3</strong>" in response.data


def test_word_count_with_no_words(client):
    response = client.post('/', data={'text': ''})

    assert response.status_code == 200
    assert b"Please enter some text." in response.data
