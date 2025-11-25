import asyncio
import datetime

from pydantic import HttpUrl

from src.ai.ArxivJudger import ArxivJudger
from src.models.Arxiv import ArxivArticle, ArxivMetaData


async def main():
    article = ArxivArticle(index=1, arxiv_id='2511.17926', category='cs.SD',
                           abs_url=HttpUrl('https://arxiv.org/abs/2511.17926'),
                           pdf_url=HttpUrl('https://arxiv.org/pdf/2511.17926'), html_url=None,
                           other_url=HttpUrl('https://arxiv.org/format/2511.17926'),
                           title='Three-Class Emotion Classification for Audiovisual Scenes Based on Ensemble Learning Scheme',
                           authors=['Xiangrui Xiong', 'Zhou Zhou', 'Guocai Nong', 'Junlin Deng', 'Ning Wu'],
                           comments=None, subjects_primary='Sound (cs.SD)',
                           subjects_other=['Human-Computer Interaction (cs.HC)'],
                           abstract='Emotion recognition plays a pivotal role in enhancing human-computer interaction, particularly in movie recommendation systems where understanding emotional content is essential. While multimodal approaches combining audio and video have demonstrated effectiveness, their reliance on high-performance graphical computing limits deployment on resource-constrained devices such as personal computers or home audiovisual systems. To address this limitation, this study proposes a novel audio-only ensemble learning framework capable of classifying movie scenes into three emotional categories: Good, Neutral, and Bad. The model integrates ten support vector machines and six neural networks within a stacking ensemble architecture to enhance classification performance. A tailored data preprocessing pipeline, including feature extraction, outlier handling, and feature engineering, is designed to optimize emotional information from audio inputs. Experiments on a simulated dataset achieve 67% accuracy, while a real-world dataset collected from 15 diverse films yields an impressive 86% accuracy. These results underscore the potential of audio-based, lightweight emotion recognition methods for broader consumer-level applications, offering both computational efficiency and robust classification capabilities.',
                           scraped_at=datetime.datetime(2025, 11, 25, 8, 24, 13, 284940, tzinfo=datetime.timezone.utc),
                           metadata=ArxivMetaData(figures=[], texts=[]))
    judger = ArxivJudger()
    res = await judger.judge(article)
    print(res.model_dump_json())


if __name__ == '__main__':
    asyncio.run(main())
