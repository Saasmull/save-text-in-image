# save-text-in-image

This an example how to save and read any kind of text in a image with Python.

This Code writes the text binary in the image after the end bytes ```FF D9``` which are the same bytes as the start bytes.

You can check the the bytes with the programm HxD. In this programm you can open the image file and at the end you can see the text which was written in the image.

**Please notice: The image file must be a .JPG file and can't be a PNG file with a changed extension. Otherwise will this Code show you an Error!**
