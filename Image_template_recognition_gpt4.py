import os
import base64
import requests
import time

# Function to encode the image
# hhhh
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')


def generate_random_file_name_handler():
    time_to_str = time.strftime("%Y%m%d%H%M%S") + "_gpt4v_gen"
    f = open(time_to_str, 'w')
    return f

def generate_label_with_gpt4v(image_folder, file_handler, count):
    gen_count = 0
    for root, dirs, files in os.walk(image_folder):
        for file in files:
            # if gen_count < 500:
            #     gen_count += 1
            #     continue
            if gen_count == count:
                break
            print(os.path.join(root, file))
            image_path = os.path.join(root, file)
            try:
                generate_label_for_one_image(image_path, file_handler)
                gen_count += 1
            except Exception as ex:
                print("exception happens, ex is {}".format(ex))

prompt = """Task requirement: Identify image content based on the vocabulary I have provided. I will provide you with recognition standards, precautions, and some name explanations. 
Finally, write a DeepBooru prompt word that can be used for "Stable-Diffusion-WebUI",Your final vocabulary can describe all the details of this picture in great detail. Please output strictly according to my requirements！

The following categories and category properties is the clothing image content that you need to recognize and output, in the format of type: [Type Attribute 1, Type Attribute 2,...]:
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


Here is your recognition standards:
   Now, you are required to identify the most similar category attributes for all labels type above in the picture in order according to their respective category attributes, all of these categories must be output in full.
0. When you put out the "Fabric Types""Color""Collar Height""Collar Subdivision""Sleeve Length""Sleeve Subdivision", you have to put out where it is, such us "Blue Jeans, White Shirt...".
1. You have to write down the labels of all the clothing style that you can see. And write the corresponding style, such as "High collar Jacket, Short collar Shirt...", "Turn-down collar Shirt", "Checkered Coat...", similar to your method of labeling colors.
2. If the category attribute is not identified, please output "-----". All categories must be output.
3. If you know the "Skirt Length", you must write the choice of "Skirt Subdivision" . 
4. If you know the "Collar Height", you must write the choice of "Collar Subdivision" .
5. Only one corresponding content can be output for each "Type" 、"Occasions" 、"Silhouette" and "Body parts".
6. As long as there is no neck showing in the picture, the Collar Height must be high. If the skin on the neck is exposed, it may not be a high collar.
7. Silhouette please pay attention to the overall feeling of the character outline.
8. Please write down the collar heights and subdivisions of different clothes in the picture, and distinguish them for identification.
9. Do not use sentences or "()" when outputting.

The output sample format is:
Image Dimension_Body parts: Whole body
Fashion Style_Gender: 1girl
Fashion Style_Hairstyle: Short hair, Brown hair
Upper Attribute_Type: T-shirt, Hoodie
Lower Attribute_Type: Skirt
Color: White T-shirt, Silver Hoodie, White Skirt
Upper Attribute_Collar Height: High collar T-shirt, Short collar Hoodie
Silhouette: Slim silhouette

Each category occupies one line. Please strictly output the category in English according to the above format and do not output any extra content.
Categories cannot be confused or cross selected."""
def generate_label_for_one_image(image_path, file_handler):
    # Getting the base64 string
    base64_image = encode_image(image_path)

    # Keep you ZiZhenzhen API here
    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer API"
    }

    payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": prompt,
            },
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
            }
        ]
        }
    ],
    "max_tokens": 600
    }

    response = requests.post("https://flag.smarttrot.com/v1/chat/completions", headers=headers, json=payload)

    print(response.json())
    response_json = response.json()
    final_result = {}
    final_result["image_path"] = image_path
    final_result["content"] = response_json["choices"][0]["message"]["content"]
    file_handler.write(str(final_result) + "\n")


if __name__ == '__main__':
    # load_whisper_model("medium")
    # load_chatglm_model()
    image_folder = "put image folder here"
    count = 1000
    file_handler = generate_random_file_name_handler()
    generate_label_with_gpt4v(image_folder, file_handler, count)
    file_handler.flush()
