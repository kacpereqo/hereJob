from src.scrappers.justJoinIt import JustJoinItScrapper


class ScrapperService:
    # def __init__(self) -> None:
    # self.scrappers = [JustJoinItScrapper()]
    # self.threads: list[Thread] = []

    # self.start_threads()

    # def start_threads(self) -> None:
    #     for scrapper in self.scrappers:
    #         thread = Thread(target=scrapper.scrap)
    #         self.threads.append(thread)
    #         thread.start()

    # def join_threads(self) -> None:
    #     for thread in self.threads:
    #         thread.join()

    def start(self) -> None:
        # self.scrappers[0].scrap()
        JustJoinItScrapper().scrap()

        # print("Scraping finished")
