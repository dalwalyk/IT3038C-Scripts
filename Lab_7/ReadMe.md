# Image Processing using PIL

This script uses the Python Imaging Library (PIL) to perform basic image processing tasks on a given image file. Here's how to run it:

Setup
First, let's create a virtual environment for our script. You can call it whatever you like:
javascript

virtualenv ~/venv/image-processing
Activate the virtual environment:

```bash
source ~/venv/image-processing/bin/activate
```
Install the Pillow library:
```
pip install pillow
```
Usage
Find an image you want to use, and download it to your hard drive.

In Python, run the following code, replacing /full/path/to/image.jpg with the full path to your image file:

```python
from PIL import Image, ImageFilter
```

# Load the image
```
my_image = Image.open('/full/path/to/image.jpg')
my_image.load()
```

# Get format and size information
```
print(my_image.format)
print(my_image.size)
```

# Show the image
```my_image.show()```

# Apply a blur filter to the image and show the result
```blurred_image = my_image.filter(ImageFilter.BLUR)
blurred_image.show()
```

# Apply a color filter to the image and show the result
```filtered_image = my_image.convert('L')
filtered_image.show()
```
Deactivate the virtual environment when you're done:
```
deactivate
```

