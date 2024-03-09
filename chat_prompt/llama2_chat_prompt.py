from chat_prompt.base import BaseChatPrompt

class Llama2ChatPrompt(BaseChatPrompt):
    def add_user_prompt(self, message):
        self.prompt += f"""
        <s>[INST]{message}[/INST]   
        """

    def add_assistant_prompt(self, message):
        self.prompt += f"""
        {message}</s>
        """