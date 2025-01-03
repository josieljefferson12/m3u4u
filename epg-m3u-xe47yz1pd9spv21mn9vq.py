import requests

def download_file(url, output_file):
    """Baixa o arquivo da URL especificada e salva localmente."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve erro na solicitação
        with open(output_file, 'wb') as file:
            file.write(response.content)
        print(f"Arquivo atualizado e salvo em: {output_file}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar o arquivo: {e}")

def update_epg():
    """Atualiza o arquivo EPG."""
    epg_url = "http://m3u4u.com/epg/xe47yz1pd9spv21mn9vq"  # Substitua pela URL do EPG
    output_file = "epg.xml"
    download_file(epg_url, output_file)

def update_m3u():
    """Atualiza o arquivo M3U."""
    m3u_url = "http://m3u4u.com/m3u/xe47yz1pd9spv21mn9vq"  # Substitua pela URL do M3U
    output_file = "playlist.m3u"
    download_file(m3u_url, output_file)

if __name__ == "__main__":
    print("Atualizando EPG...")
    update_epg()
    print("Atualizando lista M3U...")
    update_m3u()