# models.py
from django.db import models
from django.contrib.auth.models import User

class BillboardPreview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_design = models.ImageField(upload_to='uploads/designs/')
    result_preview = models.ImageField(upload_to='previews/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)