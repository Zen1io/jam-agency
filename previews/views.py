from django.shortcuts import render, redirect
from .forms import BillboardPreviewForm
from .models import BillboardPreview
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.conf import settings
from pathlib import Path

def billboard_preview(request):
    if request.method == 'POST':
        form = BillboardPreviewForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user

            # Новый путь к фону
            background_path = Path(settings.BASE_DIR) / 'media' / 'previews' / 'billboard_template.jpg'
            background = Image.open(background_path)
            overlay = Image.open(request.FILES['uploaded_design'])

            # Изменение размера и вставка
            overlay = overlay.resize((300, 200))  # масштаб под билборд
            background.paste(overlay, (150, 100))  # координаты вставки

            # Сохраняем результат
            buffer = BytesIO()
            background.save(fp=buffer, format='JPEG')
            file_name = 'preview_{}.jpg'.format(request.user.username)
            instance.result_preview.save(file_name, ContentFile(buffer.getvalue()))
            instance.save()

            return render(request, 'previews/preview_result.html', {'preview': instance})
    else:
        form = BillboardPreviewForm()
    return render(request, 'previews/upload_design.html', {'form': form})

