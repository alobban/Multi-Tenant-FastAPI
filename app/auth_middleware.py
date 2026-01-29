from fastapi import Request, HTTPException
from auth import verify_jwt

PROTECTED_ROUTES = {"/login", "/token"}  # modify as needed

async def auth_middleware(request: Request, call_next):
    path = request.url.path

    if path in PROTECTED_ROUTES:
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            raise HTTPException(401, "Missing Authorization: Bearer token")

        token = auth_header.split()[1]
        payload = verify_jwt(token)

        request.state.user = payload  # make user available to endpoints

    return await call_next(request)