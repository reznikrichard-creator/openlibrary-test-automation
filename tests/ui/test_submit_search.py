from tests.conftest import product_details
from tests.ui.steps import search_for_books

def test_submit_search(page, home):
    search_for_books(home, "The Hobbit")
    home.submit_search_button.click()
    page.wait_for_url("https://openlibrary.org/search?q=The+Hobbit")
    assert page.url == "https://openlibrary.org/search?q=The+Hobbit"