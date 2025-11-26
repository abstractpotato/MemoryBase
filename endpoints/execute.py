def run(app, request):

    @app.route("/execute", methods=["POST"])
    def execute():
        return app.database.execute(request.get_json()["query"])

    @app.route("/load")
    def load():
        return app.database.disk_load()

    @app.route("/save")
    def save():
        return app.database.disk_save()

    @app.route("/tables")
    def tables():
        return app.database.get_tables()
