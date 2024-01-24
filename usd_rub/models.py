from django.db import models

class UsdRub(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    value = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f"{self.pk} {self.time} {self.value}"