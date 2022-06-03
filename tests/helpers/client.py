from flask.testing import FlaskClient


class CustomClient(FlaskClient):
    def __init__(self, *args, **kwargs):
        self._headers = {
            "Authorization": f'Bearer {kwargs.pop("token")}',
        }

        super().__init__(*args, **kwargs)

    def _prepare_kwargs(self, kwargs):
        if "headers" in kwargs:
            kwargs["headers"].update(self._headers)
        else:
            kwargs["headers"] = self._headers

        return kwargs

    def set_headers(self, **kwargs):
        self._headers = kwargs

    def get(self, *args, **kwargs):
        kwargs = self._prepare_kwargs(kwargs)

        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        kwargs = self._prepare_kwargs(kwargs)

        return super().post(*args, **kwargs)

    def put(self, *args, **kwargs):
        kwargs = self._prepare_kwargs(kwargs)

        return super().put(*args, **kwargs)

    def delete(self, *args, **kwargs):
        kwargs = self._prepare_kwargs(kwargs)

        return super().delete(*args, **kwargs)
