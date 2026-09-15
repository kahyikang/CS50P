import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

else:
    valid_format = [".jpg", ".png", ".jpeg"]
    before = sys.argv[1].lower()
    after = sys.argv[2].lower()
    ex_before = os.path.splitext(before)[1]
    ex_after = os.path.splitext(after)[1]

    if ex_before not in valid_format or  ex_after not in valid_format:
        sys.exit("Invalid input")

    if ex_before != ex_after:
        sys.exit("Input and output have different extensions")

    try:
        shirt = Image.open("shirt.png")
        with Image.open(before) as input_img:
            # Crop and resize input to match the exact size of the shirt image
            cropped_img = ImageOps.fit(input_img, shirt.size)

            # Overlay shirt on top of the user's cropped photo
            cropped_img.paste(shirt, shirt)

            # Save final image
            cropped_img.save(after)

    except FileNotFoundError:
        sys.exit("Input does not exist")
