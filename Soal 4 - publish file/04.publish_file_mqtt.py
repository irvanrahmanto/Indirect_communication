# import paho
import paho.mqtt.client as mqtt

# definsi broker yang digunakan
broker_address = "127.0.0.1"

# buat client bernama P1
print("creating new instance")
client = mqtt.Client("P1")

# client terkoneksi ke broker
print("connecting to broker")
client.connect(broker_address)

# print "baca file"
print("read file")

# buka file surf.jpg
my_file = open("surf.jpg", 'rb')

# baca semua isi file
fileContent = my_file.read()

# ubah file dalam bentuk byte gunakan fungsi byte()
byteArr = bytes(fileContent)
# client.publish("photo", byteArr)
# publish dengan topik photo dan data dipublish adalah file
print("publish foto")
client.publish("photo", byteArr)

# client loop mulai
client.loop_start()

# tutup file
my_file.close()
