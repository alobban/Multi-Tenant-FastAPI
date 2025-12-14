from fastapi import Request, HTTPException

DOC_PATHS = {"/docs", "/redoc", "/openapi.json"}

async def tenant_middleware(request: Request, call_next):
    if request.url.path in DOC_PATHS:
        return await call_next(request)
    
    tenant = request.headers.get("X-Tenant-ID")
    if not tenant:
        raise HTTPException(400, "Missing X-Tenant-ID")
    request.state.tenant_id = tenant
    return await call_next(request)

def get_tenant_id(request: Request):
    return request.state.tenant_id