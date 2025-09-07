from google import genai
import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyCtTflQmiUYEOAPj86B2qNVcQzehghoAes"
def ask_a_question(question, model="gemini-2.5-flash"):
    client = genai.Client()
    response = client.models.generate_content(
        model=model,
        contents=question
    )
    return response.text


##  print(ask_a_question("Explain how photosynthesis works in a few sentences."))

# my_person = "Albert Einstein"
##  print(f"""
##  {ask_a_question(f"When was {my_person} born?")}
##  """)

## print(f"when was {my_person} born?")
# my_question = f"when was {my_person} born?"

## print(my_question)
#print(ask_a_question(my_question, "gemini-2.5-flash"))


# print(f"{ask_a_question(f"When was {my_person} born?")}")

## trying something from the lecture
##
## name = "Tommy"
##potatoes = 4.75
##my_question = f"Write a couplet about my friend {name} who has about {round(potatoes)} potatoes."
## print(my_question)
## print(ask_a_question(my_question, "gemini-2.5-flash"))

## trying something from the lecture exercise
# lucky_number = 12
# print(f"My lucky number is {lucky_number*10}")

## name = "Tommy"
## potatoes = 4.75
## my_question = f"Write a couplet about my friend {name} who has about {round(potatoes)} potatoes."
## print(my_question)
family_list = ["Alice", "Bob", "Charlie"]
print(family_list)
print(len(family_list))
gender = "female"
last_name =""

for name in family_list:
    print(name)
    last_name = name
    print(last_name)
    my_question = f"write a 4 line poem inspired by my name {name } and my gender {gender} with a romantic theme."
    print(ask_a_question(my_question, "gemini-2.5-flash"))


