# bot_initializer.py

# Declaração e inicialização das variáveis
BOT_NAME = "RPA_FINANCEIRO_01"   # String
MAX_RETRIES = 3                  # Integer
EXECUTION_TIMEOUT = 120.5        # Float (segundos)
IS_PRODUCTION = True             # Boolean

# Impressão da mensagem de inicialização formatada
print("=== Inicialização do Robô ===")
print(f"BOT_NAME: {BOT_NAME} | Tipo: {type(BOT_NAME)}")
print(f"MAX_RETRIES: {MAX_RETRIES} | Tipo: {type(MAX_RETRIES)}")
print(f"EXECUTION_TIMEOUT: {EXECUTION_TIMEOUT} | Tipo: {type(EXECUTION_TIMEOUT)}")
print(f"IS_PRODUCTION: {IS_PRODUCTION} | Tipo: {type(IS_PRODUCTION)}")
print("==============================")
