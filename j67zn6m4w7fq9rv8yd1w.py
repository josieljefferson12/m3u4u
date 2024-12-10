import requests
import xml.etree.ElementTree as ET

def download_epg(url, output_file):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve algum erro na solicitação
        with open(output_file, 'wb') as file:
            file.write(response.content)
        print(f"EPG atualizado e salvo em {output_file}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar o EPG: {e}")

def update_epg():
    epg_url = "http://m3u4u.com/epg/j67zn6m4w7fq9rv8yd1w"  # Substitua pela URL do EPG
    output_file = "epg.xml"
    download_epg(epg_url, output_file)

if __name__ == "__main__":
    # Executa a atualização do EPG
    update_epg()
