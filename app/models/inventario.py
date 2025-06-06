from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from enum import Enum


class Elemento(BaseModel):
    id: Optional[int] = None
    codice: Optional[str] = None
    quantita: Optional[float] = None
    descrizione: Optional[str] = None
    codArticolo: Optional[str] = None
    codVend: Optional[str] = None
    tipoCodVen: Optional[int] = None
    eliminato: Optional[bool] = None
    costo: Optional[float] = None
    pezziCartone: Optional[float] = None
    repartoDes: Optional[str] = None
    giacenza: Optional[float] = None
    peso: Optional[float] = None
    prezzo: Optional[float] = None
    misura: Optional[str] = None
    venditaAPeso: Optional[bool] = None
    stato: Optional[str] = None
    fornitore: Optional[str] = None
    articoloFornitore: Optional[str] = None


class Inventario(BaseModel):
    id: Optional[int] = None
    idUtente: Optional[int] = None
    idPuntoVendita: Optional[int] = None
    note: Optional[str] = None
    ora: Optional[datetime] = None
    creazione: Optional[datetime] = None
    ultimaModifica: Optional[datetime] = None
    dataChiusura: Optional[datetime] = None
    tipo: Optional[int] = None
    stato: Optional[int] = None
    elementi: Optional[List[Elemento]] = None
    nomeUtente: Optional[str] = None


class RichiestaParametriInv(BaseModel):
    days: Optional[int] = None
    user_id: Optional[int] = None
