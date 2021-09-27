with open("photo.jpg", "rb")as f:
    print("State                                          | Output")
    print("-----------------------------------------------+------------------------------------------")
    print("Opening File...                                |")
    content = f.read()
    print("Searching the end of the JPG code format...    |")
    offset = content.index(bytes.fromhex("FFD9"))
    f.seek(offset + 2)
    print("Reading the text...                            |")

    print('                                               | The text is: "' + f.read().decode() + '"')
    print("Done                                           |")
