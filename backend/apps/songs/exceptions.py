from rest_framework.exceptions import APIException


class OpenAIAPIException(APIException):
    pass


class OpenAIPromptDataException(ValueError):
    pass
