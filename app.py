from flask import Flask, render_template, send_from_directory, request
import uuid
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    # Replace this UUID with a dynamic one if you want per-user tracking
    tracking_id = "43365a99-08d8-49f3-8260-e3f7d6109354"
    return render_template("index.html", tracking_id=tracking_id)

@app.route("/track/<tracker_id>")
def track(tracker_id):
    with open("tracker_log.txt", "a") as f:
        f.write(f"Tracked: {tracker_id} at {datetime.datetime.now()} from IP: {request.remote_addr}\n")
    return send_from_directory('static', '1x1.png')

if __name__ == "__main__":
    app.run(debug=True)
