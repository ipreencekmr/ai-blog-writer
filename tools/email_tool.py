import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition
import base64
from crewai.tools import tool

@tool
def send_email_tool(content: str) -> str:
    """
    Send the formatted blog post as an email attachment.
    """
    message = Mail(
        from_email=os.getenv('EMAIL_FROM'),
        to_emails=os.getenv('EMAIL_TO'),
        subject="Daily Tech Blog Post",
        html_content="<p>Please find the attached blog post.</p>"
    )

    encoded_content = base64.b64encode(content.encode('utf-8')).decode()

    attachment = Attachment(
        FileContent(encoded_content),
        FileName("blog_post.md"),
        FileType("text/markdown"),
        Disposition("attachment")
    )
    message.attachment = attachment

    try:
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        response = sg.send(message)
        return f"Email sent successfully. Status code: {response.status_code}"
    except Exception as e:
        return f"Error sending email: {e}"