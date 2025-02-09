import google.generativeai as genai

genai.configure(api_key="")

generation_config = {
  "temperature": 1.8,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 4000,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    
  ]
)

while True:
    response = chat_session.send_message(input("Enter your message: "))
    if response.lower()=="quit":
        break   
    else:    
        print(response.text)

print("Goodbye!")