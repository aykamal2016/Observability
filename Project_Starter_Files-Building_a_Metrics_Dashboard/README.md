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
  will be the actual measurement of service uptime. Maybe it's 99.96%.

## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 

service is defined in terms of five core properties :

Latency — The time taken to serve a request (usually measured in ms) 
Traffic — The amount of stress on a system from demand ,SLI the number of HTTP requests/second.
Errors — The number of requests that are failing , SLI number of 50x responses .
Saturation — The overall capacity of a service , SLI  will be he amount of CPU and RAM usage.
Uptime - The time the service is available, SLI will be time a service is active

## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.

## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here.

## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue.

TROUBLE TICKET

Name:

Date:

Subject:

Affected Area:

Severity:

Description:


## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name three SLIs that you would use to measure the success of this SLO.

## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create KPIs to accurately measure these metrics. We will make a dashboard for this, but first write them down here.

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  
