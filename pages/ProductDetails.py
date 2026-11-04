from playwright.sync_api import Page


class ProductDetails:
    def __init__(self, page: Page):
        self.page = page

        self.hobbit_title = page.get_by_role("heading", name="The Hobbit")
        self.details_author = page.locator(".result__author")
    