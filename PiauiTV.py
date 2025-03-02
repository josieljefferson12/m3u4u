import requests
import time

def download_file(url, output_file):
    """Faz o download de um arquivo e salva no disco."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica erros na solicitação
        with open(output_file, 'wb') as file:
            file.write(response.content)
        print(f"Arquivo atualizado e salvo em {output_file}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar o arquivo de {url}: {e}")

def update_m3u():
    """Atualiza a lista M3U."""
    m3u_url = "http://m3u4u.com/m3u/jq2zy9epr3bwxmgwyxr5"  # URL da lista M3U
    output_file = "PiauiTV.m3u"
    download_file(m3u_url, output_file)

def update_epg():
    """Atualiza o EPG."""
    epg_url = "http://m3u4u.com/m3u/jq2zy9epr3bwxmgwyxr5"  # URL do EPG
    output_file = "PiauiTV.xml.gz"
    download_file(epg_url, output_file)

if __name__ == "__main__":
    # Executa a atualização da lista M3U e do EPG
    update_m3u()
    time.sleep(120)  # Aguarda 2 minutos antes de atualizar o EPG
    update_epg()

