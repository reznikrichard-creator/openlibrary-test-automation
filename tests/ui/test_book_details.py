from tests.ui.steps import search_for_books, save_results
import pytest

@pytest.mark.skip(reason="Blocked by human verification")

def test_book_details(page, home, product_details):

    # 1. Search for The Hobbit
    search_for_books(home, "The Hobbit")

    # 2. Save search result information
    search_title, search_author = save_results(home)

    # 3. Click the first result
    home.search_rows.first.click()

    # 4. Check for human verification
    verification = page.get_by_role(
        "button", name="Verify you are human"
    )

    if verification.is_visible():
        print("Human verification required")
        page.pause()

    # 5. Get title from details page
    product_details.hobbit_title.wait_for(state="visible")
    details_title = product_details.hobbit_title.inner_text().strip()

    # 6. Get author from details page
    product_details.book_author.wait_for(state="visible")
    details_author = product_details.book_author.inner_text().strip()

    # 7. Compare titles
    assert search_title == details_title, (
        f"Title mismatch: Expected '{search_title}', got '{details_title}'"
    )

    # 8. Compare authors
    assert search_author == details_author, (
        f"Author mismatch: Expected '{search_author}', got '{details_author}'"
    )