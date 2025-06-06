from fastapi import APIRouter, Path, Body, HTTPException, Query
from typing import List, Optional
from app.models.raccolte import RaccolteDevice, ListRow, RichiestaParametriList

router = APIRouter()


@router.post("/insert/{mac}", response_model=int)
async def post_insert(
    mac: str = Path(..., description="MAC address del dispositivo"),
    lista: RaccolteDevice = Body(..., description="Dati della lista")
):
    """Crea una nuova lista di raccolta."""
    return 1


@router.put("/row/{idList}/{mac}")
async def put_row(
    idList: int = Path(..., description="ID della lista"),
    mac: str = Path(..., description="MAC address del dispositivo"),
    riga: ListRow = Body(..., description="Dati della riga")
):
    """Aggiorna una riga di una lista."""
    return {}


@router.post("/row/{idList}/{mac}", response_model=int)
async def post_row(
    idList: int = Path(..., description="ID della lista"),
    mac: str = Path(..., description="MAC address del dispositivo"),
    riga: ListRow = Body(..., description="Dati della riga")
):
    """Aggiunge una riga a una lista."""
    return 1


@router.delete("/row/{idRow}/{idList}/{mac}")
async def delete_row(
    idRow: int = Path(..., description="ID della riga"),
    idList: int = Path(..., description="ID della lista"),
    mac: str = Path(..., description="MAC address del dispositivo")
):
    """Elimina una riga da una lista."""
    return {}


@router.delete("/{idList}/{mac}")
async def delete_list(
    idList: int = Path(..., description="ID della lista"),
    mac: str = Path(..., description="MAC address del dispositivo")
):
    """Elimina una lista."""
    return {}


@router.post("/save/{idList}/{idUser}/{dateAndTime}/{Mac}", response_model=ListRow)
async def post_save(
    idList: int = Path(..., description="ID della lista"),
    idUser: int = Path(..., description="ID dell'utente"),
    dateAndTime: str = Path(..., description="Data e ora"),
    Mac: str = Path(..., description="MAC address del dispositivo"),
    righe: List[ListRow] = Body(..., description="Righe della lista")
):
    """Salva una lista con le sue righe."""
    return ListRow(read_code="", amount=0, is_deleted=False)


@router.post("/imported", response_model=bool)
async def post_imported(
    id: int = Body(..., description="ID della lista")
):
    """Segna una lista come importata."""
    return True


@router.get("/tobeimported/{idStore}/{idDomain}/{idUser}", response_model=List[RaccolteDevice])
async def get_to_be_imported(
    idStore: int = Path(..., description="ID del negozio"),
    idDomain: str = Path(..., description="ID del dominio"),
    idUser: int = Path(..., description="ID dell'utente")
):
    """Restituisce le liste da importare."""
    return []


@router.get("/opened/{idStore}", response_model=List[RaccolteDevice])
async def get_opened(
    idStore: int = Path(..., description="ID del negozio"),
    param_days: Optional[int] = Query(None, alias="param.days", description="Numero di giorni"),
    param_user_id: Optional[int] = Query(None, alias="param.user_id", description="ID dell'utente")
):
    """Restituisce le liste aperte per un negozio."""
    return []


@router.get("/closed/{idStore}", response_model=List[RaccolteDevice])
async def get_closed(
    idStore: int = Path(..., description="ID del negozio"),
    param_days: Optional[int] = Query(None, alias="param.days", description="Numero di giorni"),
    param_user_id: Optional[int] = Query(None, alias="param.user_id", description="ID dell'utente")
):
    """Restituisce le liste chiuse per un negozio."""
    return []


@router.get("/rows/{id}", response_model=List[ListRow])
async def get_rows(
    id: int = Path(..., description="ID della lista")
):
    """Restituisce le righe di una lista."""
    return []
