import os
import dotenv

dotenv.load_dotenv()


class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY') or None
    OPENAI_BASE_URL = os.getenv('OPENAI_BASE_URL') or "https://api.openai.com/v1/"
    DOWNLOAD_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))),'downloads')
    ANALYZER_MODEL = os.getenv('ANALYZER_MODEL') or 'gpt-5-mini'
    MAX_FIGURE_NUM = int(os.getenv('MAX_FIGURE_NUM')) or 40
    JUDGER_MODEL = os.getenv('JUDGER_MODEL') or 'gpt-5-mini'
    RESEARCH_PERFER = os.getenv('RESEARCH_PERFER') or '<everything>'