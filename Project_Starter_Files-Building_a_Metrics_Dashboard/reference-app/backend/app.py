from flask import Flask, render_template, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics

import pymongo
import logging
from flask_pymongo import PyMongo
from opentelemetry import trace
from opentelemetry.exporter import jaeger
from jaeger_client import Config
from jaeger_client.metrics.prometheus import PrometheusMetricsFactory
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchExportSpanProcessor
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    ConsoleSpanExporter,
    SimpleExportSpanProcessor,
)

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleExportSpanProcessor(ConsoleSpanExporter())
)


app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

def init_tracer(service):
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    config = Config(
        config={
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'logging': True,
            'reporting_host': 'simplezt-agent.observability.svc.cluster.local'
        },
        service_name=service,
    )
    
    # this call also sets opentracing.tracer
    return config.initialize_tracer()

tracer = init_tracer('simplezt')
app.config['MONGO_DBNAME'] = 'example-mongodb'
app.config['MONGO_URI'] = 'mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb'

mongo = PyMongo(app)
metrics = PrometheusMetrics(app, group_by='endpoint')
metrics.info("app_info", "App Info", version="1.0.0")
common_counter = metrics.counter(
    'by_endpoint_counter', 'Request count by endpoints',
    labels={'endpoint': lambda: request.endpoint}
)



@app.route('/')
@common_counter
def homepage():
    with tracer.start_span('homepage') as span: 
     span.set_tag('homepage', 'homepage')   
    return "Hello World"


@app.route('/api')
@common_counter
def my_api():
    with tracer.start_span('api') as span: 
     span.set_tag('/Api', '/api')   
     answer = "something"
    return jsonify(repsonse=answer)

@app.route('/star', methods=['POST'])
@common_counter
def add_star():
  with tracer.start_span('add_star') as span:  
       span.set_tag('Add_Star', 'Add_Star')
       star = mongo.db.stars
       name = request.json['name']
       distance = request.json['distance']
       star_id = star.insert({'name': name, 'distance': distance})
       new_star = star.find_one({'_id': star_id })
       output = {'name' : new_star['name'], 'distance' : new_star['distance']}
  return jsonify({'result' : output})

# register additional default metrics
metrics.register_default(
    metrics.counter(
        'by_path_counter', 'Request count by request paths',
        labels={'path': lambda: request.path}
    )
)

if __name__ == "__main__":
    app.run()
