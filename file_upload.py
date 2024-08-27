import requests

def upload_file(url, file_path):
    with open(file_path, 'rb') as f:
        files = {'file': (file_path, f)}
        response = requests.post(url, files=files)
        response.raise_for_status()
        print(f"Uploaded {file_path} to {url}")

# Example usage
upload_file('http://your-public-ip:8000/upload.php', 'localfile.txt')
