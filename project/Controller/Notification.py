from django.core.mail import send_mail, EmailMultiAlternatives 
from django.conf import settings


def Send_email(lead):
        send_mail(
            subject="New Lead Created",
            message=f"""
        A new lead has been created.

        Name: {lead.name}
        Email: {lead.email}
        Phone: {lead.phone}
        Source: {lead.source}
        Status: {lead.status}
        """,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=settings.RECIPIENT_LIST,
            fail_silently=False,
        )


def Update_email(lead):
        email = EmailMultiAlternatives(
            subject="Lead Updated",
            body=f"""
            Lead details have been updated.

            Name: {lead.name}
            Email: {lead.email}
            Phone: {lead.phone}
            Source: {lead.source}
            Status: {lead.status}
            """,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=settings.RECIPIENT_LIST,
        )

        html_content = f"""
        <h2>Lead Updated</h2>

        <table border="1" cellpadding="8" cellspacing="0">
            <tr><th>Name</th><td>{lead.name}</td></tr>
            <tr><th>Email</th><td>{lead.email}</td></tr>
            <tr><th>Phone</th><td>{lead.phone}</td></tr>
            <tr><th>Source</th><td>{lead.source}</td></tr>
            <tr><th>Status</th><td>{lead.status}</td></tr>
        </table>
        """

        

        email.attach_alternative(html_content, "text/html")
        email.send()
