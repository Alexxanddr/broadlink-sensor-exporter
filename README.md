# broadlink-sensor-exporter

exporter to influx for broadlink sensor on k8s

The python script collect trakt information from API rest and push the data into the influxDB.

## Build Command:
```
docker buildx build --push --tag alexxanddr/broadlink-sensor-exporter:latest --platform linux/amd64,linux/arm/v7,linux/arm64/v8  .
```

I add the variables for the configuration as environment variable in cronjob.yaml:

* BROADLINK_HOST
* INFLUXDB_HOST
* INFLUXDB_PORT
* INFLUXDB_USERNAME
* INFLUXDB_PASSWORD
* INFLUXDB_DATABASE
 
The cronjob.yaml is scheduled with cron rule:

1 * * * *


