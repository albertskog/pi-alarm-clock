"""Smart home integration module."""
import json
from paho.mqtt import client as mqtt
from config import CONFIG


class SmartHome(object):
    """MQTT connection abstraction."""

    def __init__(self, command_callback):
        """Initialize connection to MQTT broker."""
        self.client = mqtt.Client()
        self.command_callback = command_callback
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        try:
            self.client.username_pw_set(username=CONFIG["username"], password=CONFIG["password"])
            self.client.connect(CONFIG["broker"], )
            self.client.loop_start()
        except:
            print("MQTT broker not found")

    def on_connect(self, client, userdata, flags, result_code):
        """Callback for start of MQTT connection."""
        del client, userdata, flags, result_code
        self.client.subscribe(CONFIG["incoming_topic"])

    def on_message(self, client, userdata, msg):
        """Callback for incoming commands."""
        del client, userdata
        self.command_callback(json.loads(msg.payload))

    def send_event(self, event):
        """Publish state to broker."""
        self.client.publish(CONFIG["outgoing_topic"], json.dumps(event))
