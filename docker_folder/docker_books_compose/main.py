import uvicorn
from settings import settings


if __name__ == "__main__":

    print("Swagger UI:")
    print("http://localhost:8081/docs")
    print("http://localhost:8082/docs")
    print("http://localhost:8083/docs")

    uvicorn.run(
    "application:app",
        host=settings.host,
        port=settings.port,
    )
