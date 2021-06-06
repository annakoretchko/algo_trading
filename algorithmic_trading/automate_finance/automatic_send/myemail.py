
#myemail.py
#!/Users/anna/anaconda3/envs/cron/bin/python3

from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from smtplib import SMTP
import smtplib
import sys
import pandas as pd
from email import encoders
from string import Template

import datetime as dt
import time
import smtplib
from datetime import datetime
from pretty_html_table import build_table

import automatic_send.secrets as secrets


def send_email(COMPX_df ,DJI_df, SPX_df,subject):

    message = daily_mover_email(COMPX_df ,DJI_df, SPX_df,subject)
    main_email(message)


def main_email(message):


    

    #message = MIMEMultipart()
    message['From'] = secrets.MAIL_USERNAME
    message['To'] = secrets.MAIL_USERNAME


    # This example assumes the image is in the current directory
    fp = open('/Users/anna/Dev/automate_finance/automate_finance/automatic_send/img/logo.png', 'rb')
    logoImage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    logoImage.add_header('Content-ID', '<image1>')

    


    signature = "\nAnna Koretchko\nE-mail: annakoretchko@gmail.com\nPhone: (863) 602-3282\n"
    html_sig = """ 

            <a href="https://anna-koretchko.ue.r.appspot.com/index">Website</a>

        """





    # always here
    signature = MIMEText(signature, 'plain')
    html_sig = MIMEText(html_sig, 'html')
   
    
    #always last part of every email
    message.attach(signature)
    message.attach(html_sig)
    message.attach(logoImage)
    

    msg_body = message.as_string()
    

    # email passwords etc/login
    email_user = secrets.MAIL_USERNAME
    server = smtplib.SMTP ('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, secrets.MAIL_PASSWORD)


    # send email
    server.sendmail(email_user, email_user, msg_body)
    server.quit()


def daily_mover_email(COMPX_df ,DJI_df, SPX_df,subject):

    message = MIMEMultipart()
    message['Subject'] = subject


    intro_text = "Hello,\nHere is the "+ subject +"\n"
    COMPX = "$COMPX"
    DJI = "$DJI"
    SPX = "\n$SPX.X"


    table_1 = build_table(SPX_df, 'blue_light')
    table_2 = build_table(DJI_df, 'green_light')
    table_3 = build_table(COMPX_df, 'orange_light')
  

    intro_text = MIMEText(intro_text, 'plain')
    title1 = MIMEText(SPX, 'plain')
    table_1 = MIMEText(table_1, 'html')
    title2 = MIMEText(DJI, 'plain')
    table_2 = MIMEText(table_2, 'html')
    title3 = MIMEText(COMPX, 'plain')
    table_3 = MIMEText(table_3, 'html')
    

    message.attach(intro_text)
    message.attach(title1)
    message.attach(table_1)
    message.attach(title2)
    message.attach(table_2)
    message.attach(title3)
    message.attach(table_3)



    return message




#     message = MIMEMultipart()
#     message['Subject'] = subject
#     message['From'] = secrets.MAIL_USERNAME
#     message['To'] = secrets.MAIL_USERNAME

#     output = build_table(df, 'blue_light')
#     body_content = output


#     # # to add an attachment is just add a MIMEBase object to read a picture locally.
#     # with open('/Users/anna/Dev/automate_finance/automate_finance/automatic_send/img/logo.png', 'rb') as f:
#     #     # set attachment mime and file name, the image type is png
#     #     mime = MIMEBase('image', 'png', filename='logo.png')
#     #     # add required header data:
#     #     #mime.add_header('Content-Disposition', 'attachment', filename='logo.png')
#     #     #mime.add_header('X-Attachment-Id', '0')
#     #     mime.add_header('Content-ID', '<0>')
#     #     # read attachment file content into the MIMEBase object
#     #     mime.set_payload(f.read())
#     #     # encode with base64
#     #     encoders.encode_base64(mime)
#         # add MIMEBase object to MIMEMultipart object
        
#     # message.attach(MIMEText(body_content, "html"))
#     # msg_body = message.as_string()

#     # This example assumes the image is in the current directory
#     fp = open('/Users/anna/Dev/automate_finance/automate_finance/automatic_send/img/logo.png', 'rb')
#     msgImage = MIMEImage(fp.read())
#     fp.close()

#     # Define the image's ID as referenced above
#     msgImage.add_header('Content-ID', '<image1>')
#     # message.attach(msgImage)
#     #msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>Nifty!', 'html')


#     text = "Hello,\nHere is the "+ subject

#     html = """\
#     <html>
#     <head></head>
#     <body>
        
    
        
#     </body>
#     </html>
#     """
#     signature = "Anna Koretchko\nE-mail: annakoretchko@gmail.com\nPhone: (863) 602-3282\n"
#     html_sig = """ 

#             <a href="https://anna-koretchko.ue.r.appspot.com/index">Website</a>

#         """

#     html3 = """\
#     <table border="1" >

# <tr>
#     <td>IMG left</td>
#     <td colspan="2">

#         your text that could be very long and usefull to your recipient<br><br>
#         you should encode the mail text for html within your python application<br><br>

#         otherwise you will have problems with newline and so on.
#     </td>
# <tr>
#     <td></td>
#     <td>IMG center</td>
#     <td>IMG rigth</td>
# </tr>
# </table>"""

#     part1 = MIMEText(text, 'plain')
#     part2 = MIMEText(html, 'html')
#     part3 = MIMEText(output, 'html')
#     part4 = msgImage
#     part5 = MIMEText(signature, 'plain')
#     part6 = MIMEText(html_sig, 'html')
#     part7 = MIMEText(html3, 'html')

#     # Attach parts into message container.
#     # According to RFC 2046, the last part of a multipart message, in this case
#     # the HTML message, is best and preferred.
#     message.attach(part1)
#     message.attach(part2)
#     message.attach(part3)
    
#     message.attach(part5)
#     message.attach(part6)
#     #message.attach(part7)
#     message.attach(part4)
    

#     msg_body = message.as_string()
    

#     email_user = secrets.MAIL_USERNAME
#     server = smtplib.SMTP ('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(email_user, secrets.MAIL_PASSWORD)



#     #EMAIL
#     # message = 'sending this from python!'
#     # message2 = "hey there"
#     # message = message +message2
#     server.sendmail(email_user, email_user, msg_body)
#     server.quit()