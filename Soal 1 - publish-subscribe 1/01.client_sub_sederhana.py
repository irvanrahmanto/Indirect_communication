# import paho mqtt
# import paho.mqtt.client as mqtt
import paho.mqtt.client as mqtt

# import time for sleep()
import time

# buat callback on_message; jika ada pesan
# maka fungsi ini akan dipanggil secara asynch
########################################


def on_message(client, userdata, message):
    # print pesan
    print("message received ", str(message.payload.decode("utf-8")))
    #print("message topic=",message.topic)
    #print("message qos=",message.qos)
    #print("message retain flag=",message.retain)
########################################


# buat definisi nama broker yang akan digunakan
# broker_address = "localhost"
# broker_address = "smtp.mail.yahoo.com"
broker_address = "127.0.0.1"
# broker_address+"iot.eclipse.org"

# buat client baru bernama P1
print("creating new instance")
client = mqtt.Client("P1")

# kaitkan callback on_message ke client
client.on_message = on_message

# buat koneksi ke broker
print("connecting to broker")
# client.connect(broker_address, port=3333)
client.connect(broker_address)

# jalankan loop client
client.loop_start()

# client melakukan subsribe ke topik 1
print("Subscribing to topic", "waktu")
client.subscribe("waktu")

# loop forever
while True:
    # berikan waktu tunggu 1 detik
    time.sleep(1)

    # stop loop
client.loop_stop()
