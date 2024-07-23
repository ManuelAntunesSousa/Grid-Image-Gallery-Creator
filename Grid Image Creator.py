from PIL import Image
import os


image_folder = r'C:\Users\Manu\Dropbox\ETSY\Full W'  # Use a raw string
images = [os.path.join(image_folder, file) for file in os.listdir(image_folder) if file.endswith(('png', 'jpg', 'jpeg'))]


num_images = len(images)
grid_size = (15, 10)  # 15 columns and 10 rows


thumbnail_size = (100, 100)  # Adjust this as needed
images_resized = []

for img_path in images:
    img = Image.open(img_path)
    img.thumbnail(thumbnail_size)
    images_resized.append(img)

#Grid image
grid_image = Image.new('RGB', (thumbnail_size[0] * grid_size[0], thumbnail_size[1] * grid_size[1]))

for idx, img in enumerate(images_resized):
    row = idx // grid_size[0]
    col = idx % grid_size[0]
    grid_image.paste(img, (col * thumbnail_size[0], row * thumbnail_size[1]))

# Save the final grid image
grid_image.save('grid_image.jpg')
grid_image.show()
