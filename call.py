import pandas as pd
from twilio.rest import Client
import time


acc_sid = "ACfd3d4117b7dcbd08ade9d880c260f458"
auth_token ="769581eb06345cbb194606b9487ebd08"

client = Client(acc_sid, auth_token)

df = pd.read_excel("zenen.xlsx")

messages = {
    "student": "hi da",
    "staff": "good morning sir",
    "commander": "gokul reporting sir"
}

for i in range(len(df)):
    name = str(df.loc[i, "name"])
    desig = str(df.loc[i, "desig"])
    num = str(df.loc[i, "num"])

    msg = messages.get(desig.lower(), "hello")
    final_message = f"Dear {name}, {msg}"

    client.messages.create(
        to=f"whatsapp:{num}",
        from_="whatsapp:+14155238886",
        body=final_message
    )

    print(f"Message sent to {name} ({num})")
    time.sleep(1)