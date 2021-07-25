

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACddc2f6471a93bb946ca5cb1bd0168ef8"
# Your Auth Token from twilio.com/console
auth_token  = "2001ce065239f48d8e1f6e4aff6430bb"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+919872969848",
    from_="+18084007178",
    body="Hello!")

print(message.sid)
