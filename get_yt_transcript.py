from flask import Flask, jsonify
from youtube_transcript_api import YouTubeTranscriptApi


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index() -> str:
    return "This is yt transcript api powered by zappa 😘"


@app.route("/<video_id>/transcript", methods=["GET"])
def get_yt_transcript(video_id: str):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return jsonify({"transcript": transcript})


# For dev environment
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8000)
