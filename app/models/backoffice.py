from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
from uuid import UUID


# BackOfficeModifications models
class GuidCnt(BaseModel):
    id: Optional[UUID] = None


class ModificheBO(BaseModel):
    id: Optional[UUID] = None
    mac: Optional[str] = None
    idPV: Optional[int] = None
    deviceDescription: Optional[str] = None
    idUser: Optional[int] = None
    userDescription: Optional[str] = None
    dataOraDevice: Optional[datetime] = None
    dataOraServer: Optional[datetime] = None
    dataOraApplicazioneBackOffice: Optional[datetime] = None
    dataOraApplicazioneServer: Optional[datetime] = None
    soggetto: Optional[str] = None
    modifica: Optional[int] = None
    valore: Optional[Any] = None
    dataInizioAzione: Optional[datetime] = None
    dataFineAzione: Optional[datetime] = None
    dataScadenza: Optional[datetime] = None
    action: Optional[str] = None


class ModificaMsg(BaseModel):
    data: Optional[datetime] = None
    idUtente: Optional[int] = None
    idPV: Optional[int] = None
    valore: Optional[Any] = None


class InfoPromozione(BaseModel):
    descrizione: Optional[str] = None
    dataInizio: Optional[datetime] = None
    dataFine: Optional[datetime] = None


class PromoMsg(BaseModel):
    valore: Optional[InfoPromozione] = None
    data: Optional[datetime] = None
    idUtente: Optional[int] = None
    idPV: Optional[int] = None


class InfoOfferta(BaseModel):
    promozione: Optional[str] = None
    tipo: Optional[int] = None
    valore: Optional[float] = None


class OffertaMsg(BaseModel):
    valore: Optional[InfoOfferta] = None
    data: Optional[datetime] = None
    idUtente: Optional[int] = None
    idPV: Optional[int] = None


class ScadenzeMsg(BaseModel):
    action: Optional[str] = None
    item_code: Optional[str] = None
    start_expiry_date: Optional[datetime] = None
    end_expiry_date: Optional[datetime] = None
    expiry_date: Optional[datetime] = None
    qty: Optional[float] = None
    state: Optional[str] = None


class RootScadenzeMsg(BaseModel):
    date: Optional[datetime] = None
    user_id: Optional[int] = None
    store_id: Optional[int] = None
    list_of_expire: Optional[List[ScadenzeMsg]] = None


class Centrale(BaseModel):
    ID: Optional[int] = None
    CodiceBO: str
    Descrizione: str
    trasferimenti: Optional[bool] = None


class PuntoVendita(BaseModel):
    ID: Optional[int] = None
    CodicePV: str
    Descrizione: Optional[str] = None
    CodiceWS: Optional[int] = None
    IDCentrale: Optional[int] = None
    urlWS: Optional[str] = None
