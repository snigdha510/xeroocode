import base64

class CodeAnalyzer:
    def __init__(self, chatgpt, github_api):
        self.chatgpt = chatgpt
        self.github_api = github_api

    def analyze_repository(self, repo_name):
        code_contents = self.github_api.get_repository_code(repo_name)
        analysis_results = []
        for file_info in code_contents:
            if file_info["type"] == "file":
                file_path = file_info["path"]
                file_content = self.github_api.get_file_content(repo_name, file_path)
                decoded_content = base64.b64decode(file_content).decode('utf-8')  # Decode the content
                analysis = self.chatgpt.analyze_code(decoded_content)  # Pass decoded content to ChatGPT
                analysis_results.append({"file": file_info["name"], "analysis": analysis})
                return analysis_results

