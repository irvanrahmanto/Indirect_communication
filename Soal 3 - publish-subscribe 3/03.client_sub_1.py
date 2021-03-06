# import paho mqtt
import paho.mqtt.client as mqtt

# import time for sleep()
import time

# import re (regular expression) untuk filter


# buat callback on_message; jika ada pesan
# maka fungsi ini akan dipanggil secara asynch
########################################
def on_message(client, userdata, message):
    # filter pesan yang masuk
    pesan = str(message.payload.decode("utf-8"))
    match = "AAA" in pesan
    print(pesan)
    # jika ada pola AAA tulis ke result_a.txt
    if match:
        with open("result_a.txt", "a+") as x:
            x.write(pesan)
            x.write("\n")
        # lainnya tulis ke result_b.txt
    else:
        with open("result_b.txt", "a+") as x:
            x.write(pesan)
            x.write("\n")
########################################


# buat definisi nama broker yang akan digunakan
broker_address = "127.0.0.1"

# buat client baru bernama P1
print("creating new instance")
client = mqtt.Client("P1")

# kaitkan callback on_message ke client
client.on_message = on_message

# buat koneksi ke broker
print("connecting to broker")
client.connect(broker_address)

# jalankan loop client
client.loop_start()

# client melakukan subsribe ke topik 1 dan topik 2
print("Subscribing to topic")
client.subscribe("topik_1")
client.subscribe("topik_2")

# loop forever
while True:
    # berikan waktu tunggu 1 detik
    time.sleep(1)

# stop loop
client.loop_stop()
