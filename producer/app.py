from fastapi import FastAPI, HTTPException
from kafka import KafkaProducer
import json
import os
import uvicorn
from pydantic import BaseModel

app = FastAPI()
producer = KafkaProducer(
    bootstrap_servers=[os.getenv('KAFKA_BROKER')],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

class Event(BaseModel):
    message: str
    priority: int = 1

@app.post("/produce")
async def produce_event(event: Event):
    try:
        future = producer.send(os.getenv('TOPIC_NAME'), 
                             value={"message": event.message, 
                                   "priority": event.priority})
        future.get(timeout=10)
        return {"status": "success", "message": "Event produced successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT', 8001)))