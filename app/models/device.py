from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime


class Position(BaseModel):
    latitude: Optional[float] = None
    longitude: Optional[float] = None


class Log(BaseModel):
    modulo: Optional[str] = None
    messaggio: Optional[str] = None
    eccezione: Optional[str] = None
    IDUtente: Optional[int] = None
    dataOraDevice: Optional[datetime] = None
    exceptionHttpCod: Optional[str] = None
    exceptionHttpMsg: Optional[str] = None


class AnagraficaWSInfo(BaseModel):
    address: Optional[str] = None
    sent: Optional[bool] = None
    connected: Optional[bool] = None


class DocType(BaseModel):
    id_type: Optional[str] = None
    desc_type: Optional[str] = None


class DocMember(BaseModel):
    id_member: Optional[str] = None
    desc_member: Optional[str] = None
    in_out: Optional[str] = None


class DocConfigDett(BaseModel):
    key_data: Optional[str] = None
    is_modify: Optional[bool] = None
    is_visible: Optional[bool] = None
    label_data: Optional[str] = None
    is_mandatory: Optional[bool] = None


class DocConfig(BaseModel):
    type: Optional[DocType] = None
    id_data: Optional[str] = None
    desc_data: Optional[str] = None
    members: Optional[List[DocMember]] = None
    configurations_data: Optional[List[DocConfigDett]] = None
    is_processing: Optional[bool] = None
    is_enabled: Optional[bool] = None


class ModuleAlert(BaseModel):
    id_module: Optional[str] = None
    threshold: Optional[int] = None
    rates_alert: Optional[List[int]] = None


class DeviceProp(BaseModel):
    appRelease: Optional[str] = None
    androidVersion: Optional[str] = None
    deviceModel: Optional[str] = None


class Moduli(BaseModel):
    canUseCamera: Optional[bool] = None
    attivaVibrazione: Optional[bool] = None
    attivaParlato: Optional[bool] = None
    moduloFoto: Optional[bool] = None
    moduloDocumenti: Optional[bool] = None
    moduloOrdini: Optional[bool] = None
    moduloInventari: Optional[bool] = None
    moduloClienti: Optional[bool] = None
    moduloBolle: Optional[bool] = None
    moduloSpesa: Optional[bool] = None
    moduloCesti: Optional[bool] = None
    editEtichetta: Optional[bool] = None
    editPrezzo: Optional[bool] = None
    editGiacenze: Optional[bool] = None
    editPromo: Optional[bool] = None
    editScortaMin: Optional[bool] = None
    visioneCompleta: Optional[bool] = None
    depositi: Optional[bool] = None
    moduloOrdiniMF: Optional[bool] = None
    moduloRaccoltaArticoli: Optional[bool] = None
    numGGmoduloFoto: Optional[int] = None
    numGGmoduloDocumenti: Optional[int] = None
    numGGmoduloClienti: Optional[int] = None
    numGGmoduloOrdini: Optional[int] = None
    numGGmoduloInventari: Optional[int] = None
    numGGmoduloBolle: Optional[int] = None
    numGGmoduloSpesa: Optional[int] = None
    numGGmoduloCesti: Optional[int] = None
    numGGmoduloRaccoltaArticoli: Optional[int] = None
    moduloScadenze: Optional[bool] = None
    numGGmoduloScadenze: Optional[int] = None
    moduloCalendario: Optional[bool] = None
    numGGmoduloCalendario: Optional[int] = None
    articoloNoAnagraDocumenti: Optional[bool] = None
    articoloNoAnagraOrdini: Optional[bool] = None
    articoloNoAnagraInventari: Optional[bool] = None
    articoloNoAnagraBolle: Optional[bool] = None
    articoloNoAnagraSpesa: Optional[bool] = None
    articoloNoAnagraCesti: Optional[bool] = None
    articoloNoAnagraRaccoltaArticoli: Optional[bool] = None
    articoloNoAnagraScadenze: Optional[bool] = None
    articoloNoFornitoreDocumenti: Optional[bool] = None
    articoloNoFornitoreOrdini: Optional[bool] = None


class DeviceSetting(BaseModel):
    idPuntoVendita: Optional[int] = None
    numGiorniSellin: Optional[int] = None
    numColliMax: Optional[int] = None
    tipiCodiciVendita: Optional[List[int]] = None
    idScandIt: Optional[int] = None
    chiaveScandIt: Optional[str] = None
    tipiCodiciDocumenti: Optional[List[int]] = None
    tipiCodiciOrdini: Optional[List[int]] = None
    tipiCodiciInventari: Optional[List[int]] = None
    tipiOffertaPrezziReparti: Optional[List[str]] = None
    cassaSpesaAssistita: Optional[int] = None
    negozio: Optional[int] = None
    moduli: Optional[Moduli] = None
    idCentrale: Optional[int] = None
    descPuntoVendita: Optional[str] = None
    descCentrale: Optional[str] = None
    gruppiUtenti: Optional[List[int]] = None
    trasferimentiPossibili: Optional[bool] = None
    macAddress: Optional[str] = None
    name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    endAuthorization: Optional[datetime] = None
    lastConnected: Optional[datetime] = None
    lastModification: Optional[datetime] = None
    lastSetup: Optional[datetime] = None
    setup: Optional[int] = None
    resetDB: Optional[bool] = None
    versioneApp: Optional[int] = None
    appAuth: Optional[int] = None
    anagraficaWS: Optional[str] = None
    anagraficaWS_sent: Optional[bool] = None
    anagraficaWS_connected: Optional[bool] = None
    iconicMobileNew: Optional[bool] = None
    appAuthNew: Optional[int] = None
