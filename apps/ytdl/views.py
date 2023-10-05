from django.shortcuts import render
from django.views.generic.edit import FormView
from apps.ytdl.forms import MailForm
from .tasks import download_and_convert_to_mp3
import os
from .tasks import send_email


# Create your views here.
class MailFormView(FormView):
    template_name = "index.html"
    form_class = MailForm
    success_url = "/thanks/"



    def form_valid(self, form):
        video_url = form.cleaned_data['url']
        email = form.cleaned_data['email']
        output_directory = "media"

        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        mp3_file_path = download_and_convert_to_mp3(video_url, output_directory)
        print(f"Видео успешно скачано и сохранено в папке {output_directory}")

        to_email = email
        send_email("Тема письма", "Текст сообщения", to_email, mp3_file_path)
        print(f"Аудиофайл успешно отправлен на адрес {to_email}")

        return super().form_valid(form)

def thank_you(request):
    return render(request, 'thanks.html')

def error(request):
    return render(request, 'error.html')
