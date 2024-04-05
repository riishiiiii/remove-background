import os
import io
from PIL import Image
import requests
import rembg
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['POST'])
def remove_bg(request):
    if request.method == 'POST':
        image_url = request.data.get('image_url')
        parameters = request.data.get('parameters', {})

        try:
            response = requests.get(image_url)
            response.raise_for_status() 
            img_data = response.content

            output_img_data = rembg.remove(img_data)

            output_img = Image.open(io.BytesIO(output_img_data))

            output_dir = os.path.join(os.path.dirname(__file__), "static")
            os.makedirs(output_dir, exist_ok=True)

            output_filename = f"output_{request.data.get('image_name', 'image')}.png"
            output_img_path = os.path.join(output_dir, output_filename)
            output_img.save(output_img_path, 'PNG')

            protocol = 'https://' if request.is_secure() else 'http://'
            domain = request.get_host()
            static_url = os.path.join(domain, 'static', output_filename)
            output_img_url = f"{protocol}{static_url}"

            return JsonResponse({'output_img_url': output_img_url}, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error_message': f'Failed to download image from URL: {e}'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({'error_message': f'An error occurred: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return JsonResponse({'error_message': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)