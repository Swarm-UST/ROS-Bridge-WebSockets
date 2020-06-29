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

service = roslibpy.Service(client, '/clear', 'std_srvs/Empty')
request = roslibpy.ServiceRequest()

print('Calling service...')
result = service.call(request)
print('clear finished')

client.terminate()