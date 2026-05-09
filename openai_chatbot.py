from openai import OpenAI

client = OpenAI(api_key="BURAYA_API_KEY")

def chat_with_gpt(prompt):

    response = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "system", "content": "Sen yardımcı bir chatbotsun."},
            {"role": "user", "content": f"{prompt}"}
        ]
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":

    

    while True:
        user_input = input("Kullanıcı tarafından girilen mesaj: ")

        if user_input.lower() in ["exit", "q"]:
            print("Konuşma tamamlandı")
            break

        response = chat_with_gpt(user_input)
        print(f"Chatbot: {response}")
    
# https://platform.openai.com/api-keys 

