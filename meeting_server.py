"""Shared meeting API for Maxfront.

Run with: python meeting_server.py
The browser can read the current meeting from any device that can reach this server.
"""

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
from urllib.parse import urlparse

HOST = "0.0.0.0"
PORT = 8787
DATA_FILE = Path(__file__).with_name("meeting.json")


def read_meeting():
    if not DATA_FILE.exists():
        return None
    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8")).get("meeting_time")
    except (OSError, json.JSONDecodeError):
        return None


def write_meeting(meeting_time):
    DATA_FILE.write_text(json.dumps({"meeting_time": meeting_time}), encoding="utf-8")


class MeetingHandler(BaseHTTPRequestHandler):
    def send_json(self, status, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, PUT, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_json(204, {})

    def do_GET(self):
        if urlparse(self.path).path == "/api/meeting":
            self.send_json(200, {"meeting_time": read_meeting()})
            return
        self.send_json(404, {"error": "Not found"})

    def do_PUT(self):
        if urlparse(self.path).path != "/api/meeting":
            self.send_json(404, {"error": "Not found"})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(length))
            meeting_time = payload.get("meeting_time", "")
            if meeting_time and not self.valid_time(meeting_time):
                raise ValueError
            write_meeting(meeting_time or None)
            self.send_json(200, {"meeting_time": meeting_time or None})
        except (ValueError, json.JSONDecodeError):
            self.send_json(400, {"error": "meeting_time must use HH:MM format"})

    def do_DELETE(self):
        if urlparse(self.path).path != "/api/meeting":
            self.send_json(404, {"error": "Not found"})
            return
        write_meeting(None)
        self.send_json(200, {"meeting_time": None})

    @staticmethod
    def valid_time(value):
        if len(value) != 5 or value[2] != ":":
            return False
        hour, minute = value.split(":")
        return hour.isdigit() and minute.isdigit() and 0 <= int(hour) <= 23 and 0 <= int(minute) <= 59

    def log_message(self, format, *args):
        print("%s - %s" % (self.address_string(), format % args))


if __name__ == "__main__":
    print(f"Maxfront meeting API listening on http://localhost:{PORT}")
    ThreadingHTTPServer((HOST, PORT), MeetingHandler).serve_forever()
