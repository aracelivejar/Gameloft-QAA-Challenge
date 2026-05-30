from playwright.sync_api import Page


SEARCH_URL = "https://play.ludigames.com/search.html"


def accept_cookies(page: Page):
    try:
        page.get_by_role(
            "button",
            name="Agree and close: Agree to our"
        ).click(timeout=3000)

    except Exception:
        print("Cookie banner not displayed.")

    """
    Positive Scenario:
    Search for Merge Dragons
    Verify:
    - Result appears
    - User can open game page
    """


def test_search_merge_dragons(page: Page):

    page.goto(SEARCH_URL)

    accept_cookies(page)

    search_box = page.get_by_role(
        "textbox",
        name="Enter game name"
    )

    search_box.fill("Merge Dragons")
    search_box.press("Enter")

    page.wait_for_timeout(2000)

    result = page.get_by_text("Merge Dragons")

    assert result.is_visible(), (
        "Merge Dragons was not displayed in search results."
    )

    result.click()

    page.wait_for_timeout(3000)

    print(page.url)

    assert "game.html" in page.url.lower(), (
        "Game page did not open."
    )


"""
    Negative Scenario:
    Search for invalid game names
    Verify:
    - No matching result is found
    - Alternative recommendations are shown
    """


def test_search_invalid_games(page: Page):

    page.goto(SEARCH_URL)

    accept_cookies(page)

    invalid_games = [
        "zzzzzzzzzzzzzzzz",
        "xxxxxxxxxxxxxxx",
        "ccccccccccccc"
    ]

    for game in invalid_games:

        search_box = page.get_by_role(
            "textbox",
            name="Enter game name"
        )

        search_box.fill("")
        search_box.fill(game)
        search_box.press("Enter")

        page.wait_for_timeout(3000)

        # print(f"\nSearching for: {game}")
        # print(page.locator("body").inner_text())

        assert page.locator("text=Top 10").first.is_visible(), (
            f"Top 10 recommendations were not displayed for: {game}"
        )
