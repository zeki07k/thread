import asyncio
import time
import aiohttp
import concurrent.futures
async def download_image(img_url):
    async with session.get(url) as response:
        img_bytes = requests.get(img_url).content
        img_name = img_url.split(‘/’)[3]
        img_name = f’{img_name}.jpg’
        with open(img_name, ‘wb’) as img_file:
            img_file.write(img_bytes)
            print(f’{img_name} was downloaded...’)
async def download_all_images(images):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in images:
            task = asyncio.ensure_future(download_image(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)
def asyc_tasks(images):
    asyncio.get_event_loop().run_until_complete(download_all_images(images))
def chunks(lst, n):
    “”"Yield successive n-sized chunks from lst.“”"
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
if __name__ == “__main__“:
    images = [
            ‘https://images.unsplash.com/photo-1516117172878-fd2c41f4a759’,
            ‘https://images.unsplash.com/photo-1532009324734-20a7a5813719’,
            ‘https://images.unsplash.com/photo-1524429656589-6633a470097c’,
            ‘https://images.unsplash.com/photo-1530224264768-7ff8c1789d79’,
            ‘https://images.unsplash.com/photo-1564135624576-c5c88640f235’,
            ‘https://images.unsplash.com/photo-1541698444083-023c97d3f4b6’,
            ‘https://images.unsplash.com/photo-1522364723953-452d3431c267’,
            ‘https://images.unsplash.com/photo-1513938709626-033611b8cc03’,
            ‘https://images.unsplash.com/photo-1507143550189-fed454f93097’,
            ‘https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e’,
            ‘https://images.unsplash.com/photo-1504198453319-5ce911bafcde’,
            ‘https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99’,
            ‘https://images.unsplash.com/photo-1516972810927-80185027ca84’,
            ‘https://images.unsplash.com/photo-1550439062-609e1531270e’,
            ‘https://images.unsplash.com/photo-1549692520-acc6669e2f0c’
        ]
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
        futures = [executor.submit(asyc_tasks, s) for s in chunks(images, 8)]
        for future in concurrent.futures.as_completed(futures):
            pass
    duration = time.time() - start_time
    print(f”Downloaded {len(images)} images in {duration} seconds”)