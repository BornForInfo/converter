import os
import smtplib
import imghdr
from email.message import EmailMessage
import secrets
from flask import Flask, request, render_template


app = Flask(__name__)

# In a real-world scenario, you would use a database to store tokens and user information.
# This is just a simple in-memory storage for the sake of the example.
token_storage = set()

@app.route('/verify', methods=['GET'])
def verify():
    token = request.args.get('token')

    if token:
        if token in token_storage:
            # Token is valid, mark the user as verified in your database
            # Here you would typically update your user database to mark the user as verified
            # For simplicity, we'll just print a message here
            print(f"User with token {token} verified!")
        else:
            print(f"Invalid token: {token}")
    else:
        print("Token not provided in the request.")

    # You can render an HTML page to inform the user about the verification status
    return render_template('verification_status.html', token=token)

if __name__ == '__main__':
    app.run(debug=True)


# Flask server endpoint for verification
VERIFY_ENDPOINT = 'http://127.0.0.1:5000/verify'

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

# Function to generate a random token
def generate_token():
    return secrets.token_urlsafe(16)


#contacts = ['YourAddress@gmail.com', 'test@example.com']
receiver = EMAIL_ADDRESS
msg = EmailMessage()
msg['Subject'] = 'Check out Bronx as a puppy!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = receiver

# Generate a unique token for this email
token = generate_token()

# Add the token to the email content
verification_link = f'https://yourdomain.com/verify?token={token}'
msg.set_content(f'This is a plain text email. Click here to verify: {verification_link}')

# Save the token and associate it with the user in your database (in-memory storage for simplicity)
#token_storage.add(token)

msg.add_header(EMAIL_ADDRESS , '123')
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)