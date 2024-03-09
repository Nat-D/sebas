# SEBAS is our virtual assistant

## Setup

1. run ollama server 
```
    docker-compose -f docker-compose-gpu.yml up -d
```

2. Download llama2 model. (The model is around 4 gb.)
```
    curl http://localhost:11434/api/pull -d '{
        "name": "llama2"
    }'
```

3. Try out your 

