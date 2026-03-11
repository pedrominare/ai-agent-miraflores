# =============================================================================
# Handler principal do Lambda - padrão lambda_function.lambda_handler
# FastAPI + Mangum: converte evento Lambda (Function URL) em requisições ASGI
# =============================================================================

from mangum import Mangum
from src.app import app

# Mangum adapta o evento do Lambda para o FastAPI
# AWS Lambda invoca lambda_handler(event, context)
lambda_handler = Mangum(app)

# =============================================================================

# =============================================================================
# Handler principal do Lambda - padrão lambda_function.lambda_handler
# Chamado via Function URL (HTTP) - suporta GET e POST
# =============================================================================
'''
import json


def lambda_handler(event, context):
    """
    Handler padrão do Lambda.
    event: dict com a requisição HTTP (Function URL)
    context: objeto com informações da execução
    """
    http_method = event.get("requestContext", {}).get("http", {}).get("method", "GET")
    # Fallback para formato antigo do event
    if not http_method:
        http_method = event.get("httpMethod", "GET")

    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
    }

    # POST: processa o corpo da requisição
    if http_method == "POST":
        body = _parse_body(event)
        resultado = {
            "status": "ok",
            "metodo": "POST",
            "body_recebido": body,
        }
        return {
            "statusCode": 200,
            "headers": headers,
            "body": json.dumps(resultado),
        }

    # GET: usa query params se houver
    if http_method == "GET":
        query = event.get("queryStringParameters") or {}
        resultado = {
            "status": "ok",
            "metodo": "GET",
            "query_params": query,
        }
        return {
            "statusCode": 200,
            "headers": headers,
            "body": json.dumps(resultado),
        }

    # Método não suportado
    return {
        "statusCode": 405,
        "headers": headers,
        "body": json.dumps({"erro": "Método não permitido"}),
    }


def _parse_body(event):
    """Extrai e parseia o body da requisição POST."""
    body_raw = event.get("body") or "{}"
    if isinstance(body_raw, dict):
        return body_raw
    try:
        return json.loads(body_raw)
    except json.JSONDecodeError:
        return {"raw": body_raw}

# =============================================================================
'''