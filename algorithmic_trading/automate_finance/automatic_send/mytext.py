
#!/Users/anna/anaconda3/envs/cron/bin/python3

import smtplib
from pretty_html_table import build_table
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


import automatic_send.secrets as secrets

def send_text(message):

    # Establish a secure session with gmail's outgoing SMTP server using your gmail account
    server = smtplib.SMTP( "smtp.gmail.com", 587 )

    server.starttls()

    server.login( secrets.MAIL_USERNAME, secrets.MAIL_PASSWORD )


    # df = pd.DataFrame({'num_legs': [2, 4, 8, 0],
    #             'num_wings': [2, 0, 0, 0],
    #             'num_specimen_seen': [10, 2, 1, 8]},
    #             index=['falcon', 'dog', 'spider', 'fish'])

    # message = MIMEMultipart()
    # output = build_table(df, 'blue_light')
    # body_content = output
    # message.attach(MIMEText(body_content, "html"))
    # msg_body = message.as_string()
    # Send text message through SMS gateway of destination number
    server.sendmail( '<from>', secrets.CELL_NUMBER+'@vtext.com', message )
    server.quit()


