import broadlink
import subprocess,re,os,time
from influxdb import InfluxDBClient
from influxdb.exceptions import InfluxDBClientError

devices = broadlink.hello(os.environ['BROADLINK_HOST'])
devices.auth()
data = devices.check_sensors()

INFLUXDB_HOST = os.environ['INFLUXDB_HOST']
INFLUXDB_PORT = os.environ['INFLUXDB_PORT']
INFLUXDB_USERNAME = os.environ['INFLUXDB_USERNAME']
INFLUXDB_PASSWORD = os.environ['INFLUXDB_PASSWORD'] 
INFLUXDB_DATABASE = os.environ['INFLUXDB_DATABASE'] 
points=[]


try:
    client = InfluxDBClient(host=INFLUXDB_HOST, port=INFLUXDB_PORT, username=INFLUXDB_USERNAME, password=INFLUXDB_PASSWORD)
    client.create_database(INFLUXDB_DATABASE)
    client.switch_database(INFLUXDB_DATABASE)
except InfluxDBClientError as err:
    print("InfluxDB connection failed: %s" % (err))
    sys.exit()

json_body = [{
            "measurement": "temperature",
            "tags": {
                "room": "alexxanddr"
            },
            "fields": {
                "value": data['temperature']
            }
        },
        {
            "measurement": "humidity",
            "tags": {
                "room": "alexxanddr"
            },
            "fields": {
                "value": data['humidity']
            }
        }]

client.write_points(json_body)