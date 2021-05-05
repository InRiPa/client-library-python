"""
HttpProvider example app
"""
import arrowhead_client.api as ar
# from arrowhead_client.system import ArrowheadSystem
from arrowhead_client.system import ArrowheadSystem
import time

my_config = {
        "service_registry": ArrowheadSystem(system_name='service_registry', address='141.56.139.44', port=8443, authentication_info=''),
        "orchestrator": ArrowheadSystem(system_name='orchestrator', address='141.56.139.44', port=8441, authentication_info=''),
        "authorization": ArrowheadSystem(system_name='authorization', address='141.56.139.44', port=8455, authentication_info=''),
        "eventhandler": ArrowheadSystem(system_name='eventhandler', address='141.56.139.44', port=8455, authentication_info=''),
        "gatekeeper": ArrowheadSystem(system_name='gatekeeper', address='141.56.139.44', port=8449, authentication_info=''),
        "gateway": ArrowheadSystem(system_name='gatekeeper', address='141.56.139.44', port=8453, authentication_info='')
    }

provider_app = ar.ArrowheadHttpClient(
        system_name='provider1',
        address='127.0.0.1',
        port=7655,
        config=my_config,
        keyfile='certificates/provider1.key',
        certfile='certificates/provider1.crt',
)


@provider_app.provided_service(
        'hello-arrowhead',
        'hello',
        'HTTP-SECURE-JSON',
        'GET', )
def hello_arrowhead(request):
    return {"msg": "Hello, Arrowhead!"}



if __name__ == '__main__':
    provider_app.run_forever()
