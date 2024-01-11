import requests

class GitHubAPI:
    def __init__(self, token):
        self.headers = {"Authorization": f"Bearer {token}"}

    def get_repository_code(self, repo_name):
        url = f"https://api.github.com/repos/{repo_name}/contents"
        return requests.get(url, headers=self.headers).json()

    def get_file_content(self, repo_name, file_path):
        url = f"https://api.github.com/repos/{repo_name}/contents/{file_path}"
        content = requests.get(url, headers=self.headers).json()
        return content.get('content', '')
    
    