from flask import Flask
from __appsignal__ import appsignal
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry import trace

def create_app():
    appsignal.start()
    app = Flask(__name__)
    app.static_folder = 'static'
    
    # Instrument Flask with OpenTelemetry
    FlaskInstrumentor().instrument_app(app)
    
    from . import routes
    app.register_blueprint(routes.bp)

    return app
