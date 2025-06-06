# IconicMobileWeb API

Questo progetto è un'implementazione FastAPI delle API definite nel file `swagger.json`.

## Struttura del Progetto

```
tl.mobile.api/
├── app/
│   ├── models/
│   │   ├── anagrafica.py
│   │   ├── backoffice.py
│   │   ├── cesti.py
│   │   ├── device.py
│   │   ├── device_user.py
│   │   ├── documenti.py
│   │   ├── inventario.py
│   │   ├── raccolte.py
│   │   └── users_modules.py
│   └── routers/
│       ├── anagrafica.py
│       ├── backoffice.py
│       ├── cesti.py
│       ├── device.py
│       ├── device_user.py
│       ├── documenti.py
│       ├── inventario.py
│       ├── raccolte.py
│       └── users_modules.py
├── main.py
├── requirements.txt
└── swagger.json
```

## Installazione

1. Clonare il repository
2. Installare le dipendenze:

```bash
pip install -r requirements.txt
```

## Avvio del Server

```bash
uvicorn main:app --reload
```

Il server sarà disponibile all'indirizzo: http://localhost:8000

## Documentazione API

Una volta avviato il server, è possibile accedere alla documentazione interattiva delle API:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Implementazione

Il progetto è strutturato seguendo i principi di FastAPI:

- Modelli Pydantic per la validazione dei dati in `app/models/`
- Router FastAPI per gestire le endpoint in `app/routers/`
- Main app che riunisce tutti i router

L'implementazione attuale è uno scheletro che rispetta la struttura definita in `swagger.json`, ma le funzioni restituiscono dati fittizi. Per un'implementazione completa, è necessario integrare un database e implementare la logica di business nelle funzioni di router.
