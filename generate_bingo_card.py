import textwrap
from PIL import Image, ImageDraw, ImageFont
import os
from random import sample, seed
import random

def create_bingo_card():

    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Load the base image for the card (template) at 300 DPI
    base_image = Image.open(os.path.join(current_directory, 'bingo_template.png'))
    draw = ImageDraw.Draw(base_image)
    
    # Adding the Bingo text
    # There are 24 different spots

    #draw.text((680, 680), "Bingo", fill='black', font=ImageFont.truetype('arial.ttf', size= 70))

    # Generate a random seed number
    seed_num = random.randint(0, 2**10)

    seed(seed_num)

    # Square images to be Square (scales down to 450 by 450)
    picture_names = os.listdir(os.path.join(current_directory, "Images"))

    picture_sample = sample(picture_names, 12)
    # three different x positions
    x_pos = list(range(100, 2170, 770))
    # three different y positions
    y_pos = list(range(1117, 3008, 770))

    count = 1

    for x in x_pos:

        for y in y_pos: 
            img = Image.open(os.path.join(current_directory, "Images", picture_sample[count])) 

            if(img.height < img.width):
                img = img.resize((600, int(600*img.height/img.width)))
            else:
                img = img.resize((int(600*img.width/img.height), 600))

            base_image.paste(img, (x, y))
            draw.ellipse([(x + 30, y + 30), (x + 150, y + 150)], fill='white', outline='black')
            
            wrapped_text = textwrap.wrap(picture_sample[count], width=40)  # Adjust the width as needed
            y_text = y + 670  # Starting Y position for the 'Ability' text
            for line in wrapped_text:
                draw.text((x + 40, y_text), line, fill='black', font=ImageFont.truetype('arial.ttf', size= 50))
                y_text += int(50)  # Move Y position for the next line
            
            count = count + 1

    draw.text((2200, 3436), "Seed:" + str(seed_num), fill='black', font=ImageFont.truetype('arial.ttf', size= 50))

    base_image.save(os.path.join(current_directory, "bingo_card" + str(seed_num) + ".png")) 

create_bingo_card()