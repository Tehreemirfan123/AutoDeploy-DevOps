from fastapi import FastAPI, status
from pydantic import BaseModel, Field

app = FastAPI(title="AutoDeploy API", version="0.1.0")


class UserCreate(BaseModel):
    """Data a client must send to create a user."""
    name: str = Field(min_length=1, max_length=100)
    email: str = Field(min_length=3, max_length=255)


class User(UserCreate):
    """A stored user: the input fields plus a server-assigned id."""
    id: int


# Temporary in-memory storage. Replaced by PostgreSQL tomorrow.
users: list[User] = []


@app.get("/health")
def health() -> dict[str, str]:
    """Liveness check used by Docker, deploy scripts and monitoring."""
    return {"status": "ok"}


@app.get("/api/status")
def api_status() -> dict[str, str]:
    return {"service": "autodeploy", "version": app.version}


@app.get("/api/users")
def list_users() -> list[User]:
    return users


@app.post("/api/users", status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate) -> User:
    user = User(id=len(users) + 1, **payload.model_dump())
    users.append(user)
    return user
