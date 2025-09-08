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

#for country in country_list :
#    print(ask_a_question(f"what is the capital of {country}"))
country_list.append("thailand")
print(country_list)
country_list.remove("japan")
print(country_list)
for c_name in country_list:
    print(c_name)
ice_cream_flavours = ["Vanilla", "Chocolate", "Strawberry", "Mint"]
flavour_desc = []
i = 0
for flavour in ice_cream_flavours:
    # print(ask_a_question(f"""For the icecream flavour listed below
     #              provide a captivating desecription that would be used for promotion
     #              Flavor : {flavour}"""))
    print(flavour)
    question = f"""For the flavour {flavour},
    provide a 10 words description"""
    print(question)
    # print(ask_a_question(question))
    flavour_desc.append(ask_a_question(question))
    print(flavour_desc[i])
    i=i+1
    
print("done your task")



 



