from pydantic import BaseModel
from typing import Optional, List


class MiniUtenteDevice(BaseModel):
    id: Optional[int] = None
    userName: Optional[str] = None
    password: Optional[str] = None
    descrizione: Optional[str] = None
    ordineIcone: Optional[str] = None
