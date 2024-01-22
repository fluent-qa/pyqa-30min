import pytest

from revisited.r_config.dynaconf_settings_demo import ensure_env_settings
from revisited.r_dispatch.dispatch import Dispatcher


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="Environment to run tests in")

# provider env value in pytest 
def env(request):
    return request.config.getoption("-—env")


@pytest.fixture
def listener():
    class Listener(object):
        def __init__(self):
            self.received_events = []
            self.received_event_data = []
            self.property_events = []
            self.property_event_kwargs = []
            self.property_event_map = {}

        def on_event(self, *args, **kwargs):
            self.received_event_data.append({'args': args, 'kwargs': kwargs})
            name = kwargs.get('triggered_event')
            if name is not None:
                self.received_events.append(name)

        def on_prop(self, obj, value, **kwargs):
            self.property_events.append(value)
            self.property_event_kwargs.append(kwargs)
            prop = kwargs['property']
            if prop.name not in self.property_event_map:
                self.property_event_map[prop.name] = []
            self.property_event_map[prop.name].append({'value': value, 'kwargs': kwargs})

    return Listener()


@pytest.fixture
def sender_cls():
    class Sender(Dispatcher):
        def trigger_event(self, name, *args, **kwargs):
            kwargs['triggered_event'] = name
            self.emit(name, *args, **kwargs)

    return Sender


@pytest.fixture
def sender(sender_cls):
    return sender_cls()


@pytest.fixture(scope="session", autouse=True)
def setup_environment_setting(request):
    env_name = request.config.getoption("--env")
    ensure_env_settings(env_name)
