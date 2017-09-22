"""Smart home integration module"""
import json
from paho.mqtt import client as paho
from config import CONFIG

class SmartHome(object): # pylint: disable=R0903
    """MQTT connection abstraction"""
    def __init__(self):
        self.client = paho.Client()
        self.client.connect(CONFIG["broker"])
        self.client.loop_start()

    def send_event(self, event):
        """Publish state to broker"""
        self.client.publish(CONFIG["topic"], json.dumps(event))
