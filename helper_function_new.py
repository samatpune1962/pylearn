import google.generativeai as genai
import os

# Configure the API key
# genai.configure(api_key=os.getenv("AIzaSyC8zxhvyNHtN1Qw-qHpUomA2Ct0auKN3sE"))

genai.configure(api_key="AIzaSyC8zxhvyNHtN1Qw-qHpUomA2Ct0auKN3sE")

def ask_a_question(question, model="gemini-2.5-flash"):
    # Create model instance
    model = genai.GenerativeModel(model)


    
    # Generate content
    response = model.generate_content(question)
    return response.text

country_name = 'france'
print(ask_a_question("What is the capital of France?"))
print(ask_a_question(f"what is the capital of {country_name}?"))


country_list = ["india", "japan","north korea"]

for country in country_list :
    print(ask_a_question(f"what is the capital of {country}"))


 



