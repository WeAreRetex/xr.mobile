from fastapi import APIRouter, Path, Body, HTTPException, Query
from typing import List, Optional
from app.models.inventario import Inventario, Elemento, RichiestaParametriInv

router = APIRouter()


@router.get("/ping", response_model=bool)
async def get_ping():
    """Verifica se il servizio inventario è attivo."""
    return True


@router.get("/{pv}/{utente}", response_model=List[Inventario])
async def get_aperti(
    pv: int = Path(..., description="ID del punto vendita"),
    utente: int = Path(..., description="ID dell'utente")
):
    """Restituisce gli inventari aperti per un punto vendita e utente."""
    return []


@router.get("/{pv}", response_model=List[Inventario])
async def get_chiusi(
    pv: int = Path(..., description="ID del punto vendita")
):
    """Restituisce gli inventari chiusi per un punto vendita."""
    return []


@router.post("/chiudi")
async def post_chiudi(
    id: int = Body(..., description="ID dell'inventario")
):
    """Chiude un inventario."""
    return {}


@router.post("/importato", response_model=bool)
async def post_importato(
    id: int = Body(..., description="ID dell'inventario")
):
    """Segna un inventario come importato."""
    return True


@router.get("/righe/{id}", response_model=List[Elemento])
async def get_righe(
    id: int = Path(..., description="ID dell'inventario")
):
    """Restituisce le righe di un inventario."""
    return []


@router.post("/riga/{id}", response_model=int)
async def post_riga(
    id: int = Path(..., description="ID dell'inventario"),
    riga: Elemento = Body(..., description="Dati della riga")
):
    """Aggiunge una riga a un inventario."""
    return 1


@router.post("/row/{id}", response_model=int)
async def post_row(
    id: int = Path(..., description="ID dell'inventario"),
    riga: Elemento = Body(..., description="Dati della riga")
):
    """Aggiunge una riga a un inventario (alternativo)."""
    return 1


@router.post("/insert", response_model=int)
async def post_lista(
    lista: Inventario = Body(..., description="Dati dell'inventario")
):
    """Crea un nuovo inventario."""
    return 1


@router.delete("/")
async def delete_lista(
    id: int = Body(..., description="ID dell'inventario")
):
    """Elimina un inventario."""
    return {}


@router.delete("/riga")
async def delete_riga(
    id: int = Body(..., description="ID della riga")
):
    """Elimina una riga di un inventario."""
    return {}


@router.delete("/row")
async def delete_row(
    id: int = Body(..., description="ID della riga")
):
    """Elimina una riga di un inventario (alternativo)."""
    return {}


@router.post("/chiudiInv/{idInv}/{idUtente}/{dataora}", response_model=List[Elemento])
async def post_chiudi_inv(
    idInv: int = Path(..., description="ID dell'inventario"),
    idUtente: int = Path(..., description="ID dell'utente"),
    dataora: str = Path(..., description="Data e ora"),
    righe: List[Elemento] = Body(..., description="Righe dell'inventario")
):
    """Chiude un inventario con le sue righe."""
    return []


@router.get("/opened/{idStore}", response_model=List[Inventario])
async def get_open_inv(
    idStore: int = Path(..., description="ID del punto vendita"),
    param_days: Optional[int] = Query(None, alias="param.days", description="Numero di giorni"),
    param_user_id: Optional[int] = Query(None, alias="param.user_id", description="ID dell'utente")
):
    """Restituisce gli inventari aperti per un punto vendita."""
    return []


@router.get("/closed/{idStore}", response_model=List[Inventario])
async def get_closed_inv(
    idStore: int = Path(..., description="ID del punto vendita"),
    param_days: Optional[int] = Query(None, alias="param.days", description="Numero di giorni"),
    param_user_id: Optional[int] = Query(None, alias="param.user_id", description="ID dell'utente")
):
    """Restituisce gli inventari chiusi per un punto vendita."""
    return []


@router.put("/riga/{idInventario}", response_model=int)
async def put_riga(
    idInventario: int = Path(..., description="ID dell'inventario"),
    riga: Elemento = Body(..., description="Dati della riga")
):
    """Aggiorna una riga di un inventario."""
    return 1
