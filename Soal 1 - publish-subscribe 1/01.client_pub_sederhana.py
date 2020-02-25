# import paho mqtt
import paho.mqtt.client as mqtt

# import time untuk sleep()
import time

# import datetime untuk mendapatkan waktu dan tanggal
import datetime

# definisikan nama broker yang akan digunakan
# broker_address = "localhost"
# broker_address = "smtp.mail.yahoo.com"
broker_address = "127.0.0.1"

# buat client baru bernama P2
print("creating new instance")
client = mqtt.Client("P2")


def on_publish(client, userdata, resutl):
    print("data published")


client.on_publish = on_publish

# koneksi ke broker
print("connecting to broker")
# client.connect(broker_address, port=3333)
client.connect(broker_address)

# mulai loop client
client.loop_start()


# lakukan 20x publish waktu dengan topik 1
print("publish something")
for i in range(20):
    # sleep 1 detik
    time.sleep(1)
    # publish waktu sekarang
    client.publish(
        "waktu", datetime.datetime.now().strftime("%Y:%m:%D:%H:%M:%S"))
    # print(x)
    # datetime()
    # stop loop
client.loop_stop()
