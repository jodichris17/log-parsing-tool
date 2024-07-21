# Log Parsing CLI Tool

This documentation provides a step-by-step guide to set up an ELK (Elasticsearch, Logstash, Kibana) stack and create a dashboard to visualize key metrics such as error rate over time, transaction volume, and average response time. 

Prerequisites:
```
Docker
Docker Compose
```
## Directory Structure

Ensure your project directory structure looks like this:

```
project-directory/
├── docker-compose.yml
├── logstash/
│ ├── config/
│ │ └── pipelines.yml
| | └── logstash.yml
│ └── pipeline/
│ └── logstash.conf
└── src/
   └── sample.log
   └── log_parser.py
   └── parsed_logs.json
```

-  docker-compose.yml: This file defines the Docker services for Elasticsearch, Logstash, and Kibana. It specifies the configurations, volumes, ports, and networks needed to run the ELK stack using Docker Compose.

-  pipelines.yml: This file configures the Logstash pipelines. It specifies the pipeline ID and the path to the pipeline configuration file (logstash.conf). This tells Logstash which pipeline to use and where to find its configuration.
  
-  logstash.yml: This file is the main configuration file for Logstash. It defines various settings that control the behavior of Logstash. 

-  logstash.conf: This file defines the Logstash pipeline configuration. It includes the input, filter, and output sections. The input section specifies the source of the data (parsed_logs.json), the filter section is for any data processing (currently commented out), and the output section specifies where to send the processed data (Elasticsearch).

-  sample.log: This file contains raw log entries that need to be parsed and converted into a structured format (e.g., JSON). It is the source data that the log_parser.py script will process.

-  log_parser.py: This script reads the raw log entries from sample.log, parses them, and outputs the structured log data into a file named parsed_logs.json. This structured data is then ingested by Logstash.

-  parsed_logs.json: This file contains the parsed log data in JSON format. It is the input data for Logstash. Logstash reads this file, processes the log entries, and sends them to Elasticsearch.
