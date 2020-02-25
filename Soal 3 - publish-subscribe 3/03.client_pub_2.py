# import paho mqtt
import paho.mqtt.client as mqtt

# import time untuk sleep()
import time

# import datetime untuk mendapatkan waktu dan tanggal
import datetime

# definisikan nama broker yang akan digunakan
broker_address = "127.0.0.1"

# buat client baru bernama P3
print("creating new instance")
client = mqtt.Client("P3")


def on(client, userdata, message):
    print("ok")


# koneksi ke broker
print("connecting to broker")
client.connect(broker_address)
client.on_publish = on

# mulai loop client
client.loop_start

# lakukan 20x publish topik 2
print("publish something")
for i in range(20):
    # sleep 1 detik
    time.sleep(1)
    # publish waktu sekarang topik 2
    client.publish("topik_2", datetime.datetime.now().strftime(
        "BBB %Y:%m:%D:%H:%M:%S"))

# stop the loop
client.loop_stop
