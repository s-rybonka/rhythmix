import logging

import llm as llm_sdk
from django.conf import settings as dj_settings
from django.core.exceptions import ValidationError as DjValidationError
from llm.errors import ModelError
from llm.errors import NeedsKeyException
from rest_framework.serializers import ValidationError as DRFValidationError


logger = logging.getLogger(__name__)


class OpenAIAPIService:
    API_KEY = dj_settings.OPEN_AI_API_KEY
    MODEL = dj_settings.OPEN_AI_DEFAULT_MODEL
    DEFAULT_REST_ERROR_CLASS = DRFValidationError
    DEFAULT_NATIVE_ERROR_CLASS = DjValidationError

    def get_model(self):
        model = llm_sdk.get_model(self.MODEL)
        model.key = self.API_KEY
        return model

    def make_prompt(self, body):
        model = self.get_model()

        try:
            response = model.prompt(body)

        except (ModelError, NeedsKeyException) as e:
            logger.error(e)
            raise self.DEFAULT_REST_ERROR_CLASS(e)
        else:
            return response.text()
