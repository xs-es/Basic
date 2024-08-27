import requests

def download_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"Downloaded {local_filename} from {url}")

# Example usage
download_file('http://your-public-ip:8000/yourfile.txt', 'localfile.txt')
