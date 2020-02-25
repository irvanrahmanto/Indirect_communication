# import paho mqtt
import paho.mqtt.client as mqtt

# import time untuk sleep()
import time

# import datetime untuk mendapatkan waktu dan tanggal
import datetime


def on(client, userdata, message):
    print("published")


# definisikan nama broker yang akan digunakan
broker_address = "127.0.0.1"

# buat client baru bernama P2
print("creating new instance")
client = mqtt.Client("P2")
client.on_publish = on

# koneksi ke broker
print("connecting to broker")
client.connect(broker_address)

# mulai loop client
client.loop_start()

# lakukan 20x publish topik 1
print("publish something")
for i in range(20):
    # sleep 1 detik
    time.sleep(1)
    # publish waktu sekarang topik 1
    client.publish("topik_1", datetime.datetime.now().strftime(
        "AAA %Y:%m:%D:%H:%M:%S"))

# stop loop
client.loop_stop()
