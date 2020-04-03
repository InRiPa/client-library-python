import datetime
from arrowhead_client.arrowhead_system import ProviderSystem
from arrowhead_client.provider import provided_service
from flask import request
#from source.service_provider import ServiceProvider

class TimeProvider(ProviderSystem):
    def __init__(self, *args, **kwargs):
       ProviderSystem.__init__(self, *args, **kwargs)
       self.format = '%H:%M:%S'

    def setup_services(self):
        @self.add_service('time', '/time', 'HTTP-SECURE-JSON')
        def get_time():
            return datetime.datetime.now().strftime(self.format)

        @self.add_service('format', '/time/format', 'HTTP-SECURE-JSON', ['POST'])
        def change_format():
            data = request.data

            self.format = data.decode()

            return data


if __name__ == '__main__':
    from pprint import pprint

    time_provider = TimeProvider.from_properties('examples/time_provider.properties')
    #time_provider.setup_services()
    time_provider.run_forever()
