from fastapi import FastAPI
from kafka import KafkaConsumer
import json
import os
import uvicorn
from threading import Thread
import asyncio
from collections import deque

app = FastAPI()
messages = deque(maxlen=100)  # Store last 100 messages

def kafka_consumer():
    consumer = KafkaConsumer(
        os.getenv('TOPIC_NAME'),
        bootstrap_servers=[os.getenv('KAFKA_BROKER')],
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='latest',
        enable_auto_commit=True
    )
    
    for message in consumer:
        messages.appendleft({
            'timestamp': message.timestamp,
            'value': message.value,
            'partition': message.partition
        })

@app.on_event("startup")
async def startup_event():
    Thread(target=kafka_consumer, daemon=True).start()

@app.get("/consume")
async def get_messages():
    return list(messages)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT', 8002)))