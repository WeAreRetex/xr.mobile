from pydantic import BaseModel, Field
from typing import List, Optional, Any, Dict
from datetime import datetime
from enum import Enum


# Common models and enums
class MisuraType(BaseModel):
    unità: Optional[str] = None
    quantità: Optional[float] = None


class IVAType(BaseModel):
    desc: Optional[str] = None
    val: Optional[int] = Field(None, ge=0, le=100)


class CodiceVendita(BaseModel):
    codice: Optional[str] = None
    tipo: Optional[int] = None
    moltiplicatore: Optional[int] = None
    divisore: Optional[int] = None


class Variante(BaseModel):
    codice: Optional[str] = None
    nome: Optional[str] = None


# Anagrafica_Info models
class TipoDocumenti(BaseModel):
    id: Optional[str] = None
    descrizione: Optional[str] = None
    numeroObbligatorio: Optional[bool] = None
    fornitore: Optional[bool] = None
    magazzino: Optional[bool] = None
    deposito: Optional[bool] = None
    soloFuturi: Optional[bool] = None


class PossibiliCapacita(BaseModel):
    bolle: Optional[bool] = None
    image: Optional[bool] = None
    modificaGiacenza: Optional[bool] = None
    modificaPrezzo: Optional[bool] = None
    modificaPromozioni: Optional[bool] = None
    modificaScortaMin: Optional[bool] = None
    nrm: Optional[bool] = None
    promozioni: Optional[bool] = None
    stampaEtichetta: Optional[bool] = None
    storico: Optional[bool] = None


class Anagrafica_Info(BaseModel):
    ora: Optional[str] = None
    nomeProgramma: Optional[str] = None
    nomeNegozio: Optional[str] = None
    versioneDB: Optional[int] = None
    centrale: Optional[bool] = None
    tipiDocumenti: Optional[List[TipoDocumenti]] = None
    capacita: Optional[PossibiliCapacita] = None


# Anagrafica_Articoli models
class Anagrafica_Articoli(BaseModel):
    codice: str
    descrizione: str
    prezzo: Optional[float] = None
    prezzoOriginale: Optional[float] = None
    misura: Optional[MisuraType] = None
    iva: Optional[IVAType] = None
    giacenza: Optional[float] = None
    scortaMinima: Optional[float] = None
    stato: Optional[str] = None
    venditaAPeso: Optional[bool] = None
    promozione: Optional[str] = None
    codiciVendita: Optional[List[CodiceVendita]] = None
    ultimoFornitore: Optional[str] = None
    dataAcquisto: Optional[datetime] = None
    quantitàAcquisto: Optional[float] = None
    costoAcquisto: Optional[float] = None
    dataOrdine: Optional[datetime] = None
    quantitàOrdine: Optional[float] = None
    costoOrdine: Optional[float] = None
    dataVendita: Optional[datetime] = None
    quantitàVendita: Optional[float] = None
    codReparto: Optional[str] = None
    reparto: Optional[str] = None
    tipo: Optional[int] = None
    codDeposito: Optional[str] = None
    deposito: Optional[str] = None
    varianti: Optional[List[Variante]] = None


# Anagrafica_Items models
class Anagrafica_Items(BaseModel):
    codice: str
    descrizione: str
    prezzo: Optional[float] = None
    prezzoOriginale: Optional[float] = None
    misura: Optional[MisuraType] = None
    iva: Optional[IVAType] = None
    giacenza: Optional[float] = None
    scortaMinima: Optional[float] = None
    stato: Optional[str] = None
    venditaAPeso: Optional[bool] = None
    promozione: Optional[str] = None
    codiciVendita: Optional[List[CodiceVendita]] = None
    ultimoFornitore: Optional[str] = None
    dataAcquisto: Optional[datetime] = None
    quantitàAcquisto: Optional[float] = None
    costoAcquisto: Optional[float] = None
    dataOrdine: Optional[datetime] = None
    quantitàOrdine: Optional[float] = None
    costoOrdine: Optional[float] = None
    dataVendita: Optional[datetime] = None
    quantitàVendita: Optional[float] = None
    codReparto: Optional[str] = None
    reparto: Optional[str] = None
    tipo: Optional[int] = None
    codDeposito: Optional[str] = None
    deposito: Optional[str] = None
    categoria: Optional[str] = None
    categoriaDes: Optional[str] = None
    classe: Optional[str] = None
    classeDes: Optional[str] = None
    suddivisione1: Optional[str] = None
    suddivisione1Des: Optional[str] = None
    suddivisione2: Optional[str] = None
    suddivisione2Des: Optional[str] = None
    suddivisione3: Optional[str] = None
    suddivisione3Des: Optional[str] = None
    suddivisione4: Optional[str] = None
    suddivisione4Des: Optional[str] = None
    suddivisione5: Optional[str] = None
    suddivisione5Des: Optional[str] = None
    suddivisione6: Optional[str] = None
    suddivisione6Des: Optional[str] = None
    codiceTLCentrale: Optional[str] = None
    varianti: Optional[List[Variante]] = None


# Anagrafica_Fornitori model
class Anagrafica_Fornitori(BaseModel):
    codice: Optional[str] = None
    descrizione: Optional[str] = None
    indirizzo: Optional[str] = None
    città: Optional[str] = None
    cap: Optional[str] = None
    primario: Optional[int] = None


