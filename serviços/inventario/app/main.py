from contextlib import asynccontextmanager

from fastapi import APIRouter, Depends, FastAPI, Query
from sqlalchemy.orm import Session

from app.auth.dependencias import exigir_perfil, usuario_atual
from app.database import Base, engine, get_db
from app.inventario import servico
from app.inventario.esquemas import AtivoCriar, AtivoSaida
from app.seguranca_http import adicionar_cabecalhos_de_seguranca


@asynccontextmanager
async def ciclo_de_vida(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="HelpDesk TI - Servico de Inventario", lifespan=ciclo_de_vida)
adicionar_cabecalhos_de_seguranca(app)

router = APIRouter(prefix="/ativos", tags=["Inventario"])


@router.post(
    "",
    response_model=AtivoSaida,
    status_code=201,
    dependencies=[Depends(exigir_perfil("tecnico", "admin"))],
)
def criar_ativo(dados: AtivoCriar, db: Session = Depends(get_db)):
    return servico.criar(db, dados)


@router.get("", response_model=list[AtivoSaida], dependencies=[Depends(usuario_atual)])
def listar_ativos(setor: str | None = Query(None, max_length=80), db: Session = Depends(get_db)):
    return servico.listar(db, setor)


@router.get("/{ativo_id}", response_model=AtivoSaida, dependencies=[Depends(usuario_atual)])
def obter_ativo(ativo_id: int, db: Session = Depends(get_db)):
    return servico.obter(db, ativo_id)


@app.get("/saude", tags=["Saude"])
def saude():
    return {"servico": "inventario", "status": "ok"}


app.include_router(router)
