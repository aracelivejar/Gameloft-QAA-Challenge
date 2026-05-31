"""
Gameloft QA Automation Challenge

Autor: Araceli Duenas Bejar
"""

# ============= TEST SCENARIO 1 ====================
# ========= Search Quality Test ====================

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

# ============== Positive Scenaro =================


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

    assert "game.html" in page.url.lower(), (
        "Game page did not open."
    )

# ============== Negative Scenario =================


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

        assert page.locator("text=Top 10").first.is_visible(), (
            f"Top 10 recommendations were not displayed for: {game}"
        )

# ============= TEST SCENARIO 2 ====================
# ========= Category Health Check ====================


HOME_URL = "https://play.ludigames.com"


def accept_cookies(page: Page):
    try:
        page.get_by_role(
            "button",
            name="Agree and close: Agree to our"
        ).click(timeout=3000)

    except Exception:
        print("Cookie banner not displayed.")

# ============== Positive & Negative Scenario =================


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

        game_links = page.locator(
            "a[href*='game.html']"
        )

        assert game_links.count() > 0, (
            f"No games found in {category}."
        )

        print(
            f"{category}: {game_links.count()} games found"
        )

# ============= TEST SCENARIO 3 ====================
# ========= Game Launch Consistency ================


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

        assert "category.html" in page.url.lower(), (
            f"{category} page did not load."
        )

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
# ============= TEST SCENARIO 4 ====================
# ========= Duplicate Game Detection ===============


HOME_URL = "https://play.ludigames.com"


def accept_cookies(page: Page):
    try:
        page.get_by_role(
            "button",
            name="Agree and close: Agree to our"
        ).click(timeout=3000)

    except Exception:
        print("Cookie banner not displayed.")

# ============== Positive & Negative Scenario =================


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

    category_games = {}

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

        game_urls = game_links.evaluate_all(
            "(elements) => elements.map(e => e.href)"
        )

        category_games[category] = set(game_urls)

        print(
            f"{category}: {len(game_urls)} games found"
        )

    duplicate_games = {}

    for i, category_a in enumerate(categories):

        for category_b in categories[i + 1:]:

            duplicates = (
                category_games[category_a]
                &
                category_games[category_b]
            )

            if duplicates:

                duplicate_games[
                    f"{category_a} <-> {category_b}"
                ] = duplicates

    if duplicate_games:

        print("\nDuplicate games detected:")

        for pair, games in duplicate_games.items():

            print(
                f"{pair}: {len(games)} duplicate games"
            )

    print(
        f"\nTotal category overlaps found: "
        f"{len(duplicate_games)}"
    )

    assert len(category_games) == len(categories), (
        "Not all categories were analyzed."
    )
