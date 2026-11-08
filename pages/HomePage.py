from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page):
        self.page = page

        # Header Area
        self.browse_button = page.get_by_role('button', name='Browse')

        # Search Area
        self.search_button = page.get_by_role("button", name="Search")

        self.search_text = page.get_by_role("searchbox", name="Search")

        # Search Results Area
        self.search_modal = page.get_by_role("dialog", name="Search Open Library")
        
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