import multiprocessing
import os
from multiprocessing import Process
import requests
import time

urls = [
    'http://photokeep.ru/images/content/spravochnik/fajlovye-formaty/jpeg-05.jpg',
    'https://fotogora.ru/img/Peter%20Majkut.jpg',
    'https://wp-s.ru/wallpapers/9/1/547422858285832/grand-kanon-v-arizone-ssha.jpg',
    'https://images.wallpapershq.com/wallpapers/67/wallpaper_67_1080x1920.jpg',
]
all_time_load = multiprocessing.Value('f', 0.0)


def download_image(url_images, all_time_load: {all_time_load.get_lock, all_time_load.value}):
    response = requests.get(url_images)
    image_name = url_images.split('/')[-1]
    image_path = os.path.join('images', image_name)
    with open(image_path, 'wb') as file:
        file.write(response.content)
    with all_time_load.get_lock():
        all_time_load.value += time.time() - start_time
    print(f'\nLoading: {url_images}')
    print(f"Loaded: {image_name} \nuploaded for: {time.time() - start_time:.2f}s")


processes = []
start_time = time.time()

if __name__ == '__main__':

    for url in urls:
        process = Process(target=download_image, args=(url, all_time_load))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f"\nAll time uploaded: {all_time_load.value:.2f}s")