# Anagrafica_ArtFor models
class InfoCodice(BaseModel):
    codice: Optional[str] = None
    descrizione: Optional[str] = None
    tipo: Optional[int] = None
    dataNPO: Optional[datetime] = None
    misura: Optional[MisuraType] = None


class Listino(BaseModel):
    prezzo: Optional[float] = None
    dataInizio: Optional[datetime] = None
    dataFine: Optional[datetime] = None
    codice: Optional[str] = None


class Anagrafica_ArtFor(BaseModel):
    articolo: Optional[str] = None
    fornitore: Optional[str] = None
    codici: Optional[List[InfoCodice]] = None
    codiciScan: Optional[List[str]] = None
    pezziCartone: Optional[int] = None
    listiniCartone: Optional[bool] = None
    stato: Optional[str] = None
    dataNPO: Optional[datetime] = None
    ordinabile: Optional[bool] = None
    nrm: Optional[bool] = None
    listini: Optional[List[Listino]] = None
    dataAcquisto: Optional[datetime] = None
    quantitàAcquisto: Optional[float] = None
    valoreAcquisto: Optional[float] = None
    dataOrdine: Optional[datetime] = None
    quantitàOrdine: Optional[float] = None
    valoreOrdine: Optional[float] = None
    sostituto: Optional[str] = None


# Anagrafica_Promozioni models
class PromoArticolo(BaseModel):
    articolo: Optional[str] = None
    tipo: Optional[int] = None
    valore: Optional[float] = None
    descrizione: Optional[str] = None


class Anagrafica_Promozioni(BaseModel):
    codice: Optional[str] = None
    descrizione: Optional[str] = None
    dataInizio: Optional[datetime] = None
    dataFine: Optional[datetime] = None
    note: Optional[str] = None
    oldGuid: Optional[str] = None
    origine: Optional[int] = None
    articoli: Optional[List[PromoArticolo]] = None


# Anagrafica_Storico model
class Anagrafica_Storico(BaseModel):
    giorno: Optional[int] = None
    mese: Optional[int] = None
    quantita: Optional[float] = None
    valore: Optional[float] = None


# Anagrafica_StoricoVendite model
class Anagrafica_StoricoVendite(BaseModel):
    data_riferimento: Optional[str] = None
    quantita: Optional[float] = None
    valore: Optional[float] = None
    iva: Optional[str] = None


# Anagrafica_StoricoAcquisti model
class Anagrafica_StoricoAcquisti(BaseModel):
    data_riferimento: Optional[str] = None
    quantita: Optional[float] = None
    valore: Optional[float] = None
    iva: Optional[str] = None
    fornitore: Optional[str] = None


# Bolla models
class Riga(BaseModel):
    articolo: Optional[str] = None
    quantita: Optional[float] = None


class RigaVerifica(BaseModel):
    articolo: Optional[str] = None
    ean: Optional[str] = None
    quantita: Optional[float] = None


class Verifica(BaseModel):
    bolle: Optional[List[str]] = None
    righe: Optional[List[RigaVerifica]] = None


class Bolla(BaseModel):
    codice: Optional[str] = None
    tipo: Optional[str] = None
    numero: Optional[str] = None
    data: Optional[datetime] = None
    fornitore: Optional[str] = None
    note: Optional[str] = None
    righe: Optional[List[Riga]] = None


# Anagrafica_RigheNRM models
class Acquisti_NRM(BaseModel):
    descrizione: Optional[str] = None
    codice: Optional[str] = None
    valore: Optional[float] = None
    prezzo: Optional[float] = None
    promo: Optional[bool] = None
    pezziCartone: Optional[int] = None
    fattorePrezzo: Optional[float] = None


class Ordine_NRM(BaseModel):
    codice: Optional[str] = None
    valore: Optional[float] = None


class Anagrafica_RigheNRM(BaseModel):
    deposito: Optional[str] = None
    codice: Optional[str] = None
    codVen: Optional[str] = None
    acquisti: Optional[List[Acquisti_NRM]] = None
    categoria: Optional[str] = None
    iva: Optional[int] = None
    prezzo: Optional[float] = None


# Anagrafica_Depositi model
class Anagrafica_Depositi(BaseModel):
    codDeposito: Optional[str] = None
    deposito: Optional[str] = None


# Anagrafica_Scadenze model
class Anagrafica_Scadenze(BaseModel):
    item_code: Optional[str] = None
    qty: Optional[str] = None
    start_expiry_date: Optional[datetime] = None
    end_expiry_date: Optional[datetime] = None
    action: Optional[str] = None
    state: Optional[str] = None
    expired: Optional[bool] = None
    id_row: Optional[int] = None
    id_user: Optional[int] = None
    name_user: Optional[str] = None


# Anagrafica_StoricoOrdini models
class RigaOrdine(BaseModel):
    item_supplier: Optional[str] = None
    item_code: Optional[str] = None
    amount: Optional[float] = None
    package_amount: Optional[float] = None
    pieces_package: Optional[float] = None


class Anagrafica_StoricoOrdini(BaseModel):
    order_code: Optional[str] = None
    order_number: Optional[str] = None
    order_date: Optional[datetime] = None
    supplier: Optional[str] = None
    notes: Optional[str] = None
    rows: Optional[List[RigaOrdine]] = None
