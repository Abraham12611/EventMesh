from fastapi import FastAPI
import httpx
import os
import uvicorn

app = FastAPI(title="Event-Driven Processing API",
             description="API for managing and monitoring event processing")

@app.get("/api/status")
async def get_status():
    async with httpx.AsyncClient() as client:
        try:
            producer_status = await client.get("http://producer:8001/produce")
            consumer_status = await client.get("http://consumer:8002/consume")
            return {
                "status": "healthy",
                "services": {
                    "producer": "up" if producer_status.status_code == 200 else "down",
                    "consumer": "up" if consumer_status.status_code == 200 else "down"
                }
            }
        except Exception as e:
            return {"status": "unhealthy", "error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT', 8000)))