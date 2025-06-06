from fastapi import APIRouter, Path, Body, HTTPException
from typing import List, Optional, Dict
from app.models.device import (
    DeviceSetting, Position, Log, AnagraficaWSInfo, DocConfig, 
    ModuleAlert, DeviceProp
)

router = APIRouter()


@router.get("/{mac}", response_model=DeviceSetting)
async def get_values(
    mac: str = Path(..., description="MAC address del dispositivo")
):
    """Restituisce le impostazioni per un dispositivo specifico."""
    return DeviceSetting()


@router.post("/position/{mac}", response_model=int)
async def post_position(
    mac: str = Path(..., description="MAC address del dispositivo"),
    position: Position = Body(..., description="Posizione del dispositivo")
):
    """Aggiorna la posizione di un dispositivo."""
    return 1


@router.post("/log/{mac}", response_model=bool)
async def post_log_iconic(
    mac: str = Path(..., description="MAC address del dispositivo"),
    logObj: Log = Body(..., description="Oggetto log")
):
    """Registra un log per un dispositivo."""
    return True


@router.get("/setup/{mac}", response_model=int)
async def get_setup(
    mac: str = Path(..., description="MAC address del dispositivo")
):
    """Restituisce lo stato di setup per un dispositivo."""
    return 0


@router.get("/exitSetup/{mac}")
async def get_exit_setup(
    mac: str = Path(..., description="MAC address del dispositivo")
):
    """Esce dalla modalità setup per un dispositivo."""
    return {}


@router.get("/address/{mac}", response_model=AnagraficaWSInfo)
async def get_address(
    mac: str = Path(..., description="MAC address del dispositivo")
):
    """Restituisce l'indirizzo per un dispositivo."""
    return AnagraficaWSInfo()


@router.post("/status/{mac}")
async def post_status(
    mac: str = Path(..., description="MAC address del dispositivo"),
    success: bool = Body(..., description="Stato di successo")
):
    """Aggiorna lo stato di un dispositivo."""
    return {}


@router.get("/setResetDB/{mac}")
async def get_set_reset(
    mac: str = Path(..., description="MAC address del dispositivo")
):
    """Imposta il reset del database per un dispositivo."""
    return {}


@router.post("/version/{mac}")
async def post_version(
    mac: str = Path(..., description="MAC address del dispositivo"),
    versione: int = Body(..., description="Versione dell'app")
):
    """Aggiorna la versione dell'app per un dispositivo."""
    return {}


@router.get("/apk/{mac}")
async def get_apk(
    mac: str = Path(..., description="MAC address del dispositivo")
):
    """Restituisce l'APK per un dispositivo."""
    return {}


@router.get("/configData/{mac}/{userId}", response_model=List[DocConfig])
async def get_config_data(
    mac: str = Path(..., description="MAC address del dispositivo"),
    userId: int = Path(..., description="ID dell'utente")
):
    """Restituisce i dati di configurazione per un dispositivo e utente."""
    return []


@router.get("/moduleAlert/{mac}/{userId}", response_model=List[ModuleAlert])
async def get_module_alert(
    mac: str = Path(..., description="MAC address del dispositivo"),
    userId: int = Path(..., description="ID dell'utente")
):
    """Restituisce gli alert dei moduli per un dispositivo e utente."""
    return []


@router.get("/domain", response_model=Dict[str, str])
async def get_domain():
    """Restituisce la mappa dei domini."""
    return {}


@router.post("/infodevice/{mac}")
async def post_info_device(
    mac: str = Path(..., description="MAC address del dispositivo"),
    info: DeviceProp = Body(..., description="Proprietà del dispositivo")
):
    """Aggiorna le informazioni di un dispositivo."""
    return {}
