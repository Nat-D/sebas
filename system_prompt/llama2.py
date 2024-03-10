from system_prompt.base import BaseSystemPrompt

class Llama2SystemPrompt(BaseSystemPrompt):
    def __init__(self, prompt, user_message):
        self.prompt = f"""
        <s>[INST] <<SYS>>
        {prompt}
        <</SYS>>

        {user_message}[/INST]</s>
        """