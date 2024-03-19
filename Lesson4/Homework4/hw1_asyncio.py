import asyncio
import os

import aiofiles as aiofiles
import aiohttp
import time

urls = [
    'http://photokeep.ru/images/content/spravochnik/fajlovye-formaty/jpeg-05.jpg',
    'https://fotogora.ru/img/Peter%20Majkut.jpg',
    'https://wp-s.ru/wallpapers/9/1/547422858285832/grand-kanon-v-arizone-ssha.jpg',
    'https://images.wallpapershq.com/wallpapers/67/wallpaper_67_1080x1920.jpg',
]

all_time_load = 0.0


async def download_images(url_images):
    global all_time_load
    async with aiohttp.ClientSession() as session:
        async with session.get(url_images) as response:
            image_name = url_images.split('/')[-1]
            image_path = os.path.join('images', image_name)
            async with aiofiles.open(image_path, 'wb') as file:
                content = await response.read()
                await file.write(content)
            all_time_load += time.time() - start_time
            print(f'\nLoading: {url_images}')
            print(f"Loaded: {image_name} \nuploaded for: {time.time() - start_time:.2f}s")


async def main():
    tasks = []
    for url in urls:
        task = asyncio.create_task(download_images(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


start_time = time.time()

if __name__ == '__main__':
    asyncio.run(main())
    print(f"\nAll time uploaded: {all_time_load:.2f}s")
