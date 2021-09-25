write_text = b"Hello World"  # ←- Change this bytes to the text which should be written in the image
with open("photo.jpg", "r+b") as f:
    print("State                                          | Output")
    print("-----------------------------------------------+-------------------------------------")
    print("Opening File...                                |")
    content = f.read()
    print("Searching the end of the JPG code format...    |")
    offset = content.index(bytes.fromhex("FFD9"))
    f.seek(offset + 2)
    print("Deleting old text...                           |")
    f.truncate()
with open("photo.jpg", "ab") as f:
    print("                                               | Write " + str(write_text) + " in the photo")
    f.write(write_text)
    print("Done                                           |")
    