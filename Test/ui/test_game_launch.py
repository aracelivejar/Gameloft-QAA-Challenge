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


def test_game_launch_consistency(page: Page):

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

        game_links = page.locator(
            "a[href*='game.html']"
        )

        assert game_links.count() > 0, (
            f"No games found in {category}"
        )

        first_game = game_links.first

        first_game.click()

        page.wait_for_timeout(5000)

        assert "game.html" in page.url.lower(), (
            f"Game did not open from {category}"
        )

        game_frame = page.locator("#game-frame")

        assert game_frame.count() > 0, (
            f"Game container not found for {category}"
        )
