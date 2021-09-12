import pya3rt

apikey = "DZZun7AGQ9C7VYpDqsQWffXWg4xaMGQd"
client = pya3rt.TalkClient(apikey)
reply_message = client.talk("いい天気ですね")
print(reply_message["results"][0]["reply"])

