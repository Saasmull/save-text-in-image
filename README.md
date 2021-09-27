# save-text-in-image

This an example how to save and read any kind of text in an image with Python.

This Code writes the text binary in the image after the end bytes ```FF D9``` which are the same bytes as the start bytes.

You can check the the bytes with the programm [HxD20](https://mh-nexus.de/en/downloads.php?product=HxD20 "Download HxD20"). In this programm you can open the image file and at the end of the file you can see the text which was written in the image.

![HxD20](https://upload.wikimedia.org/wikipedia/en/0/02/HxD_screenshot.png)
>HxD20 ist for showing the bits of a file.

* **Please notice: The image file must be a .JPG file and can't be a PNG file with a changed extension. Otherwise will this Code show you an Error!**
