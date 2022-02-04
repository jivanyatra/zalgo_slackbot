from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from zalgolibpy import enzalgofy, dezalgofy

# Install the Slack app and get xoxb- token in advance
app = App(token=SLACK_BOT_TOKEN,
          signing_secret=SIGNING_SECRET)

@app.command("/enzalgofy")
def convert_to_zalgo(ack, respond, command):
    # Acknowledge command request
    ack()
    respond(f"{enzalgofy(command['text'])}")

@app.command("/dezalgofy")
def convert_from_zalgo(ack, respond, command):
    # Acknowledge command request
    ack()
    respond(f"{dezalgofy(command['text'])}")

if __name__ == "__main__":
    load_dotenv()
    SocketModeHandler(app, SLACK_APP_TOKEN).start()