from playwright.sync_api import Page


HOME_URL = "https://play.ludigames.com"


def accept_cookies(page: Page):

    try:
        page.get_by_role(
            "button",
            name="Agree and close: Agree to our"
        ).click(timeout=3000)

    except Exception:
        print("Cookie banner not displayed.")


def test_duplicate_category_detection(page: Page):

    categories = [
        "Action games",
        "Sport games",
        "Family games",
        "Casual games",
        "Racing games",
        "Adventure games",
        "Simulation games",
        "Strategy games",
        "Logic games",
        "Boardgames",
        "All games"
    ]

    page.goto(HOME_URL)

    accept_cookies(page)

    visited_urls = []

    for category in categories:

        page.goto(HOME_URL)

        page.wait_for_timeout(2000)

        page.get_by_role(
            "link",
            name=category,
            exact=True
        ).click()

        page.wait_for_timeout(3000)

        current_url = page.url

        print(f"{category}: {current_url}")

        visited_urls.append(current_url)

    unique_urls = set(visited_urls)

    assert len(unique_urls) == len(categories), (
        "Duplicate category pages detected."
    )
