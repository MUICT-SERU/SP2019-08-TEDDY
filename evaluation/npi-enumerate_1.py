def test_memory_consumption():
    app = flask.Flask(__name__)

    @app.route("/")
    def index():
        return flask.render_template("simple_template.html", whiskey=42)

    def fire():
        with app.test_client() as c:
            rv = c.get("/")
            assert rv.status_code == 200
            assert rv.data == b"<h1>42</h1>"

    # Trigger caches
    fire()

    # This test only works on CPython 2.7.
    if sys.version_info >= (2, 7) and not hasattr(sys, "pypy_translation_info"):
        with assert_no_leak():
            for _x in range(10):
                fire()