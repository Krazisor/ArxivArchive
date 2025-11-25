import asyncio

from src.workflows.ArxivDailyWorkflow import ArxivDailyWorkflow


async def main():
    workflow = ArxivDailyWorkflow('cs.AI')
    await workflow.run(without_analyze=True)

if __name__ == '__main__':
    asyncio.run(main())