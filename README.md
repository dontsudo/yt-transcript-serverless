# yt-transcript-serverless 👻

- Here is an example:

```curl
# https://www.youtube.com/watch?v=NCtzkaL2t_Y
# video_id => NCtzkaL2t_Y

$ curl http://localhost:8000/NCtzkaL2t_Y/transcript
{
  "transcript": [
    {
      "duration": 3.167,
      "start": 0.961,
      "text": "(\"Don't Let Me Down\")"
    },
    {
      "duration": 5.0,
      "start": 5.022,
      "text": "\u266a Don't let me down \u266a"
    },
    {
      "duration": 5.0,
      "start": 11.08,
      "text": "\u266a Don't let me down \u266a"
    },
    {
      "duration": 5.0,
      "start": 17.027,
      "text": "\u266a Don't let me down \u266a"
    },
    ...
  ]
}
```
