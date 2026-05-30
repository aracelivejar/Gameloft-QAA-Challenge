# Test Case 1

## UI - Search Quality Test

### Business Question

If a user searches for a game, can they find it?

### Manual Test

#### Positive Scenario

**Search**

* Merge Dragons

**Verify**

* Results appear
* Merge Dragons is displayed
* User can open the game page

**Expected Result**

The search returns relevant results and allows access to the game.



#### Negative Scenario

**Search**

* zzzzzzzzzzzzzzzz
* xxxxxxxxxxxxxxx
* ccccccccccccc

**Verify**

* Results appear
* Message displayed:

  * "We don't have that title yet. You can try our Top 10 games!"
* User can open the game page

**Expected Result**

The system informs the user that no matching title exists and suggests alternative games.



# Test Case 2

## UI - Category Health Check

### Business Question

Can users browse categories successfully?

### Manual Test

#### Positive Scenario

**Open**

* Action Games
* Sport Games
* Family Games
* Casual Games
* Racing Games
* Adventure Games
* Simulation Games
* Strategy Games
* Logic Games
* Boardgames
* All Games

**Verify**

* Category page loads successfully
* Games are displayed

**Expected Result**

Every category contains playable games.



#### Negative Scenario

**Open**

* Action Games
* Sport Games
* Family Games
* Casual Games
* Racing Games
* Adventure Games
* Simulation Games
* Strategy Games
* Logic Games
* Boardgames
* All Games

**Verify**

* Category is not empty
* No blank category page exists

**Expected Result**

Users always see game content.


# Test Case 3

## UI - Game Launch Consistency

### Business Question

Can users actually start games?

### Positive Scenario

**Open games from:**

* Action Games
* Sport Games
* Family Games
* Casual Games
* Racing Games
* Adventure Games
* Simulation Games
* Strategy Games
* Logic Games
* Boardgames
* All Games

**Verify**

* Category page loads
* At least one game is available
* User can open a game
* URL contains `game.html`
* Game container loads

**Expected Result**

Every category contains at least one game that launches successfully.


# Test Case 4

## UI - Duplicate Game Detection

### Business Question

Are categories showing unique content?

### What We Verify

For every category:

* Action Games
* Sport Games
* Family Games
* Casual Games
* Racing Games
* Adventure Games
* Simulation Games
* Strategy Games
* Logic Games
* Boardgames
* All Games

### We Will

* Open the category
* Count game cards
* Save the category URL
* Verify categories are different

**Expected Result**

Users are not always seeing the same category page.
