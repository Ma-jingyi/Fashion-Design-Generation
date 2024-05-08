# An Intelligent Generative Method of Fashion Design Combining Attribute Knowledge and Stable Diffusion
We aims for a novel design method through constructing fashion attribute knowledge group, prompt templates and a specific attribute [LoRA](https://github.com/microsoft/LoRA), for incorporate attribute knowledge into the generation of fashion design in [Stable Diffusion](https://github.com/Stability-AI/StableDiffusion). 
# Below is our method
To address the difficult of obtaining a comprehensive description of fashion image and generating results closely with expected attribute, herein the feasible method is proposed to combin attributes knowledge of fashion design and Stable Diffusion. The method primarily consists of four stages, designed based on fashion attribute knowledge graph and LoRA training method.  

![Figure 0](https://github.com/Ma-jingyi/Fashion-Design-Generation/assets/126131823/8052b8a5-4d19-48dd-9dd1-0993aed3a90d)
## 1. Fashion attribute knowledge graph
Fashion labels are collected from fashion website.
A fashion attribute knowledge graph is constructed based on generic and specialized fashion attributes. 

![Figure 2](https://github.com/Ma-jingyi/Fashion-Design-Generation/assets/126131823/d745f037-7e0d-4d1a-bc15-7c2842c96d82)

## 2. Prompt templates translate
Prompt templates are constructed based on the input dimensions of the Stable Diffusion and fashion attribute knowledge graph.
Natural language of fashion design requirements inputs provided by designers will turn to generate labels through the GPT-4 model. [Training_label_conversion_gpt4](https://github.com/Ma-jingyi/Fashion-Design-Generation/blob/main/Training_label_conversion_gpt4.py)

![提示词模板转换方法-补充图片](https://github.com/Ma-jingyi/Fashion-Design-Generation/assets/126131823/7537c9fe-86f1-48d9-91b1-bde4e74f3f3c)

## 3. Specific attribute LoRA training
A multimodal visual recognition method is then employed to label the fashion images datasets with templated descriptive labels. [Image_template_recognition_gpt4](https://github.com/Ma-jingyi/Fashion-Design-Generation/blob/main/Image_template_recognition_gpt4.py)
Then, merging or replacing label with specific attribute properties to train LoRA model. 

![Figure 6](https://github.com/Ma-jingyi/Fashion-Design-Generation/assets/126131823/fa3ddad9-b3f4-4b20-a328-779e966163d9)

## 4. Specific attribute LoRA training
Finally, the prompt template-generated results are directly input into stable diffusion to generate images. The relevant LoRA is utilized for precise control of the image content, resulting in fashion designs with specific attribute.
