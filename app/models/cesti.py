from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class Riga(BaseModel):
    codice: Optional[str] = None
    quantita: Optional[int] = None
    codArticolo: Optional[str] = None
    descrizione: Optional[str] = None


class Cesto(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    idPV: Optional[int] = None
    idUserCreator: Optional[int] = None
    idUserLastMod: Optional[int] = None
    dataCreator: Optional[datetime] = None
    dataLastMod: Optional[datetime] = None
    costoConfezione: Optional[float] = None
    spesaConfezionamento: Optional[float] = None
    prezzo: Optional[float] = None
    scatola: Optional[bool] = None
    righe: Optional[List[Riga]] = None
