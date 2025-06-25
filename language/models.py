from django.db import models

class LanguagePreference(models.Model):
    session_id = models.CharField(max_length=100, unique=True)
    language = models.CharField(max_length=10, choices=[('ru', 'Русский'), ('uz', "O'zbekcha")])

    def __str__(self):
        return f"{self.session_id} - {self.language}"
