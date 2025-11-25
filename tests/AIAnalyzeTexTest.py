import asyncio
import datetime

from pydantic import HttpUrl

from src.models.Arxiv import ArxivArticle, ArxivMetaData
from src.workflows.ArxivDailyWorkflow import ArxivDailyWorkflow

async def main():
    article = ArxivArticle(index=54, arxiv_id='2511.19314', category='cs.AI', abs_url=HttpUrl('https://arxiv.org/abs/2511.19314'),
                 pdf_url=HttpUrl('https://arxiv.org/pdf/2511.19314'),
                 html_url=HttpUrl('https://arxiv.org/html/2511.19314v1'),
                 other_url=HttpUrl('https://arxiv.org/format/2511.19314'),
                 title='PRInTS: Reward Modeling for Long-Horizon Information Seeking',
                 authors=['Jaewoo Lee', 'Archiki Prasad', 'Justin Chih-Yao Chen', 'Zaid Khan', 'Elias Stengel-Eskin',
                          'Mohit Bansal'], comments='18 pages, code: this https URL',
                 subjects_primary='Artificial Intelligence (cs.AI)',
                 subjects_other=['Computation and Language (cs.CL)', 'Machine Learning (cs.LG)'],
                 abstract="Information-seeking is a core capability for AI agents, requiring them to gather and reason over tool-generated information across long trajectories. However, such multi-step information-seeking tasks remain challenging for agents backed by language models. While process reward models (PRMs) can guide agents by ranking candidate steps at test-time, existing PRMs, designed for short reasoning with binary judgment, cannot capture richer dimensions of information-seeking steps, such as tool interactions and reasoning over tool outputs, nor handle the rapidly growing context in long-horizon tasks. To address these limitations, we introduce PRInTS, a generative PRM trained with dual capabilities: (1) dense scoring based on the PRM's reasoning across multiple step quality dimensions (e.g., interpretation of tool outputs, tool call informativeness) and (2) trajectory summarization that compresses the growing context while preserving essential information for step evaluation. Extensive evaluations across FRAMES, GAIA (levels 1-3), and WebWalkerQA (easy-hard) benchmarks on multiple models, along with ablations, reveal that best-of-n sampling with PRInTS enhances information-seeking abilities of open-source models as well as specialized agents, matching or surpassing the performance of frontier models with a much smaller backbone agent and outperforming other strong reward modeling baselines.",
                 scraped_at=datetime.datetime(2025, 11, 25, 6, 40, 2, 262497, tzinfo=datetime.timezone.utc),
                 metadata=ArxivMetaData(figures=[], texts=[]))
    workflow = ArxivDailyWorkflow('cs.AI')
    metadata = await workflow._generate_metadata(article)
    article.metadata = metadata
    res = await workflow._aiAnalyzeOne(article)
    print(res.content[1].get('text'))
if __name__ == '__main__':
    asyncio.run(main())