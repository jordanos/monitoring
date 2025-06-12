### Monitoring Setup with Prometheus and Grafana

This setup provides robust monitoring capabilities using Prometheus and Grafana.

#### Steps to Get Started:

1. **Launch the Monitoring Stack:**

   - Run the following command to start the services:
     ```bash
     python3 generate_configs.py
     docker compose up
     ```
   - This will spin up all necessary components, including Prometheus, Grafana, and any relevant exporters.

2. **Access the Grafana Dashboard:**

   - Once the stack is up and running, open your browser and navigate to:
     [http://localhost:4444](http://localhost:4444)

3. **Configure Grafana Dashboards:**
   - After logging into Grafana, configure your monitoring dashboards by importing the relevant dashboard IDs or by customizing your own.

### Steps for configuration:

- Navigate to data sources section and select prometheus.
- Set prometheus url access `http://prometheus:9090`, leave the other default settings and press `save & test`.
- After you're done with configuring prometheus data source go ahead and Import dashboard templates.

### Dashboard templates

#### Node Exporter:

- Import: using the dashboard ID `1860`.
- Name: Node Exporter Full.
- Description: helps to see system information and usage (cpu, network, memory...).

#### cAdvisor Exporter:

- Import: using the dashboard ID `14282`.
- Name: Docker and system monitoring using Prometheus.
- Description: helps to see containers information and usage.

#### Celery:

- Import: using the json document in `/dashboards/celery.json`.
- Name: Celery.
- Description: Monitoring celery service.

#### Django Requests:

- Import: using the json document in `/dashboards/django_requests.json`.
- Name: Django Requests.
- Description: Monitoring django requests.

#### Django Prometheus:

- Import: using the json document in `/dashboards/django_promethues.json`.
- Name: Django Prometheus.
- Description: Monitoring Django.

#### Gunicorn:

- Import: using the json document in `/dashboards/gunicorn.json`.
- Name: Gunicorn Monitoring.
- Description: Monitoring gunicorn workers.
