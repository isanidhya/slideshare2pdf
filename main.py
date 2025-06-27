import requests
from bs4 import BeautifulSoup
import re
import os
from PIL import Image
import shutil
from io import BytesIO
from tqdm import tqdm

url = input(print("Enter Your URL: "))
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img',  class_='vertical-slide-image')


def get_best_quality_image(img_tag):
    srcset = img_tag.get('srcset', '')
    
    if not srcset:
        return img_tag.get('src')  
    
    entries = srcset.split(',')

    width_url_pairs = []
    for entry in entries:
        parts = entry.strip().split()
        if len(parts) == 2:
            url, width = parts
            width_value = int(width.replace('w', ''))
            width_url_pairs.append((width_value, url))

    # Return the URL with the highest width
    if width_url_pairs:
        return max(width_url_pairs, key=lambda x: x[0])[1]
    else:
        return img_tag.get('src')  # fallback

slides_urls = []
for img in img_tags:
    best_url = get_best_quality_image(img)
    slides_urls.append(best_url)



def online():
    images = []

    for url in tqdm(slides_urls, desc="Processing Slides"):
        res = requests.get(url)
        if res.status_code == 200:
            img = Image.open(BytesIO(res.content)).convert("RGB")
            images.append(img)
        else:
            print(f"Failed to load {url}")

    # Save to PDF (if at least one image was successfully loaded)
    if images:
        images[0].save("slides_from_urls.pdf", save_all=True, append_images=images[1:])
        print("PDF created from URL images.")
    else:
        print("No images loaded.")




def offline():
    # Create a folder to store downloaded images
    folder_name = "slides"
    os.makedirs(folder_name, exist_ok=True)

    # Download and save each image

    for idx, url in tqdm(enumerate(slides_urls), desc="Downloading Slides", total=len(slides_urls)):
        response = requests.get(url)
        
        if response.status_code == 200:
            filename = f"{folder_name}/slide_{idx + 1}.jpg"
            with open(filename, 'wb') as f:
                f.write(response.content)
        else:
            print(f"Failed to download: {url}")


    folder_name = "slides"

    def extract_number(filename):
        # Finds the number in 'slide_1.jpg' etc.
        match = re.search(r'slide_(\d+)\.jpg', filename)
        return int(match.group(1)) if match else float('inf')  # put invalid ones at the end

    # List all .jpg files and sort them numerically
    image_files = sorted(
        [f for f in os.listdir(folder_name) if f.endswith('.jpg')],
        key=extract_number
    )

    # Full path for each image
    image_paths = [os.path.join(folder_name, f) for f in image_files]

    # Open all images and convert them to RGB
    images = [Image.open(img_path).convert('RGB') for img_path in image_paths]

    # Save as a single PDF
    if images:
        output_path = "slide_presentation.pdf"
        images[0].save(output_path, save_all=True, append_images=images[1:])
        print(f"PDF saved as: {output_path}")
        shutil.rmtree(folder_name)

    else:
        print("No images found to convert.")



try:
    num = int(input("Enter \nonline : 1\noffline : 0\n"))
    if num == 1:
        online()
    elif num == 0:
        offline()
    else:
        print("Error: Enter 1 or 0")
except ValueError:
    print("Please enter a number (1 or 0)")