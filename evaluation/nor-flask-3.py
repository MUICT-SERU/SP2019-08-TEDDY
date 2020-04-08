def test_context_available(app, client):
    class ContextConverter(BaseConverter):
        def to_python(self, value):
            assert has_request_context()
            return value