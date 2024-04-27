import boto3

def send_email():
    # Set up AWS credentials directly (not recommended for production)
    aws_access_key_id = 'AKIA25T6P2GFFEBD4CO7'
    aws_secret_access_key = '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'
    aws_region = 'us-east-1'

    # Initialize the SES client
    ses_client = boto3.client('ses', region_name=aws_region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    # Set up the email parameters
    sender = 'info@elogicals.com'
    recipient = 'pradnyesh.shembavanekar@elogicals.com'
    subject = 'Test Email'
    body_text = 'This is a test email.'
    body_html = '<html><body><h1>Test Email</h1><p>This is a test email.</p></body></html>'

    # Send the email
    try:
        response = ses_client.send_email(
            Source=sender,
            Destination={'ToAddresses': [recipient]},
            Message={
                'Subject': {'Data': subject},
                'Body': {
                    'Text': {'Data': body_text},
                    'Html': {'Data': body_html}
                }
            }
        )
        print("Email sent! Message ID:", response['MessageId'])
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    send_email()
