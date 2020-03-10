# gunakan library paho
import paho.mqtt.client as mqtt

# gunakan library time
import time

# buat callback pada saat ada pesan masuk
###########################################


def on_message(client, userdata, message):
    # tulis hasil file yang didapat bernama "iris.jpg"
    # with open("iris.jpg", "wb") as x:
    #     x.write(message.payload)
    #     x.close()
    #     print("Downloaded")
    my_file = open("iris.jpg", 'wb')
    my_file.write(message.payload)
    my_file.close()
    print("Downloaded")
    # with open("iris.jpg", "wb"):
    #     my_file = open("surf.jpg", 'wb')
    #     my_file.write(message.payload)
    #     my_file.close()
    #     print("Downloaded")
    ##########################################


# definisikan broker yang akan digunakan
broker_address = "127.0.0.1"

# buat client P2
print("creating new instance")
client = mqtt.Client("P2")
# client.on_message = on_message

# koneksi P2 ke broker
print("connecting to broker")
client.connect(broker_address)

# P2 subcribe ke topik "photo"
print("Subscribing to topic", "photo")
client.subscribe("photo")

# callback diaktifkan
client.on_message = on_message

# client.loop_forever()
while True:
    client.loop(15)
    time.sleep(2)
