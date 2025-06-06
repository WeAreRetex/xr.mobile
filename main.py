import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import (
    anagrafica,
    backoffice,
    cesti,
    device,
    device_user,
    documenti,
    inventario,
    raccolte,
    users_modules,
)

app = FastAPI(
    title="IconicMobileWeb",
    version="v1",
    description="FastAPI implementation of IconicMobileWeb API",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(anagrafica.router, prefix="/api/anagrafica", tags=["Anagrafica"])
app.include_router(
    backoffice.router, prefix="/api/backoffice", tags=["BackOfficeModifications"]
)
app.include_router(cesti.router, prefix="/api/cesti", tags=["CestiDevice"])
app.include_router(device.router, prefix="/api/device", tags=["Device"])
app.include_router(device_user.router, prefix="/api/users", tags=["DeviceUser"])
app.include_router(documenti.router, prefix="/api/documenti", tags=["Documenti"])
app.include_router(inventario.router, prefix="/api/inventario", tags=["Inventario"])
app.include_router(raccolte.router, prefix="/api/list", tags=["Raccolte"])
app.include_router(
    users_modules.router, prefix="/api/usersModules", tags=["UsersModules"]
)


@app.get("/")
async def root():
    return {"message": "Welcome to IconicMobileWeb API"}


if __name__ == "__main__":
    # Get host and port from environment variables with defaults
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 8000))

    # Get reload setting from environment (default to True for development)
    reload = os.environ.get("RELOAD", "True").lower() == "true"

    uvicorn.run("main:app", host=host, port=port, reload=reload)
