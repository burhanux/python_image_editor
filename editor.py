from PIL import Image, ImageEnhance, ImageFilter
import os

pathI = './images' # Original Images Path
pathO = './editedImages' # Edited Images Path

for filename in os.listdir(pathI):
	img = Image.open(f"{pathI}/{filename}")
	edit = img.filter(ImageFilter.SHARPEN)
	factor = 1.5
	enhancer = ImageEnhance.Contrast(edit)
	edit = enhancer.enhance(factor)
	cleanName  = os.path.splitext(filename)[0]
	edit.save(f'{pathO}/{cleanName}_edited.jpg')