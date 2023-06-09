import os
import requests
from PIL import Image, ImageDraw, ImageOps

def download_image(url, output_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(output_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        return True
    return False

def resize_image(input_path, output_path, size):
    with Image.open(input_path) as image:
        image.thumbnail(size)
        image.save(output_path)

def apply_watermark(input_path, output_path, watermark_path):
    with Image.open(input_path) as image:
        with Image.open(watermark_path) as watermark:
            watermark = watermark.convert("RGBA")
            watermark = watermark.resize(image.size)

            watermarked_image = Image.alpha_composite(image.convert("RGBA"), watermark)
            watermarked_image.save(output_path, "PNG")  # Save as PNG

def mass_download_resize_watermark(image_urls, output_folder, size, watermark_path):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i, url in enumerate(image_urls):
        output_filename = f'image_{i}.jpg'
        output_path = os.path.join(output_folder, output_filename)

        if download_image(url, output_path):
            resized_output_path = os.path.join(output_folder, f'resized_{output_filename}')
            resize_image(output_path, resized_output_path, size)

            watermarked_output_path = os.path.join(output_folder, f'watermarked_{output_filename}')
            apply_watermark(resized_output_path, watermarked_output_path, watermark_path)

            os.remove(output_path)
            os.remove(resized_output_path)

            print(f'Processed image {i+1}/{len(image_urls)}')
        else:
            print(f'Failed to download image {i+1}/{len(image_urls)}')

# Example usage
image_urls = [
'https://store.icrealtime.com/SSP%20Applications/NetSuite%20Inc.%20-%20SCS/SuiteCommerce%20Standard/img/product-images-2019/DVR-LOCK-BOX.media.01.jpg?resizeid=5&resizeh=600&resizew=600', 'https://store.icrealtime.com/SSP%20Applications/NetSuite%20Inc.%20-%20SCS/SuiteCommerce%20Standard/img/product-images-2019/DVR-LOCK-BOX.media.02.jpg?resizeid=5&resizeh=600&resizew=600', 'https://store.icrealtime.com/SSP%20Applications/NetSuite%20Inc.%20-%20SCS/SuiteCommerce%20Standard/img/product-images-2019/DVR-LOCK-BOX.media.03.jpg?resizeid=5&resizeh=600&resizew=600', 'https://store.icrealtime.com/SSP%20Applications/NetSuite%20Inc.%20-%20SCS/SuiteCommerce%20Standard/img/product-images-2019/DVR-LOCK-BOX.media.04.jpg?resizeid=5&resizeh=600&resizew=600', 'https://store.icrealtime.com/SSP%20Applications/NetSuite%20Inc.%20-%20SCS/SuiteCommerce%20Standard/img/product-images-2019/DVR-LOCK-BOX-LG.media.01.jpg?resizeid=5&resizeh=600&resizew=600', 'https://store.icrealtime.com/SSP%20Applications/NetSuite%20Inc.%20-%20SCS/SuiteCommerce%20Standard/img/product-images-2019/DVR-LOCK-BOX-LG.media.02.jpg?resizeid=5&resizeh=600&resizew=600', 'https://store.icrealtime.com/SSP%20Applications/NetSuite%20Inc.%20-%20SCS/SuiteCommerce%20Standard/img/product-images-2019/DVR-LOCK-BOX-LG.media.03.jpg?resizeid=5&resizeh=600&resizew=600', 'https://store.icrealtime.com/SSP%20Applications/NetSuite%20Inc.%20-%20SCS/SuiteCommerce%20Standard/img/product-images-2019/DVR-LOCK-BOX-LG.media.04.jpg?resizeid=5&resizeh=600&resizew=600', 'https://store.icrealtime.com/SSP%20Applications/NetSuite%20Inc.%20-%20SCS/SuiteCommerce%20Standard/img/product-images-2019/DVR-LOCK-BOX-SM.media.01.jpg?resizeid=5&resizeh=600&resizew=600', 'https://store.icrealtime.com/SSP%20Applications/NetSuite%20Inc.%20-%20SCS/SuiteCommerce%20Standard/img/product-images-2019/DVR-LOCK-BOX-SM.media.02.jpg?resizeid=5&resizeh=600&resizew=600', 'https://store.icrealtime.com/SSP%20Applications/NetSuite%20Inc.%20-%20SCS/SuiteCommerce%20Standard/img/product-images-2019/DVR-LOCK-BOX-SM.media.03.jpg?resizeid=5&resizeh=600&resizew=600', 'https://store.icrealtime.com/SSP%20Applications/NetSuite%20Inc.%20-%20SCS/SuiteCommerce%20Standard/img/product-images-2019/MNT-BOX%202.media.01.jpg?resizeid=5&resizeh=600&resizew=600', 'https://store.icrealtime.com/SSP%20Applications/NetSuite%20Inc.%20-%20SCS/SuiteCommerce%20Standard/img/product-images-2019/MNT-BOX%202.media.02.jpg?resizeid=5&resizeh=600&resizew=600', 'https://store.icrealtime.com/SSP%20Applications/NetSuite%20Inc.%20-%20SCS/SuiteCommerce%20Standard/img/product-images-2019/MNT-BOX%202.media.03.jpg?resizeid=5&resizeh=600&resizew=600', 'https://store.icrealtime.com/SSP%20Applications/NetSuite%20Inc.%20-%20SCS/SuiteCommerce%20Standard/img/product-images-2019/MNT-BOX%202.media.04.jpg?resizeid=5&resizeh=600&resizew=600', 'https://store.icrealtime.com/SSP%20Applications/NetSuite%20Inc.%20-%20SCS/SuiteCommerce%20Standard/img/product-images-2019/MNT-BOX-B.media.01.jpg?resizeid=5&resizeh=600&resizew=600', 'https://store.icrealtime.com/SSP%20Applications/NetSuite%20Inc.%20-%20SCS/SuiteCommerce%20Standard/img/product-images-2019/MNT-BOX-B.media.02.jpg?resizeid=5&resizeh=600&resizew=600', 'https://store.icrealtime.com/SSP%20Applications/NetSuite%20Inc.%20-%20SCS/SuiteCommerce%20Standard/img/product-images-2019/MNT-BOX-B.media.03.jpg?resizeid=5&resizeh=600&resizew=600', 'https://store.icrealtime.com/SSP%20Applications/NetSuite%20Inc.%20-%20SCS/SuiteCommerce%20Standard/img/product-images-2019/MNT-BOX-B.media.04.jpg?resizeid=5&resizeh=600&resizew=600', 'https://store.icrealtime.com/SSP%20Applications/NetSuite%20Inc.%20-%20SCS/SuiteCommerce%20Standard/img/product-images-2019/MNT-BOX-B.media.05.jpg?resizeid=5&resizeh=600&resizew=600', 'https://store.icrealtime.com/SSP%20Applications/NetSuite%20Inc.%20-%20SCS/SuiteCommerce%20Standard/img/product-images-2019/MNT-BOX-MPA120.media.01.jpg?resizeid=5&resizeh=600&resizew=600'
]
output_folder = 'D:\Apps\Python Tool Scripts\Python Mass Image Download_Resize_Watermark\Post Edit Images'
size = (600, 600)
watermark_path = 'D:\Apps\Python Tool Scripts\Python Mass Image Download_Resize_Watermark\Watermark\Preorder-Model-Banner.png'

mass_download_resize_watermark(image_urls, output_folder, size, watermark_path)
