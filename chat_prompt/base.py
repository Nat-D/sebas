class BaseChatPrompt:
    def __init__(self, begin_prompt):
        self.prompt = begin_prompt
    
    def add_user_prompt(self, message):
        self.prompt += f"""
        User: {message} \n    
        """
    
    def add_assistant_prompt(self, message):
        self.prompt += f"""
        Assistant: {message} \n
        """