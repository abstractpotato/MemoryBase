def run(app, request):

    @app.route("/execute", methods=["POST"])
    def execute():
        json = request.get_json()
        if "data" in json:
            return app.database.execute(json["query"], tuple(json["data"]))
        return app.database.execute(json["query"])

    @app.route("/load")
    def load():
        return app.database.disk_load()

    @app.route("/save")
    def save():
        return app.database.disk_save()

    @app.route("/tables")
    def tables():
        return app.database.get_tables()
