from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page):
        self.page = page

        # self.search_button = page.locator("button.search-bar-trigger")
        self.search_button = page.get_by_role("button", name="Search")

        self.search_modal = page.get_by_role(
            "dialog", name="Search Open Library"
        )

        self.search_text = page.locator("input.search-input:visible")


        self.submit_search_button = page.locator(
            'button[aria-label^="See all"]'
        )

        self.search_rows = page.locator(
            "#ol-search-panel li.result-row"
        )

        self.author = page.locator(".result__author")
        self.title = page.locator(".result__title")
    
    def open(self):
        self.page.goto("/")
        return self

    def search_icon(self):
        self.search_button.click()

    def enter_search(self, title: str):
        self.search_text.fill(title)

    def submit_search(self):
        self.submit_search_button.click()