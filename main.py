from utils.github import GitHubAPI
from utils.chatgpt import ChatGPT
from utils.analysis import CodeAnalyzer
from utils.report import ReportGenerator

# Set your GitHub and ChatGPT tokens here
github_token = "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"
chatgpt_api_key = "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"

# Set the GitHub repository name you want to analyze
repository_name = "snigdha510/Minor-Project---Sentiment-Analysis"

github_api = GitHubAPI(github_token)
chatgpt = ChatGPT(chatgpt_api_key)
analyzer = CodeAnalyzer(chatgpt, github_api)
report_generator = ReportGenerator()

analysis_results = analyzer.analyze_repository(repository_name)
report=report_generator.generate_report(analysis_results)
