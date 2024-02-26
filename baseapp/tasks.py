import requests
from authentication.models import AppUser as User
from io import BytesIO
from celery import shared_task
from django.core.mail import EmailMessage
from xhtml2pdf import pisa
from django.template.loader import get_template
from baseapp.models import Fav, Movie, TVShow
import requests


@shared_task
def generate_and_send_pdf():
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwODcwMTA2YmQ2ZmY4YjVhOGQ5Mzg4MDlhZGU3NGQzNCIsInN1YiI6IjY1NzkzNzlmNTY0ZWM3MDBjNDc0OTJlMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.tonKVBmTGW0dsX35lZSG-TyXAov0VLNregJFcJnkhGg",
    }
    # Generate HTML content dynamically within the task (optional)
    # You can use logic to dynamically generate the data for the template
    users = User.objects.filter(notifications_enabled=True)
    # Call the existing view function to render the HTML
    template = get_template("baseapp/favorites_template.html")

    for user in users:

        data = {}

        

        movies = Fav.objects.filter(user=user,favorite_type="movie").values_list('item_id',flat=True)
        shows = Fav.objects.filter(user=user,favorite_type="tvshow").values_list('item_id',flat=True)
        data['movies'] = movies
        data['shows'] = shows
        data['user'] = user
        context = data  # Update context as needed
        html = template.render(context)

        # Create a byte buffer for the PDF
        result = BytesIO()

        # Generate PDF using pisa
        pisa.CreatePDF(html, result)

        # Extract PDF content from the buffer
        pdf_content = result.getvalue()

        # Prepare email message with PDF attachment
        email = EmailMessage(
            subject="Your Weekly Report (PDF)",
            body="Here are your favorite movies !!",
            from_email="priyampranshu2903@gmail.com",
            to=[user.email],  # Replace with recipient email
        )
        email.attach("report.pdf", pdf_content)

        # Send the email
        email.send()

        return "PDF generated and sent successfully!"
