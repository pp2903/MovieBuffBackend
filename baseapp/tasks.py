import requests
from authentication.models import AppUser as User
from io import BytesIO
from celery import shared_task
from django.core.mail import EmailMessage
from xhtml2pdf import pisa
from django.template.loader import get_template
from baseapp.models import Fav, Movie, TVShow
import requests
from dotenv import dotenv_values


config = dotenv_values()


@shared_task
def generate_and_send_pdf():
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {config['TMDB_API_KEY']}",
    }
    # Generate HTML content dynamically within the task (optional)
    # You can use logic to dynamically generate the data for the template
    users = User.objects.filter(notifications_enabled=True)
    # Call the existing view function to render the HTML
    template = get_template("baseapp/favorites_template.html")
    for user in users:
        movie_data = []
        show_data = []
        data = {}
        movies = Fav.objects.filter(user=user, favorite_type="movie").values_list(
            "item_id", flat=True
        )
        shows = Fav.objects.filter(user=user, favorite_type="tvshow").values_list(
            "item_id", flat=True
        )

        for id in movies:
            movie = Movie.objects.get(id=id)
            movie_data.append(movie)
        for id in shows:
            show = TVShow.objects.get(id=id)
            show_data.append(show)

    data["movies"] = movie_data
    data["shows"] = show_data
    data["user"] = user
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
