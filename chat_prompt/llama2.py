from chat_prompt.base import BaseChatPrompt

class Llama2ChatPrompt(BaseChatPrompt):
    def add_user_prompt(self, user_message):
        self.prompt += f"""
        <s>[INST]{user_message}[/INST]  
        """

    def add_assistant_response(self, response):
        self.prompt += f"""
        {response}</s>
        """