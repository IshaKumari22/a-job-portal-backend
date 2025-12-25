
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Resume 
from .utils import extract_text_from_pdf
@receiver(post_save, sender=Resume)
def my_handler(sender, instance, created, **kwargs):
    if instance.resume_file:
        try:
            text=extract_text_from_pdf(instance.resume.file.path)
            instance.extracted_text=text
            instance.save(update_fields=["extracted_text"])
        except Exception as e:
            print("Resume extraction error:",e)