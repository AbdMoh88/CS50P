import sys
from PIL import Image, ImageOps
import os


if len(sys.argv) == 3:
    extensions = [".jpeg", ".jpg", ".png"]
    input = os.path.splitext(sys.argv[1])[1].lower()
    output = os.path.splitext(sys.argv[2])[1].lower()
    if input == output and input in extensions and output in extensions:
        try:
            pup_image = Image.open(sys.argv[1])
        except FileNotFoundError:
            sys.exit("File does not exist")
        cs50_shirt = Image.open("shirt.png")
        size = cs50_shirt.size
        pup_image = ImageOps.fit(pup_image, size)
        pup_image.paste(cs50_shirt, cs50_shirt)
        pup_image.save(sys.argv[2])
    elif input == output and input not in extensions or output not in extensions:
        sys.exit("unsupported file extension")
    elif input != output:
        sys.exit("files extension don't match")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
