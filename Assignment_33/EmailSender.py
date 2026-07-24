"""
Module Name : EmailSender.py

Description :
This module sends the generated log file
as an email attachment.
"""

import smtplib
import os

from email.message import EmailMessage


#----------------------------------------------------------
# Function Name : SendEmail
# Description   : Sends log file through email
#----------------------------------------------------------

def SendEmail(SenderEmail,
              AppPassword,
              ReceiverEmail,
              LogFilePath):

    try:

        # Create Email Object
        Message = EmailMessage()

        Message["Subject"] = "Duplicate File Removal Report"
        Message["From"] = SenderEmail
        Message["To"] = ReceiverEmail

        Body = """
Hello,

Duplicate File Removal operation has completed successfully.

Please find the attached log file.

Thank You.
"""

        Message.set_content(Body)

        # Attach Log File
        fd = open(LogFilePath, "rb")

        FileData = fd.read()

        fd.close()

        FileName = os.path.basename(LogFilePath)

        Message.add_attachment(
            FileData,
            maintype="application",
            subtype="octet-stream",
            filename=FileName
        )

        # Connect to Gmail SMTP
        Server = smtplib.SMTP("smtp.gmail.com", 587)

        Server.starttls()

        Server.login(SenderEmail, AppPassword)

        Server.send_message(Message)

        Server.quit()

        print("\nEmail Sent Successfully.")

    except Exception as e:

        print("\nUnable to send email.")
        print("Reason :", e)