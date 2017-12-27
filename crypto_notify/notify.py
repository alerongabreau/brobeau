from sendgrid.helpers.mail import *
from sendgrid import *
import datetime

def send_alert(to_addr, exchange_pair, spot_price):
    mail = Mail()

    mail.from_email = Email("alert@cb-spotter.net", "cb-spotter")
    mail.subject = "Alert for {} :: X Price Below ${}".format(exchange_pair, spot_price)

    mail.template_id = "0pla3k5la-07bm-15ll-92az-10ja9gui1k22"

    current_time = datetime.datetime.new()

    personalization = Personalization()
    personalization.add_to(to_addr)
    personalization.add_substitution("%current_time%", current_time)
    personalization.add_substitution("%exchange_pair%", exchange_pair)
    personalization.add_substitution("%spot_price%", spot_price)

    mail.add_personalization(personalization)

    sg = SendGridAPIClient(username=os.environ.get('SG_USERNAME'),
                           password=os.environ.get('SG_PASSWORD')
                           )
    try:
        response = sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        print(response.headers)
        print(response.body)
    except:
        Exception("Mail not sent")

    return
