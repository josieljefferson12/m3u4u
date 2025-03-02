python
import requests
from xml.etree.ElementTree import Element, SubElement, tostring

def fetch_m3u_file(m3u_url):
    response = requests.get(m3u_url)
    response.raise_for_status()
    return response.text

def parse_m3u(data):
    channels = []
    lines = data.splitlines()
    for i in range(len(lines)):
        if lines[i].startswith("#EXTINF"):
            channel_info = lines[i].split(",", 1)[1]
            channel_url = lines[i + 1] if (i + 1) < len(lines) else ''
            channels.append({'name': channel_info.strip(), 'url': channel_url.strip()})
    return channels

def generate_epg(channels):
    tv = Element('tv')
    for channel in channels:
        channel_elem = SubElement(tv, 'channel', id=channel['url'])
        display_name = SubElement(channel_elem, 'display-name')
        display_name.text = channel['name']
        
        # Aqui utilizamos horários de exemplo, ajuste conforme necessário
        programme = SubElement(tv, 'programme',
                               start="20230101000000 +0000", stop="20230101010000 +0000",
                               channel=channel['url'])
        title = SubElement(programme, 'title')
        title.text = f"{channel['name']} Program"
        
    return tostring(tv, encoding='unicode', method='xml')

def main():
    m3u_url = 'https://gitlab.com/josieljefferson12/playlists/-/raw/main/PiauiTV.m3u'
    m3u_data = fetch_m3u_file(m3u_url)
    channels = parse_m3u(m3u_data)
    epg_xml = generate_epg(channels)
    
    with open('epg.xml', 'w', encoding='utf-8') as file:
        file.write(epg_xml)

if __name__ == '__main__':
    main()
