# SEBAS is our virtual assistant

## Setup

0. Install docker and setup Nvidia container toolkit

https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html


1. run ollama server (with GPU)
```
    docker compose -f docker-compose-gpu.yml up -d
```
or without gpu
```
    docker compose -f docker-compose.yml up -d
```

2. Download llama2 model. (The model is around 4 gb.)
```
    curl http://localhost:11434/api/pull -d '{
        "name": "llama2"
    }'
```

3. Try talk to the model
```
    curl http://localhost:11434/api/chat -d '{
        "model": "llama2",
        "messages": [
            {
            "role": "user",
            "content": "why is the sky blue?"
            }
        ]
    }'
```

# Things to try out.

[ ] System prompt
[ ] Memory and Chatbot capability
[ ] Using RAG
[ ] Output JSON format and validation
[ ] Output parsing
[ ] Calling external functions
[ ] Try Thai Language  



