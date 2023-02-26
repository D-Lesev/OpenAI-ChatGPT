import openai


class Chatbot:
    def __init__(self):

        # Open external API key
        with open("OPENAI_API.txt", "r") as api:
            api_key = api.read()
        openai.api_key = api_key

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text

        return response
