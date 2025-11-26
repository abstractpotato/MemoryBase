def run(app):

    @app.route("/")
    def version():
        return {"status": "online"}

    @app.errorhandler(404)
    def err404(e):
        return {"msg": "not_found"}, 404

    @app.errorhandler(405)
    def err405(e):
        return {"msg": "method_not_allowed"}, 405

    @app.errorhandler(429)
    def err429(e):
        return {"msg": "too_many_requests"}, 429

    @app.errorhandler(500)
    def err500(e):
        return {"msg": "internal_server_error"}, 500
