import openai
from distutils import config

openai.api_key = config('OPENAI_API_KEY'),

response = openai.Image.create(
  prompt="a white siamese cat",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)