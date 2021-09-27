write_text = input("Please enter the text: ")
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
    print('                                               | Write "' + write_text + '" in the photo')
    f.write(str.encode(write_text))
    print("Done                                           |")
    