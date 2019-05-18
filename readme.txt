
You are given three channels of the same image: red, green and blue. They are encoded as 16-bit unsigned integers (uint16). Your task is to write a program in Python that converts these files into a good looking RGB image in PNG format, so that it can be displayed in regular programs and browsers. For example, the grass should be bright green and there should be no visible overexposed pixels. It should look like a normal photo captured on a sunny day. PNGs should use 8-bit unsigned integers. 

Your python script should have the following signature:
python create_rgb.py --red red.tif --green green.tif --blue blue.tif --output rgb.png

Hint: dividing all pixels by 256 will not produce a good-looking image.

We recommend to use argparse, numpy and cv2 in your program.

Hint 2: .shape property of numpy arrays can help in debugging.