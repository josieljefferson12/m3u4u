import requests
import time

def download_file(url, output_file):
    """Baixa um arquivo da URL e salva localmente."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(output_file, 'wb') as file:
            file.write(response.content)
        print(f"Arquivo salvo com sucesso: {output_file}")
    except requests.RequestException as e:
        print(f"Erro ao baixar o arquivo: {e}")

def update_m3u():
    """Atualiza a lista M3U."""
    m3u_url = "http://m3u4u.com/m3u/xe47yz1pd9spv21mn9vq"
    download_file(m3u_url, "playlist.m3u")

def update_epg():
    """Atualiza o EPG."""
    epg_url = "http://m3u4u.com/epg/xe47yz1pd9spv21mn9vq"
    download_file(epg_url, "epg.xml")

if __name__ == "__main__":
    # Baixa a lista M3U
    update_m3u()
    
    # Aguarda 5 minutos (300 segundos)
    print("Aguardando 5 minutos antes de atualizar o EPG...")
    time.sleep(300)
    
    # Baixa o EPG
    update_epg()
