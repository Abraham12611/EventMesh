# Event-Driven Data Processing with Traefik, Kafka, and Docker

This repository demonstrates a practical implementation of event-driven architecture using Traefik as an API gateway, Apache Kafka for message processing, and Docker for containerization. The application consists of three main services: a producer, a consumer, and an API service, all orchestrated using Docker Compose.

## 🏗️ System Interaction Diagram

[![diagram-export-11-15-2024-10-43-51-AM.png](https://i.postimg.cc/9M2rMFnX/diagram-export-11-15-2024-10-43-51-AM.png)](https://postimg.cc/DWC2pFhR)

The application implements:

- Event-driven message processing
- Service orchestration with Docker Compose
- API Gateway pattern with Traefik
- Producer/Consumer pattern with Kafka
- Health monitoring and status reporting

### Components

- **Traefik**: API Gateway and load balancer
- **Kafka**: Message broker for event processing
- **Zookeeper**: Required for Kafka coordination
- **Producer Service**: Generates events and sends them to Kafka
- **Consumer Service**: Processes events from Kafka
- **API Service**: Provides system status and documentation

## 🚀 Getting Started

### Prerequisites

- Docker and Docker Compose installed

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/EventMesh.git
cd EventMesh
```

1. Start the application:

```bash
docker-compose up --build
```

The application will be available at:

- Traefik Dashboard: `http://localhost:8080`
- Producer API: `http://localhost/produce`
- Consumer API: `http://localhost/consume`
- Status API: `http://localhost/api/status`

## 📝 Usage Examples

### Producing Events

Send a message using cURL:

```bash
curl -X POST http://localhost/produce \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Hello World",
    "priority": 1
  }'
```

### Consuming Events

Retrieve processed messages:

```bash
curl http://localhost/consume
```

### Checking System Status

Monitor system health:

```bash
curl http://localhost/api/status
```

## 🛠️ Project Structure

```plaintext
event-driven-processing/
├── docker-compose.yml
├── .env
├── producer/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py
├── consumer/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py
├── api/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py
└── traefik/
    └── traefik.yml
```

## 🔧 Configuration

### Environment Variables

Configure the application using the `.env` file:

```plaintext
KAFKA_BROKER=kafka:9092
TOPIC_NAME=data_events
API_PORT=8000
PRODUCER_PORT=8001
CONSUMER_PORT=8002
```

### Service Configuration

Each service can be configured through their respective Dockerfile and requirements.txt files. The main configuration for service routing is handled in the docker-compose.yml file through Traefik labels.

## 🔍 Monitoring and Debugging

### Logs

View logs for all services:

```bash
docker-compose logs
```

View logs for a specific service:

```bash
docker-compose logs [service_name]
```

### Traefik Dashboard

Access the Traefik dashboard at `http://localhost:8080` to monitor:

- Service health
- Routing rules
- Request metrics

## 🧪 Testing

To test the complete flow:

1. Start the system:

```bash
docker-compose up -d
```

1. Send test messages:

```bash
# Send multiple test messages
for i in {1..5}; do
  curl -X POST http://localhost/produce \
    -H "Content-Type: application/json" \
    -d "{\"message\": \"Test message $i\", \"priority\": $i}"
done
```

1. Verify message processing:

```bash
curl http://localhost/consume
```

## 🔒 Security Considerations

This is a development setup and includes:

- Exposed Traefik dashboard (disabled in production)
- No authentication
- No SSL/TLS configuration

For production deployment, consider:

- Enabling authentication
- Configuring SSL/TLS
- Securing the Kafka cluster
- Implementing proper logging
- Setting up monitoring

## 📈 Scaling

The application can be scaled in several ways:

1. Horizontal scaling of services:

```bash
docker-compose up -d --scale producer=3 --scale consumer=3
```

1. Kafka partition adjustment for parallel processing
2. Load balancing through Traefik

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📚 Resources

- [Traefik Documentation](https://doc.traefik.io/traefik/)
- [Kafka Documentation](https://kafka.apache.org/documentation/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Documentation](https://docs.docker.com/)
