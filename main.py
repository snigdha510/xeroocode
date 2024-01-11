from utils.github import GitHubAPI
from utils.chatgpt import ChatGPT
from utils.analysis import CodeAnalyzer
from utils.report import ReportGenerator

# Set your GitHub and ChatGPT tokens here
github_token = "your github token here"
chatgpt_api_key = "your openai api key here "

# Set the GitHub repository name you want to analyze
repository_name = "snigdha510/Minor-Project---Sentiment-Analysis"

github_api = GitHubAPI(github_token)
chatgpt = ChatGPT(chatgpt_api_key)
analyzer = CodeAnalyzer(chatgpt, github_api)
report_generator = ReportGenerator()

analysis_results = analyzer.analyze_repository(repository_name)
report=report_generator.generate_report(analysis_results)
