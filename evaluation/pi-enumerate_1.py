def test_jsonify_date_types(self, app, client):
        """Test jsonify with datetime.date and datetime.datetime types."""
        test_dates = (
            datetime.datetime(1973, 3, 11, 6, 30, 45),
            datetime.date(1975, 1, 5),
        )

        for i, d in enumerate(test_dates):
            url = "/datetest{0}".format(i)
            app.add_url_rule(url, str(i), lambda val=d: flask.jsonify(x=val))
            rv = client.get(url)
            assert rv.mimetype == "application/json"
            assert flask.json.loads(rv.data)["x"] == http_date(d.timetuple())