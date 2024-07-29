import json
import os

# Função para formatar o tempo em milissegundos para o formato [mm:ss.SSS]
def format_time(ms):
    minutes = ms // 60000
    seconds = (ms % 60000) // 1000
    milliseconds = ms % 1000
    return f"[{minutes:02}:{seconds:02}.{milliseconds:03}]"

# Nome do arquivo JSON
filename = "lyric.json"

# Obter o diretório do script atual
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, filename)

# Carregar o arquivo JSON
try:
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Verificar se a chave "lyrics" e "lines" estão presentes no JSON
    if "lyrics" in data and "lines" in data["lyrics"]:
        lines = data["lyrics"]["lines"]
        for line in lines:
            start_time_ms = int(line["startTimeMs"])
            words = line["words"]
            print(f"{format_time(start_time_ms)} {words}")
    else:
        print("Erro: chave 'lines' não encontrada no JSON")
except FileNotFoundError:
    print(f"Erro: arquivo '{filename}' não encontrado no diretório '{script_dir}'")
except json.JSONDecodeError:
    print(f"Erro: não foi possível decodificar o arquivo '{filename}' como JSON")

