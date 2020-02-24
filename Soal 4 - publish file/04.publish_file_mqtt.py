# import paho
import paho.mqtt.client as mqtt

# definsi broker yang digunakan
broker_address = "localhost"

# buat client bernama P1
print("creating new instance")
client = mqtt.Client("P1")

# client terkoneksi ke broker
print("connecting to broker")
client.connect(broker_address, port=3333)

# print "baca file"
print("read file")

# buka file surf.jpg


# baca semua isi file


# ubah file dalam bentuk byte gunakan fungsi byte()


# publish dengan topik photo dan data dipublish adalah file
print("publish foto")


# client loop mulai


# tutup file
