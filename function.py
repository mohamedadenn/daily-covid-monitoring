from twilio.rest import Client
from covid import Covid

# Your Account SID from twilio.com/console
account_sid = "<your account_sid here>"
# Your Auth Token from twilio.com/console
auth_token  = "<your auth token here>"

# Number to Send Message to: If you want to send to mulitple numbers leave it in a list, otherwise
# you can just use a string here and remove the loop from line 15.
outbound_num = ["whatsapp:<OUTBOUND_NUM1>","whatsapp:<OUTBOUND_NUM2>","whatsapp:<OUTBOUND_NUM3>" ] 

# Helper function that sends the WhatsApp Message
def send_whatsapp_message(msg):
    for num in outbound_num:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
        to=num, 
        from_="whatsapp:<YOUR TWILIO NUMBER>",
        body=msg)

def main():
    covid = Covid(source="worldometers")
    stats = covid.get_status_by_country_name("canada")
    country = stats["country"]
    active_cases = stats["active"]
    msg = f"There are currently {active_cases} active COVID cases in {country}." 
    print("Sending WhatsApp message now...")
    try:
        send_whatsapp_message(msg)
        print("Message was sent successfully!")
    except:
        print("An Error has occured")

if __name__ == '__main__':
    main()