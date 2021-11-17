**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

*TODO:* run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation
![pods](https://github.com/aykamal2016/Observability/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/pods-monitoring-observability.png)
![Svc](https://github.com/aykamal2016/Observability/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/svc-monitoring-observability.png)
## Setup the Jaeger and Prometheus source
*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.
![prometheus](https://github.com/aykamal2016/Observability/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/gravana_observability.png)

## Create a Basic Dashboard
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.
![prometheus](https://github.com/aykamal2016/Observability/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/prometheus-totalhttp-observability.png) 

## Describe SLO/SLI
*TODO:* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.

SLO is  service level objective  which is a target value or range of values for a service level that is measured by an SLI. Latency is one of the 4 golden signals that measure performance thus i want to rephrase the abstract SLO "request response time" to SLO more quantifiable like:
#### SLO: 95% of all Get request with status 200 should be within 0.1 seconds and the SLI will be 
  ##### SLI: 
  will be the actual measure for failed request divided by success request and it can be in the range of 0 to 5 % in order to comply with the target SLO
  ##### SLI: 
  Can be the actual measure of the average number of successful request duration and it can be less than 0.1 seconds to comply with the target SLO 
for the abstract SLO "monthy uptime" , i will rephrase it to more quantifiable like 
#### SLO: 99% monthly uptime for the service 
  ##### SLI: 
  will be the actual measurement of service uptime. Maybe it's  99.96%.

## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 
![prometheus](https://github.com/aykamal2016/Observability/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/final-totalhttp-observability.png)

service is defined in terms of five core properties :

Latency — The time taken to serve a request (usually measured in ms) 
Traffic — The amount of stress on a system from demand ,SLI the number of HTTP requests/second.
Errors — The number of requests that are failing , SLI number of 50x responses .
Saturation — The overall capacity of a service , SLI  will be he amount of CPU and RAM usage.
Uptime - The time the service is available, SLI will be time a service is active

## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.
![prometheus](https://github.com/aykamal2016/Observability/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/observability-dashboard4050.png)

## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here.
![tracability](https://github.com/aykamal2016/Observability/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/tracability.png)

## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.
![tracability](https://github.com/aykamal2016/Observability/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/jaeger-prometheus.png)
## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue.

TROUBLE TICKET

Name: POST request on backend service /star  00 500 Internal Server Error

Date: NOVEMBER 14 2021, 19:42:00

Subject: MongoDB Databse required by backend service is not accessible 

Affected Area: Backend Service

Severity: High


Description: /star endpoint in backend service should be able to post request to mongo database to procees it when we tried to post the request  using curl as shown below it gives 500 internal server error .
"vagrant@localhost:~> for i in {1..10} ; do curl --header "Content-Type: application/json" \
>   --request POST \
>   --data '{"name":"Ayman","distance":"15"}' \
>   10.0.2.15:8081/star ; done
## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name three SLIs that you would use to measure the success of this SLO.

SLO will be Uptime - SLI will be Service uptime should >= 99.95%

SLO will Latency- SLI will be Service latency should less than 0.5 seconds for >= 99.99% requests

SLO will Trafic-  SLI Service success response should be more than 99.99% request

SLO Resource Capacity- SLI The amount of memory and cpu usage by the service should be less than 90%


## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create KPIs to accurately measure these metrics. We will make a dashboard for this, but first write them down here.
CPU Usage <= 90%

Memory Usage <= 90%

Pod uptime >= 99.999 %

Average response time should be less than 0.5 seconds

Response latency should less than 0.5 seconds for >= 99.99% requests

Error per second <= 0.04% of the request

Success repsonse rate >= 99.99% request

These KPI were chosen as they are relevant and built around the four golden signal developed by google 
(latency, error rate ,traffic ,saturation)

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  
![prometheus](https://github.com/aykamal2016/Observability/blob/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/final-dashboard.png)
The memory usage of the Flask app. 

The CPU usage of the Flask app as measured over 30 seconds intervals.

The 50th percentile of request durations over the last 30 seconds.

pod Uptime

Number  of 40X and 50x responses

Number of failed (non HTTP 200) responses per second.

The average response time measured over 30 seconds intervals for successful requests

Request per second 

The 50th percentile of request durations over the last 30 seconds. 

Total Request per minute 
