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

    """
    Business Question:
    Can users browse categories successfully?

    Verify:
    - Category page loads
    - Category is not empty
    - At least one game is displayed
    """


def test_categories_have_games(page: Page):

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

    for category in categories:

        page.goto(HOME_URL)

        page.wait_for_timeout(2000)

        page.get_by_role(
            "link",
            name=category,
            exact=True
        ).click()

        page.wait_for_timeout(3000)

        assert "category.html" in page.url.lower(), (
            f"{category} page did not load."
        )

        game_links = page.locator("a[href*='game.html']")

        print(
            f"{category}: {game_links.count()} games found"
        )

        assert game_links.count() > 0, (
            f"No games found in {category}."
        )
