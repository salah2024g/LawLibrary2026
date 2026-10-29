from datetime import datetime, timedelta, timezone

SECRET_KEY = "change-me"
ALGORITHM = "HS256"


def create_token(subject: str) -> dict:

    expires = datetime.now(timezone.utc) + timedelta(minutes=30)

    return {"sub": subject, "expires": expires.isoformat()}


def decode_token(token: dict):

    return token.get("sub")
