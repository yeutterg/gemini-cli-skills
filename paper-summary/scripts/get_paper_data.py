import sys
import json
import re
import urllib.request
import xml.etree.ElementTree as ET

def fetch_arxiv_metadata(arxiv_id):
    try:
        url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            root = ET.fromstring(content)
            entry = root.find('{http://www.w3.org/2005/Atom}entry')
            
            title_node = entry.find('{http://www.w3.org/2005/Atom}title')
            title = title_node.text.strip().replace('\n', ' ') if title_node is not None else "Unknown Title"
            
            authors = [auth.find('{http://www.w3.org/2005/Atom}name').text for auth in entry.findall('{http://www.w3.org/2005/Atom}author')]
            
            summary_node = entry.find('{http://www.w3.org/2005/Atom}summary')
            summary = summary_node.text.strip() if summary_node is not None else ""
            
            published_node = entry.find('{http://www.w3.org/2005/Atom}published')
            published = published_node.text if published_node is not None else ""
            
            return {
                "title": title,
                "authors": authors,
                "summary": summary,
                "published": published,
                "url": f"https://arxiv.org/abs/{arxiv_id}"
            }
    except Exception as e:
        return {"error": str(e)}

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No URL or ID provided"}))
        sys.exit(1)

    input_val = sys.argv[1]
    
    # Check for ArXiv ID in URL
    arxiv_match = re.search(r'arxiv\.org/(?:abs|pdf)/(\d+\.\d+)', input_val)
    if arxiv_match:
        metadata = fetch_arxiv_metadata(arxiv_match.group(1))
        print(json.dumps(metadata))
    else:
        # Placeholder for other sources or direct text
        print(json.dumps({"input": input_val, "type": "unknown"}))

if __name__ == "__main__":
    main()
