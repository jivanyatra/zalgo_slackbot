from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Install the Slack app and get xoxb- token in advance
app = App(token=SLACK_BOT_TOKEN,
          signing_secret=SIGNING_SECRET)

if __name__ == "__main__":
    load_dotenv()
    SocketModeHandler(app, SLACK_APP_TOKEN).start()