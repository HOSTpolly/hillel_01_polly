import os
import threading
import time

import requests

encryption_counter = 0
download_counter = 0


# CPU-bound task (heavy computation)
def encrypt_file(image_url: str):
    global encryption_counter
    print(f"Processing image from {image_url} in process {os.getpid()}")
    start_time = time.perf_counter()
    # Simulate heavy computation by sleeping for a while
    _ = [i for i in range(100_000_000)]
    end_time = time.perf_counter()
    encryption_counter = end_time - start_time
    print(f"Encryption task took {encryption_counter} seconds")


# I/O-bound task (downloading image from URL)


def download_image(image_url):
    global download_counter
    print(f"Downloading image from {image_url} in thread {threading.current_thread().name}")
    start_time = time.perf_counter()
    response = requests.get(image_url)
    with open("image.jpg", "wb") as f:
        f.write(response.content)
    end_time = time.perf_counter()
    download_counter = end_time - start_time
    print(f"Download task took {download_counter} seconds")


try:
    encrypt_file("rockyou.txt")
    download_image("https://picsum.photos/1000/1000")
    total = encryption_counter + download_counter
    print(f"Time taken for encryption task: {encryption_counter}")
    print(f"  I/O-bound task: {download_counter}, Total: {total} seconds")
except Exception as e:
    print(f"Error occurred: {e}")
