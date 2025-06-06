from fastapi import APIRouter, Path, Body, HTTPException, Query
from typing import List, Optional
from app.models.documenti import (
    Documenti_Documento, DocumentoDevice, RigaDocDevice, 
    RigaDocDeviceId, RichiestaParametri
)

router = APIRouter()


@router.get("/{pv}/{utente}", response_model=List[Documenti_Documento])
async def get_documenti(
    pv: int = Path(..., description="ID del punto vendita"),
    utente: int = Path(..., description="ID dell'utente")
):
    """Restituisce la lista dei documenti per un punto vendita e utente."""
    return []


@router.delete("/{id}/{mac}/{dataora}")
async def delete_documento(
    id: int = Path(..., description="ID del documento"),
    mac: str = Path(..., description="MAC address del dispositivo"),
    dataora: str = Path(..., description="Data e ora")
):
    """Elimina un documento specifico."""
    return {}


@router.post("/nuovo/{utente}/{mac}/{dataora}", response_model=int)
async def post_nuovo(
    utente: int = Path(..., description="ID dell'utente"),
    mac: str = Path(..., description="MAC address del dispositivo"),
    dataora: str = Path(..., description="Data e ora"),
    documento: DocumentoDevice = Body(..., description="Dati del documento")
):
    """Crea un nuovo documento."""
    return 1


@router.get("/modifica/{id}/{mac}/{dataora}")
async def get_modifica(
    id: int = Path(..., description="ID del documento"),
    mac: str = Path(..., description="MAC address del dispositivo"),
    dataora: str = Path(..., description="Data e ora")
):
    """Avvia la modifica di un documento."""
    return {}


@router.get("/chiudi/{id}/{mac}/{dataora}")
async def get_chiudi(
    id: int = Path(..., description="ID del documento"),
    mac: str = Path(..., description="MAC address del dispositivo"),
    dataora: str = Path(..., description="Data e ora")
):
    """Chiude un documento."""
    return {}


@router.get("/prelevato/{id}")
async def get_prelevato(
    id: int = Path(..., description="ID del documento")
):
    """Segna un documento come prelevato."""
    return {}


@router.put("/riga/{id}/{mac}/{dataora}", response_model=int)
async def put_riga(
    id: int = Path(..., description="ID del documento"),
    mac: str = Path(..., description="MAC address del dispositivo"),
    dataora: str = Path(..., description="Data e ora"),
    riga: RigaDocDeviceId = Body(..., description="Dati della riga")
):
    """Aggiorna una riga di un documento."""
    return 1


@router.post("/riga/{id}/{mac}/{dataora}", response_model=int)
async def post_riga(
    id: int = Path(..., description="ID del documento"),
    mac: str = Path(..., description="MAC address del dispositivo"),
    dataora: str = Path(..., description="Data e ora"),
    riga: RigaDocDevice = Body(..., description="Dati della riga")
):
    """Aggiunge una riga a un documento."""
    return 1


@router.delete("/riga/{id}/{mac}/{dataora}")
async def delete_riga(
    id: int = Path(..., description="ID del documento"),
    mac: str = Path(..., description="MAC address del dispositivo"),
    dataora: str = Path(..., description="Data e ora")
):
    """Elimina una riga da un documento."""
    return {}


@router.post("/chiudidoc/{id}/{mac}/{sDataIng}/{dataora}", response_model=List[RigaDocDeviceId])
async def post_chiudi_doc(
    id: int = Path(..., description="ID del documento"),
    mac: str = Path(..., description="MAC address del dispositivo"),
    sDataIng: str = Path(..., description="Data di ingresso"),
    dataora: str = Path(..., description="Data e ora"),
    righe: List[RigaDocDevice] = Body(..., description="Righe del documento")
):
    """Chiude un documento con le sue righe."""
    return []


@router.get("/opened/{idStore}", response_model=List[Documenti_Documento])
async def get_open_docs(
    idStore: int = Path(..., description="ID del punto vendita"),
    param_days: Optional[int] = Query(None, alias="param.days", description="Numero di giorni"),
    param_user_id: Optional[int] = Query(None, alias="param.user_id", description="ID dell'utente")
):
    """Restituisce i documenti aperti per un punto vendita."""
    return []


@router.get("/closed/{idStore}", response_model=List[Documenti_Documento])
async def get_closed_docs(
    idStore: int = Path(..., description="ID del punto vendita"),
    param_days: Optional[int] = Query(None, alias="param.days", description="Numero di giorni"),
    param_user_id: Optional[int] = Query(None, alias="param.user_id", description="ID dell'utente")
):
    """Restituisce i documenti chiusi per un punto vendita."""
    return []
