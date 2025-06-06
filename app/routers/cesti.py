from fastapi import APIRouter, Path, Body, HTTPException
from typing import List, Optional
from app.models.cesti import Cesto

router = APIRouter()


@router.get("/{idPV}", response_model=List[Cesto])
async def get_values(
    idPV: int = Path(..., description="ID del punto vendita")
):
    """Restituisce i cesti per un punto vendita."""
    return []


@router.post("/", response_model=int)
async def post_value(
    value: Cesto = Body(..., description="Dati del cesto")
):
    """Crea un nuovo cesto."""
    # In una applicazione reale, questo salverebbe nel database e restituirebbe l'ID generato
    return 1


@router.delete("/{id}")
async def delete_value(
    id: int = Path(..., description="ID del cesto da eliminare")
):
    """Elimina un cesto specifico."""
    return {}
