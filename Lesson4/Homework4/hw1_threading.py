import os
import threading
import requests
import time

urls = [
    'http://photokeep.ru/images/content/spravochnik/fajlovye-formaty/jpeg-05.jpg',
    'https://fotogora.ru/img/Peter%20Majkut.jpg',
    'https://wp-s.ru/wallpapers/9/1/547422858285832/grand-kanon-v-arizone-ssha.jpg',
    'https://images.wallpapershq.com/wallpapers/67/wallpaper_67_1080x1920.jpg',
]

all_time_load = 0.0


def download_image(url_images):
    global all_time_load
    response = requests.get(url_images)
    image_name = url_images.split('/')[-1]
    image_path = os.path.join('images', image_name)
    all_time_load += time.time() - start_time
    with open(image_path, 'wb') as file:
        file.write(response.content)
    print(f'\nLoading: {url_images}')
    print(f"Loaded: {image_name} \nuploaded for: {time.time() - start_time:.2f}s")


threads = []
start_time = time.time()

for url in urls:
    thread = threading.Thread(target=download_image, args=[url])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"\nAll time uploaded: {all_time_load:.2f}s")
