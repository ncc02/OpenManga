from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
import PIL.Image
import os

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
img = PIL.Image.open('./test.png')

model = genai.GenerativeModel(model_name="gemini-1.5-flash")
response = model.generate_content(["Đây là truyện trung quốc hãy dịch sang tiếng việt:", img])
print(response.text)
