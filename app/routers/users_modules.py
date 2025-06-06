from fastapi import APIRouter, Path
from app.models.users_modules import UsersModules

router = APIRouter()


@router.get("/{idUtente}", response_model=UsersModules)
async def get_config(
    idUtente: int = Path(..., description="ID dell'utente")
):
    """Restituisce la configurazione dei moduli per un utente."""
    return UsersModules()
