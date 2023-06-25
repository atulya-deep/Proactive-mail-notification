import smtplib
def send_email(sender_email, receiver_email, subject, message):
    # SMTP server details for Gmail
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Sender's credentials (replace with your Gmail account details)
    sender_username = sender_email
    sender_password = "oggnnddiqbuvzmfr"

    # Create a secure connection to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_username, sender_password)

    # Compose the email
    email_message = f"Subject: {subject}\n\n{message}"

    try:
        # Send the email
        server.sendmail(sender_email, receiver_email, email_message)
        print("Email sent successfully!")
    except smtplib.SMTPException as e:
        print("An error occurred while sending the email:", str(e))
    finally:
        # Close the connection to the SMTP server
        server.quit()
