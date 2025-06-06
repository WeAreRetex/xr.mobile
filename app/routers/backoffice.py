from fastapi import APIRouter, Path, Body, HTTPException
from typing import List, Optional, Dict, Any
from app.models.backoffice import (
    ModificheBO, GuidCnt, ModificaMsg, PromoMsg, OffertaMsg, RootScadenzeMsg,
    Centrale, PuntoVendita
)
from uuid import UUID
from datetime import datetime

router = APIRouter()


@router.head("/")
async def head():
    """Endpoint per verificare se il servizio di back office è attivo."""
    return {}


@router.get("/{id}", response_model=List[ModificheBO])
async def get_modifiche(
    id: int = Path(..., description="ID del punto vendita")
):
    """Restituisce le modifiche per un punto vendita."""
    return []


@router.post("/{id}", response_model=bool)
async def post_modifica(
    id: UUID = Path(..., description="ID della modifica"),
    dataOra: datetime = Body(..., description="Data e ora della modifica")
):
    """Aggiunge una modifica per un ID specifico."""
    return True


@router.get("/{mac}/{id}/{ore}", response_model=List[GuidCnt])
async def get_modifiche_applicate(
    mac: str = Path(..., description="MAC address del dispositivo"),
    id: int = Path(..., description="ID del punto vendita"),
    ore: int = Path(..., description="Ore da considerare")
):
    """Restituisce le modifiche applicate per un dispositivo e punto vendita."""
    return []


@router.post("/etichetta/{mac}/{codice}", response_model=str)
async def post_etichetta(
    mac: str = Path(..., description="MAC address del dispositivo"),
    codice: str = Path(..., description="Codice articolo"),
    info: ModificaMsg = Body(..., description="Informazioni sulla modifica")
):
    """Aggiorna l'etichetta di un articolo."""
    return "OK"


@router.post("/prezzo/{mac}/{codice}", response_model=str)
async def post_prezzo(
    mac: str = Path(..., description="MAC address del dispositivo"),
    codice: str = Path(..., description="Codice articolo"),
    info: ModificaMsg = Body(..., description="Informazioni sulla modifica")
):
    """Aggiorna il prezzo di un articolo."""
    return "OK"


@router.post("/giacenza/{mac}/{codice}", response_model=str)
async def post_giacenza(
    mac: str = Path(..., description="MAC address del dispositivo"),
    codice: str = Path(..., description="Codice articolo"),
    info: ModificaMsg = Body(..., description="Informazioni sulla modifica")
):
    """Aggiorna la giacenza di un articolo."""
    return "OK"


@router.post("/scortaMin/{mac}/{codice}", response_model=str)
async def post_scorta_min(
    mac: str = Path(..., description="MAC address del dispositivo"),
    codice: str = Path(..., description="Codice articolo"),
    info: ModificaMsg = Body(..., description="Informazioni sulla modifica")
):
    """Aggiorna la scorta minima di un articolo."""
    return "OK"


@router.post("/promo/{mac}/{codice}", response_model=str)
async def post_promo(
    mac: str = Path(..., description="MAC address del dispositivo"),
    codice: str = Path(..., description="Codice articolo"),
    info: PromoMsg = Body(..., description="Informazioni sulla promozione")
):
    """Aggiorna la promozione di un articolo."""
    return "OK"


@router.post("/offerta/{mac}/{codice}", response_model=str)
async def post_offerta(
    mac: str = Path(..., description="MAC address del dispositivo"),
    codice: str = Path(..., description="Codice articolo"),
    info: OffertaMsg = Body(..., description="Informazioni sull'offerta")
):
    """Aggiorna l'offerta di un articolo."""
    return "OK"


@router.post("/expire/{mac}", response_model=str)
async def post_expire(
    mac: str = Path(..., description="MAC address del dispositivo"),
    info: RootScadenzeMsg = Body(..., description="Informazioni sulle scadenze")
):
    """Aggiorna le scadenze."""
    return "OK"


@router.get("/centrali", response_model=List[Centrale])
async def get_centrali():
    """Restituisce la lista delle centrali."""
    return []


@router.get("/pv/{id}", response_model=List[PuntoVendita])
async def get_punti_vendita(
    id: int = Path(..., description="ID della centrale")
):
    """Restituisce la lista dei punti vendita per una centrale."""
    return []
