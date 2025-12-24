# Broadlink Sensor Exporter

A Python application to **read temperature and humidity from Broadlink sensors** and export the data to **InfluxDB**. Designed to run as a **Docker container** and optionally deployed on **Kubernetes as a CronJob**.

---

## ✨ Features

- Read data from Broadlink sensors via Python `broadlink` library
- Export temperature and humidity to InfluxDB
- Configurable via environment variables
- Dockerized for easy deployment
- Kubernetes CronJob ready for scheduled runs

---

## 🧱 Requirements

- Python **3.7+**
- Broadlink sensor on the network
- InfluxDB instance reachable via network
- Docker (optional, for containerized deployment)
- Kubernetes (optional, for CronJob deployment)

---

## 🔧 Installation

1. Clone the repository
```bash
git clone <repo-url>
cd broadlink-sensor-exporter
```

2. Install Python dependencies
```bash
pip install -r requirements.txt
```

3. Set environment variables
```bash
export BROADLINK_HOST=<BROADLINK_IP>
export INFLUXDB_HOST=<INFLUXDB_HOST>
export INFLUXDB_PORT=<INFLUXDB_PORT>
export INFLUXDB_USERNAME=<USERNAME>
export INFLUXDB_PASSWORD=<PASSWORD>
export INFLUXDB_DATABASE=<DATABASE_NAME>
```

---

## ▶️ Running the script

```bash
python broadlink-sensor.py
```

The script will read temperature and humidity from the Broadlink device and write the measurements to InfluxDB.

---

## 🐳 Docker Usage

1. Build the Docker image
```bash
docker build -t broadlink-sensor-exporter .
```

2. Run the container with environment variables
```bash
docker run -e BROADLINK_HOST=<BROADLINK_IP>            -e INFLUXDB_HOST=<INFLUXDB_HOST>            -e INFLUXDB_PORT=<INFLUXDB_PORT>            -e INFLUXDB_USERNAME=<USERNAME>            -e INFLUXDB_PASSWORD=<PASSWORD>            -e INFLUXDB_DATABASE=<DATABASE_NAME>            broadlink-sensor-exporter
```

---

## ☸️ Kubernetes CronJob

The repository includes a **CronJob manifest** to schedule sensor reads in a Kubernetes cluster.

- **Schedule:** Every 2 minutes (`1-59/2 * * * *`)
- **Environment variables:** Set within the container spec
- **Image:** `alexxanddr/broadlink-sensor-exporter:latest`

```yaml
apiVersion: batch/v1beta1
kind: CronJob
metadata:
  name: broadlink-sensor-exporter
spec:
  schedule: "1-59/2 * * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: broadlink-sensor-exporter
            image: alexxanddr/broadlink-sensor-exporter:latest
            env:
            - name: BROADLINK_HOST
              value: ''
            - name: INFLUXDB_HOST
              value: ''
            - name: INFLUXDB_PORT
              value: ''
            - name: INFLUXDB_USERNAME
              value: ''
            - name: INFLUXDB_PASSWORD
              value: ''
            - name: INFLUXDB_DATABASE
              value: ''
          restartPolicy: OnFailure
```

---

## ⚠️ Notes

- Ensure the Broadlink device is reachable from the host/container
- InfluxDB credentials must be valid
- The Python script will automatically create the database if it does not exist

---

## 📜 License

MIT License

---

## 👤 Author

A simple tool for exporting sensor data from Broadlink devices to InfluxDB, deployable via Docker and Kubernetes.
