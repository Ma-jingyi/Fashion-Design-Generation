import os
import base64
import requests
import time


prompt = """This is a selection template, here are some of the costume parts and labels for the costumes, in the format of type: [Type Attribute 1, Type Attribute 2,...]:
  These vocabulary can only be selected within the following range!
  Body Parts: [Full body, Upper body, Lower body, Head]
  Gender: [1boy, 1girl]
  Hairstyle: [Long hair, Short hair, Bun hair, Tir hair, Ponytail hair], and color.
  Posture: [Standing, Sitting, Squatting, Kneeling, Walking]
  Clothing Style: [T-shirt, Shirt, Sweater, Polo shirt, Under shirt, Halter top, Jacket, Skirt, Shorts, Sweatpants, Jeans]
  Fabric Types: [Leather, Plush, Wool, Denim Fabric, Lace, Cotton Fabric, Silk Fabric, Knitted Fabric, Velvet fabric, Printed fabric, Jacquard fabric, Down filling]
  Cloth Color: [Please fill in the sentences according to the ones I gave you]
  Sleeve Length: [Sleeveless, Short sleeve, Elbow sleeve, Long sleeve]
  Sleeve Subdivision: [Flare sleeve, Cape sleeve, Lantern sleeve, Puff sleeve, Ruffle cuff sleeve, Straight sleeve]
  Collar Height: [Short collar, Collarless, High collar]
  Collar Subdivision: [Round collar, V-neck collar, Tailored collar, Turn-down collar, Fur collar, Hooded collar, Lotus leaf collar], such as "Turn-down collar Jacket"
  Skirt Length: [Ultra-short skirt, Knee-length skirt, Long-length skirt, Floor-length skirt]
  Pants Length: [Short pants, Capri pants, Long pants]
  Skirt Subdivision: [Pleated Skirt, A-skirt, Fishtail Skirt, Pencil skirt, Slit skirt, Straight Skirt]
  Front Opening Subdivision: [No front placket, Open front placket, Zipper front placket, Breasted front placket]
  Cloth Silhouette: [Slim silhouette, Oversized silhouette, Mini length, Short silhouette, Ankle length silhouette, Low waistline silhouette, Low waist silhouette, High waist silhouette, H silhouette, Flare line silhouette, Tapered line silhouette, X line silhouette, Hourglass silhouette, Box silhouette, Cocoon silhouette, A-line, Short trapeze, Bell silhouette, Asymmetrical silhouette, Pencil silhouette, Multi-layer silhouette, Symmetrical silhouette, Loose silhouette, Crop top silhouette]
  Occasions and Style Feel: [Traveling, Indoors, Workplace, Date, Party, Outdoors]
  Style: [Y2K style, Baroque style, Bohemian style, Animal print style, Vintage style, Gothic style, Workwear style, Navy style, Korean style, Floral style, Wedding style, Minimalist style, Street fashion style, Military style, Cute style, Loose style, Rococo style, Ethnic style, Party style, Punk style, Fur style, Japanese style, Racing style, Business style, Luxury style, Floral style, Countryside style, Casual style, College style, Rock style, Italian style, British style, Elegant style, Sporty style]
  Craft Elements: [Embroidery, Hot drilling, Sequins, Tie-dye, Patch, Fur, Feathers, Tassel, Bow, Topstitching, Lacing, Printing]
  Pattern Texture: [Please fill in the sentences according to the ones I gave you, For example: Abstract Patterns]
  Shooting Angle: [View from front, View from side, View from back, View from outside]
  Shooting Format: [Close-up shot, Cowboy shot, Wide shot, Aerial View, Dutch Angle]
  Image Range: [Head out of frame, Feet out of frame]
  Number of Characters: [Solo]
  
Next, based on the description of clothing I gave at the end of this paragraph, match and select words in each of the above categories, and eventually give me the major category and selected subcategories, each on a separate line. You need to output all the tag categories. Please output all categories. If you come across something you can't recognise, output "-----". 
The vocabulary must be the same as I wrote, no other words or brackets!!
Output all categories.
Note that you can't create new vocabulary in the categories where I've given you vocabulary, you can only choose from the words I've given you. You cannot have words that are not covered in the sentence.
Don't fill in the elements of the sentence that aren't deciphered on your own, I need you to lower your creativity.
Categories that do not exist in a sentence cannot be created.
Write content in the same category on the same line.
The output format is as follows:
Gender: 1girl
Season: Spring
Cloth color: Yellow skirt, White jacket
...

Next is a one sentence description of the garment: {}"""

def generate_label_for_one_sentence(sentence):
    # Getting the base64 string

    # Keep you ZiZhenzhen API here
    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer API"
    }

    payload = {
    "model": "gpt-4-0125-preview",
    "messages": [
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": prompt.format(sentence),
            }
        ]
        }
    ],
    "max_tokens": 600
    }

    response = requests.post("https://flag.smarttrot.com/v1/chat/completions", headers=headers, json=payload)

    print(response.json())
    response_json = response.json()
    print(response_json["choices"][0]["message"]["content"])


if __name__ == '__main__':

    generate_label_for_one_sentence("put sentence here")
