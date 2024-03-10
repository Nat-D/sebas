class BaseChatPrompt:
    def __init__(self, begin_prompt):
        self.prompt = begin_prompt
    
    def add_user_prompt(self, user_message):
        self.prompt += f"""
        User: {user_message} \n    
        """
    
    def add_assistant_response(self, response):
        self.prompt += f"""
        Assistant: {response} \n
        """