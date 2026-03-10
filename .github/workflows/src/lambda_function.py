# =============================================================================
# Handler principal do Lambda - padrão lambda_function.lambda_handler
# Chamado via Function URL (HTTP)
# =============================================================================

import json


def lambda_handler(event, context):
    """
    Handler padrão do Lambda.
    event: dict com a requisição HTTP (Function URL)
    context: objeto com informações da execução
    """
    # Corpo da requisição (POST)
    body = {}
    if event.get("body"):
        try:
            body = json.loads(event["body"])
        except json.JSONDecodeError:
            body = {"raw": event["body"]}

    # Headers da resposta (CORS para chamadas do navegador)
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
    }

    # Exemplo de resposta
    resultado = {
        "status": "ok",
        "mensagem": "Lambda funcionando",
        "body_recebido": body,
    }

    return {
        "statusCode": 200,
        "headers": headers,
        "body": json.dumps(resultado),
    }

# =============================================================================
