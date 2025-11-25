from langchain_core.messages import SystemMessage, HumanMessage

from src.ai.BaseAI import BaseAI
from src.ai.prompts.ArxivAnalyzerPrompt import AnalyzerPrompt
from src.config.Config import Config
from src.models.Arxiv import ArxivMetaData


class ArxivAnalyzer(BaseAI):
    systemMessage = SystemMessage(AnalyzerPrompt)

    def __init__(self):
        self.model.model_name = Config.ANALYZER_MODEL

    async def analyze(self, metadata: ArxivMetaData):
        images, texts = self._buildContentBlocks(metadata)
        texts.extend(images)
        humanMessage = HumanMessage(content_blocks=texts)
        messages = [self.systemMessage, humanMessage]
        res = await self.model.ainvoke(messages)
        return res

    def _buildContentBlocks(self, metadata: ArxivMetaData):
        textContentBlocks = []
        imageContentBlocks = []
        images = metadata.figures
        texts = metadata.texts
        for image in images:
            imageContentBlocks.append(self.buildB64ImageContent(image))
        for text in texts:
            textContentBlocks.append(self.buildTextContentBlock(text))
        return imageContentBlocks, textContentBlocks
