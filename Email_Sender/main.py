import smtplib
import ssl

# Server setup
host = "smtp.gmail.com"
port = 465

# Email credentials (ensure to use environment variables or a secure method to store sensitive info)
username = "gauravpande568@gmail.com"
password = "ezek fdzy ogno cnti"

# Collect input
receiver = input("Enter receiver's email: ")
subject = input("Enter the subject: ")
body = input("Enter your message: ")

# Construct the full message with subject and body
message = f"Subject: {subject}\n\n{body}"

# Create a secure SSL context
context = ssl.create_default_context()

# Sending the email
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)

print("Email sent successfully.")
