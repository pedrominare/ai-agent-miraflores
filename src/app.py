# =============================================================================
# FastAPI app - rotas da API do Lambda
# Input bem definido via Pydantic para validacao automatica
# =============================================================================

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Agent API", version="0.1.0")


class MessageInput(BaseModel):
    """Input da rota de teste - mensagem do usuario."""

    mensagem: str = Field(..., min_length=1, max_length=5000, description="Mensagem do usuario")


@app.post("/test")
async def rota_teste(data: MessageInput):
    """
    Rota de teste: recebe JSON e retorna eco com validacao.
    Exemplo de input:
    {
        "mensagem": "mensagem do usuario"
    }
    """
    return {
        "status": "ok",
        "message": "Input recebido e validado",
        "recebido": {
            "mensagem": data.mensagem,
        },
    }

# =============================================================================