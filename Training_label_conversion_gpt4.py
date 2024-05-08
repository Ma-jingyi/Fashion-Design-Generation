import os
import base64
import requests
import time


prompt = """This is a selection template, here are some of the costume parts and labels for the costumes, in the format of type: [Type Attribute 1, Type Attribute 2,...]:
  These vocabulary can only be selected within the following range!
Fashion Style: {
  Gender: [1boy, 1girl]
  Hairstyle: [Long hair, Short hair, Bun hair, Tir hair, Ponytail hair], and color.
  Posture: [Standing, Sitting, Squatting, Kneeling, Walking]
  Style: [Vintage style,Minimalist style,Cute style,Luxury style,College style,Elegant style,Sporty style, Floral style, Cute style, Rock style]
  Silhouette: [Slim silhouette,Short silhouette,Low waistline silhouette,High waist silhouette, Loose silhouette]

  }
Fashion Craft: {
  Fabric: [Leather, Plush, Wool, Denim Fabric, Lace, Cotton Fabric, Silk Fabric, Knitted Fabric, Velvet fabric, Printed fabric, Jacquard fabric, Down filling]
  Color: [Reference the Pantone color chart of current cloth for color judgment]
  Occasions: [Traveling, Indoors, Workplace, Date, Party, Outdoors]
  Decorate: [Embroidery, Hot drilling, Sequins, Tie-dye, Patch, Fur, Feathers, Tassel, Bow, Topstitching, Lacing, Printing]
  Pattern: [Please freely express and output the elements of this type contained in the clothing in this picture，such us "abstract patterns jeans". Don't need write "solid"!]

}
Whole Attributes: {
  Type: [Cocktail Dress, Evening Dress, Cheongsam, Chinese Wedding Dress]
  Sleeve Length: [Sleeveless, Short sleeve, Elbow sleeve, Long sleeve]
  Sleeve Subdivision: [Flare sleeve, Cape sleeve, Lantern sleeve, Puff sleeve, Ruffle cuff sleeve, Straight sleeve]
  Collar Height: [Short collar, Collarless, High collar]
  Collar Subdivision: [Round collar, V-neck collar, Tailored collar, Turn-down collar, Fur collar, Hooded collar, Lotus leaf collar]
  Front Opening Subdivision: [No front placket, Open front placket, Zipper front placket, Breasted front placket]

}
Lower Attributes: {
  Type: [Skirt, Shorts, Sweatpants, Jeans]
  Skirt Length: [Ultra-short skirt, Knee-length skirt, Long-length skirt, Floor-length skirt]
  Pants Length: [Short pants, Capri pants, Long pants]
  Skirt Subdivision: [Pleated Skirt, A-skirt, Fishtail Skirt, Pencil skirt, Slit skirt, Straight Skirt]

}
Upper Attributes: {
  Type: [T-shirt, Hoodie, Shirt, Sweater, Cardigan, Polo shirt, Vest, Under shirt, Halter top, Bustier]
  Sleeve Length: [Sleeveless, Short sleeve, Elbow sleeve, Long sleeve]
  Sleeve Subdivision: [Flare sleeve, Cape sleeve, Lantern sleeve, Puff sleeve, Ruffle cuff sleeve, Straight sleeve]
  Collar Height: [Short collar, Collarless, High collar]
  Collar Subdivision: [Round collar, V-neck collar, Tailored collar, Turn-down collar, Fur collar, Hooded collar, Lotus leaf collar]
  Front Opening Subdivision: [No front placket, Open front placket, Zipper front placket, Breasted front placket]

}
Image Dimension: {
  Body Parts: [Full body, Upper body, Lower body, Head]
  Character Details: [Write all the details about character, such as selfie, expressions, emotion]
  Number of Characters: [Solo]
  Character Sighting:[Looking at viewer, Looking to the side, Looking away, Looking back, Looking up, Looking down]
  Image Range: [Head out of frame, Feet out of frame]
  Shooting Angle: [View from front, View from side, View from back, View from outside]
  Shooting Format: [Close-up shot, Cowboy shot, Wide shot, Aerial View, Dutch Angle] 
}
  
Next, based on the description of clothing I gave at the end of this paragraph, match and select words in each of the above categories, and eventually give me the major category and selected subcategories, each on a separate line. You need to output all the tag categories. Please output all categories. If you come across something you can't recognise, output "-----". 
The vocabulary must be the same as I wrote, no other words or brackets!!
Output all categories.
Note that you can't create new vocabulary in the categories where I've given you vocabulary, you can only choose from the words I've given you. You cannot have words that are not covered in the sentence.
Don't fill in the elements of the sentence that aren't deciphered on your own, I need you to lower your creativity.
Categories that do not exist in a sentence cannot be created.
Write content in the same category on the same line.
The output format is as follows:
Image Dimension_Body parts: Whole body
Fashion Style_Gender: 1girl
Fashion Style_Hairstyle: Short hair, Brown hair
Upper Attribute_Type: T-shirt, Hoodie
Lower Attribute_Type: Skirt
Color: White T-shirt, Silver Hoodie, White Skirt
Upper Attribute_Collar Height: High collar T-shirt, Short collar Hoodie
Silhouette: Slim silhouette

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
