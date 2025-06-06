from fastapi import APIRouter, Path, Body, HTTPException
from typing import List
from app.models.device_user import MiniUtenteDevice

router = APIRouter()


@router.get("/{mac}", response_model=List[MiniUtenteDevice])
async def get_utenti(
    mac: str = Path(..., description="MAC address del dispositivo")
):
    """Restituisce la lista degli utenti per un dispositivo."""
    return []


@router.post("/{mac}")
async def post_utente_login(
    mac: str = Path(..., description="MAC address del dispositivo"),
    idUtente: int = Body(..., description="ID dell'utente")
):
    """Effettua il login di un utente su un dispositivo."""
    return {}


@router.post("/out/{mac}")
async def post_utente_logout(
    mac: str = Path(..., description="MAC address del dispositivo")
):
    """Effettua il logout di un utente da un dispositivo."""
    return {}


@router.post("/icone/{idUtente}")
async def post_utente_icone(
    idUtente: int = Path(..., description="ID dell'utente"),
    ordine: str = Body(..., description="Ordine delle icone")
):
    """Aggiorna l'ordine delle icone per un utente."""
    return {}
