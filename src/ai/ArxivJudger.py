from langchain.agents import create_agent
from langchain_core.messages import SystemMessage, HumanMessage
from src.ai.BaseAI import BaseAI
from src.ai.prompts.JudgerPrompt import JudgerPrompt
from src.config.Config import Config
from src.models.Arxiv import ArxivArticle, JudgeResult


class ArxivJudger(BaseAI):
    systemMessage = SystemMessage(content=JudgerPrompt)

    def __init__(self):
        self.model.model_name = Config.JUDGER_MODEL
        self.judgeAgent = create_agent(self.model, response_format=JudgeResult)

    async def judge(self, article: ArxivArticle) -> JudgeResult:
        humanMessage = HumanMessage(content=f"""文章元信息:\n{article.model_dump_json(ensure_ascii=False)}""")
        res = await self.judgeAgent.ainvoke({"messages": [self.systemMessage, humanMessage]})  # type: ignore
        return res['structured_response']
