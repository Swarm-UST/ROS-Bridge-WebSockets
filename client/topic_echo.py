import roslibpy
import sys
import configparser

config = configparser.ConfigParser()
config.read('./config.ini')

try:
    HOST=config['server']['url']
    PORT=int(config['server']['port'])
except KeyError:
    print("Plesae change directory to \"client\" first and then run the script again")
    sys.exit(1)

client = roslibpy.Ros(host=HOST, port=PORT)
client.run()

while not client.is_connected:
    pass

topics = client.get_topics()
if '/turtle1/pose' in topics:
    print('Echo /turtle1/pose')
    listener = roslibpy.Topic(client, '/turtle1/pose', 'turtlesim/Pose')
    # listener.subscribe(lambda message: print(f"x: {message['x']} y: {message['y']}"))
    listener.subscribe(lambda message: print("x: {:.4f} y: {:.4f}".format(message['x'], message['y'])))
else:
    print('Cannot find /turtle1/pose. Exit')
    client.terminate()
    sys.exit(1)


try:
    while True:
        pass
except KeyboardInterrupt:
    client.terminate()