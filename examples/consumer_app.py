"""
HttpConsumer example app
"""
import arrowhead_client.api as ar
# from arrowhead_client.system import ArrowheadSystem
from arrowhead_client.system import ArrowheadSystem


my_config = {
        "service_registry": ArrowheadSystem(system_name='service_registry', address='141.56.139.44', port=8443, authentication_info=''),
        "orchestrator": ArrowheadSystem(system_name='orchestrator', address='141.56.139.44', port=8441, authentication_info=''),
        "authorization": ArrowheadSystem(system_name='authorization', address='141.56.139.44', port=8455, authentication_info=''),
        "eventhandler": ArrowheadSystem(system_name='eventhandler', address='141.56.139.44', port=8455, authentication_info=''),
        "gatekeeper": ArrowheadSystem(system_name='gatekeeper', address='141.56.139.44', port=8449, authentication_info=''),
        "gateway": ArrowheadSystem(system_name='gatekeeper', address='141.56.139.44', port=8453, authentication_info='')
    }

consumer_app = ar.ArrowheadHttpClient(
        system_name='timeconsumer',
        address='127.0.0.1',
        port=7656,
        config=my_config,
        keyfile='certificates/timeconsumer.key',
        certfile='certificates/timeconsumer.crt',
)

consumer_app.add_consumed_service('hello-arrowhead', 'GET')




if __name__ == '__main__':
    response = consumer_app.consume_service('hello-arrowhead')
    message = consumer_app.consumer.extract_payload(response, 'json')
    message_2 = consumer_app.extract_payload(response, 'json') # TODO: remove the first message extraction

    print(message['msg'])
