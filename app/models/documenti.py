from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from enum import Enum


class RigaDocumento(BaseModel):
    id: Optional[int] = None
    codice: str
    quantita: float
    codArticolo: Optional[str] = None
    codVend: Optional[str] = None
    tipoCodVend: Optional[int] = None
    descrizione: Optional[str] = None
    codVariante: Optional[str] = None
    descrizioneVariante: Optional[str] = None
    fornitore: Optional[str] = None
    articoloFornitore: Optional[str] = None
    costo: Optional[float] = None
    pezziCartone: Optional[float] = None
    repartoDes: Optional[str] = None
    giacenza: Optional[float] = None
    peso: Optional[float] = None
    prezzo: Optional[float] = None
    misura: Optional[str] = None
    venditaAPeso: Optional[bool] = None
    stato: Optional[str] = None
    codiceTLCentrale: Optional[str] = None


class Documenti_Documento(BaseModel):
    id: Optional[int] = None
    idUtente: Optional[int] = None
    userDescription: Optional[str] = None
    idPuntoVendita: Optional[int] = None
    stato: Optional[int] = None
    dataCrazione: Optional[datetime] = None
    dataUltimaModifica: Optional[datetime] = None
    righe: Optional[List[RigaDocumento]] = None
    tipo: Optional[str] = None
    fornitore: Optional[str] = None
    magazzino: Optional[int] = None
    cliente: Optional[str] = None
    numero: Optional[str] = None
    deposito: Optional[str] = None
    note: Optional[str] = None
    dataDoc: Optional[datetime] = None
    dataIngresso: Optional[datetime] = None
    in_out: Optional[str] = None
    tipoScaricoTrasformazione: Optional[int] = None
    tipoTrasformazione: Optional[int] = None
    dataChiusura: Optional[datetime] = None
    uuid: Optional[str] = None


class RigaDocDevice(BaseModel):
    codice: str
    quantita: float
    codArticolo: Optional[str] = None
    codVend: Optional[str] = None
    tipoCodVend: Optional[int] = None
    descrizione: Optional[str] = None
    codVariante: Optional[str] = None
    descrizioneVariante: Optional[str] = None
    fornitore: Optional[str] = None
    articoloFornitore: Optional[str] = None
    costo: Optional[float] = None
    pezziCartone: Optional[float] = None
    repartoDes: Optional[str] = None
    giacenza: Optional[float] = None
    peso: Optional[float] = None
    prezzo: Optional[float] = None
    misura: Optional[str] = None
    venditaAPeso: Optional[bool] = None
    stato: Optional[str] = None
    codiceTLCentrale: Optional[str] = None


class RigaDocDeviceId(BaseModel):
    id: Optional[int] = None
    codice: str
    quantita: float
    codArticolo: Optional[str] = None
    codVend: Optional[str] = None
    tipoCodVend: Optional[int] = None
    descrizione: Optional[str] = None
    codVariante: Optional[str] = None
    descrizioneVariante: Optional[str] = None
    fornitore: Optional[str] = None
    articoloFornitore: Optional[str] = None
    costo: Optional[float] = None
    pezziCartone: Optional[float] = None
    repartoDes: Optional[str] = None
    giacenza: Optional[float] = None
    peso: Optional[float] = None
    prezzo: Optional[float] = None
    misura: Optional[str] = None
    venditaAPeso: Optional[bool] = None
    stato: Optional[str] = None
    codiceTLCentrale: Optional[str] = None


class DocumentoDevice(BaseModel):
    tipo: Optional[str] = None
    fornitore: Optional[str] = None
    magazzino: Optional[int] = None
    cliente: Optional[str] = None
    numero: Optional[str] = None
    deposito: Optional[str] = None
    note: Optional[str] = None
    dataDoc: Optional[datetime] = None
    dataIngresso: Optional[datetime] = None
    in_out: Optional[str] = None
    tipoScaricoTrasformazione: Optional[int] = None
    tipoTrasformazione: Optional[int] = None
    dataChiusura: Optional[datetime] = None
    uuid: Optional[str] = None


class RichiestaParametri(BaseModel):
    days: Optional[int] = None
    user_id: Optional[int] = None
