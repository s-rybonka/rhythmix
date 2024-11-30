import logging

import llm as llm_sdk
from django.conf import settings as dj_settings
from django.core.cache import cache
from django.core.exceptions import ValidationError as DjValidationError
from llm.errors import ModelError
from llm.errors import NeedsKeyException
from rest_framework.serializers import ValidationError as DRFValidationError


logger = logging.getLogger(__name__)


class OpenAIAPIService:
    API_KEY = dj_settings.OPEN_AI_API_KEY
    DEFAULT_MODEL = dj_settings.OPEN_AI_DEFAULT_MODEL
    DEFAULT_REST_ERROR_CLASS = DRFValidationError
    DEFAULT_NATIVE_ERROR_CLASS = DjValidationError
    CACHE_TIMEOUT = 3600 * 15

    def generate_summary(self, title, author):
        original_text = self.make_prompt(title, author)
        original_text_as_list = original_text.split('.')
        summary, countries = original_text_as_list
        return summary, countries

    def make_prompt(self, title, author):
        song_unique_key = f'{author.lower()}_{title.lower()}'
        cached_song_summary = cache.get(song_unique_key)

        if cached_song_summary:
            return cached_song_summary

        model = self.get_model()
        body = self.make_prompt_body(title, author)

        try:
            response = model.prompt(body)

        except (ModelError, NeedsKeyException) as e:
            logger.error(e)
            raise self.DEFAULT_REST_ERROR_CLASS(e)
        else:
            response_text = response.text()
            cache.set(song_unique_key, response_text, timeout=self.CACHE_TIMEOUT)
            return response_text

    def get_model(self):
        model = llm_sdk.get_model(self.DEFAULT_MODEL)
        model.key = self.API_KEY
        return model

    @staticmethod
    def make_prompt_body(title, author):
        return (f'Summarize the song {title} by {author} in one sentence. '
                f'If the song mentions countries, list them in a new sentence separated by commas.')
