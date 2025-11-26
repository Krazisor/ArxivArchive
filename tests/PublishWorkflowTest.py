from src.workflows.ArxivDailyPublishWorkflow import ArxivDailyPublishWorkflow

if __name__ == '__main__':
    pub = ArxivDailyPublishWorkflow()
    pub.publish_markdown()
