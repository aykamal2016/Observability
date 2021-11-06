from flask import Flask, render_template, request, jsonify

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

 #   config = Config(
  #      config={
   #         'sampler': {
    #            'type': 'const',
     #           'param': 1,
      #      },
       #     'logging': True,
        #},
        #service_name=service,
    #)
    
    config = Config(config={'sampler': {'type': 'const', 'param': 1},
                                'logging': True,
                                'local_agent':
                                # Also, provide a hostname of Jaeger instance to send traces to.
                                {'reporting_host': localhost}},
                        # Service name can be arbitrary string describing this particular web service.
                        service_name="backend service")
    # this call also sets opentracing.tracer
    return config.initialize_tracer()

tracer = init_tracer('backend-service')
app.config['MONGO_DBNAME'] = 'example-mongodb'
app.config['MONGO_URI'] = 'mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb'

mongo = PyMongo(app)




@app.route('/')
def homepage():
    return "Hello World"


@app.route('/api')
def my_api():
    answer = "something"
    return jsonify(repsonse=answer)

@app.route('/star', methods=['POST'])
def add_star():
  with tracer.start_span('MongoDB') as span:  
       span.set_tag('Add Star', 'Add Star')
       star = mongo.db.stars
       name = request.json['name']
       distance = request.json['distance']
       with tracer.start_span('Mongo Insert ',child_of=span) as second_span: 
            second_span.set_tag('Mongo Insert','Mongo Insert')
            star_id = star.insert({'name': name, 'distance': distance})
       with tracer.start_span('Mongo Find By ID ',child_of=span) as third_span: 
            third_span.set_tag('Find ByID','Find By ID')
            new_star = star.find_one({'_id': star_id })
       output = {'name' : new_star['name'], 'distance' : new_star['distance']}
  return jsonify({'result' : output})

if __name__ == "__main__":
    app.run()
