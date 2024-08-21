from django.db import models

class About(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    about = models.TextField(verbose_name="About")
    description = models.TextField(verbose_name="Description")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About Sections"
