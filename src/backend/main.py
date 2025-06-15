from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.get_game_info import router as hltb_router

import debugpy
debugpy.listen(("0.0.0.0", 5678))
print("⏳ Esperando debugger en el puerto 5678...")

app = FastAPI()

app.include_router(hltb_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_methods=["*"],
    allow_headers=["*"],
)
