from fastapi import Request, HTTPException

DOC_PATHS = {"/docs", "/redoc", "/openapi.json", "/login", "/token"}
TENANT_BYPASSED_PATH = '/tenants' 

async def tenant_middleware(request: Request, call_next):
    path = request.url.path
    method = request.method

    if path == "/favicon.ico":
        return await call_next(request)

    if path in DOC_PATHS:
        return await call_next(request)
    
    # Bypass for:
    # POST /tenants  (create tenant)
    # GET /tenants   (list tenants)
    if path == TENANT_BYPASSED_PATH and method in ["POST", "GET"]:
        return await call_next(request)
    
    tenant = request.headers.get("X-Tenant-ID")
    if not tenant:
        raise HTTPException(400, "Missing X-Tenant-ID")
    request.state.tenant_id = tenant
    return await call_next(request)

def get_tenant_id(request: Request):
    return request.state.tenant_id