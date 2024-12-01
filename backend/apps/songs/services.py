import logging

import llm as llm_sdk
from django.conf import settings as dj_settings
from django.core.cache import cache
from llm.errors import ModelError
from llm.errors import NeedsKeyException
from openai import AuthenticationError

from songs import exceptions as songs_exceptions


logger = logging.getLogger(__name__)


class OpenAIAPIService:
    API_KEY = dj_settings.OPENAI_API_KEY
    DEFAULT_MODEL = dj_settings.OPENAI_DEFAULT_MODEL
    DEFAULT_ERROR_CLASS = songs_exceptions.OpenAIAPIException
    CACHE_TIMEOUT = 3600 * 15

    def generate_summary(self, title, author):
        original_text = self.make_prompt(title, author)
        original_text_as_list = original_text.split('.')
        summary, countries, *junk = original_text_as_list
        return summary, countries

    def make_prompt(self, title, author):
        song_unique_key = self.get_cache_unique_key(title, author)
        cached_song_summary = cache.get(song_unique_key)

        if cached_song_summary:
            return cached_song_summary

        model = self.get_model()
        body = self.make_prompt_body(title, author)

        try:
            response = model.prompt(body)
            response_text = response.text()
            cache.set(song_unique_key, response_text, timeout=self.CACHE_TIMEOUT)
            return response_text

        except (ModelError, NeedsKeyException) as e:
            logger.error(e)
            raise self.DEFAULT_ERROR_CLASS(e)

        except AuthenticationError as e:
            logger.error(e)
            raise self.DEFAULT_ERROR_CLASS('Incorrect OpenAI API key provided.')

    def get_model(self):
        model = llm_sdk.get_model(self.DEFAULT_MODEL)
        model.key = self.API_KEY
        return model

    @staticmethod
    def make_prompt_body(title, author):
        return (f'Summarize {title} by {author} song in one sentence, title and author are not repeated. '
                f'List mentioned countries as plain comma-separated items in a new sentence. '
                f'Exclude newline symbols. If the provided song and author are not real, raise "ModelError".')

    @staticmethod
    def get_cache_unique_key(title, author):
        author_concat = "_".join(author.strip().split(" ")).lower()
        title_concat = "_".join(title.strip().split(" ")).lower()
        return f'{author_concat}_{title_concat}'
