import roslibpy
import sys
import configparser
import os

config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
config.read(config_path)

try:
    HOST=config['server']['url']
    PORT=int(config['server']['port'])
except KeyError:
    print("Cannot find correct keys! Please fix the config file.")
    sys.exit(1)

client = roslibpy.Ros(host=HOST, port=PORT)
client.run()

while not client.is_connected:
    pass

topics = client.get_topics()
if '/turtle1/pose' in topics:
    print('Echo /turtle1/pose')
    listener = roslibpy.Topic(client, '/turtle1/pose', 'turtlesim/Pose')
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