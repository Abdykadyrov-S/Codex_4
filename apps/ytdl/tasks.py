import yt_dlp
import os
import smtplib
from email.message import EmailMessage

def download_and_convert_to_mp3(url, output_directory):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_directory, '%(title)s.%(ext)s'),
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        video_title = info_dict.get('title', 'video')

        ydl.download([url])

    return os.path.join(output_directory, f"{video_title}.mp3")

def send_email(subject, body, to_email, attachment_path):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = 'abdykadyrovsyimyk0708@gmail.com'  # Replace with your email address
    msg['To'] = to_email

    with open(attachment_path, 'rb') as file:
        msg.add_attachment(file.read(), maintype='audio', subtype='mp3', filename=os.path.basename(attachment_path))

    # Setup your email server and send the email
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Replace with your email provider's SMTP server and port
    server.starttls()
    server.login('abdykadyrovsyimyk0708@gmail.com', 'hoslbzoixgdjjwox')  # Replace with your email address and password
    server.send_message(msg)
    server.quit()