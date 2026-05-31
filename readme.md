# Test Scenario 1

## UI - Search Quality Test

### Test Question:

If a user searches for a game, can they find it?

### Test Objective:
Validate that the search functionality returns relevant results for a valid game title.

### Test actions:
* Open https://play.ludigames.com
* Open the Search page
* Enter "Merge Dragons" in the search field
* Submit the search

 ### Expected Results
* Search results are displayed
* "Merge Dragons" appears in the results
* The game page can be opened from the search results

#### Manual Test

#### Test Positive Scenario:

* Open https://play.ludigames.com
* Open the Search page
* Enter "Merge Dragons" in the search field
* Submit the search
  
**Expected Result**

The search returns relevant results and allows access to the game.

**Test Observations**

* Results appear
* Merge Dragons is displayed
* User can open the game page

#### Test Negative Scenario

* Open https://play.ludigames.com
* Open the Search page
* Enter "zzzzzzzzzzzzzzzz" in the search field
* Submit the search
* Enter "xxxxxxxxxxxxxxx" in the search field
* Submit the search
* Enter "ccccccccccccc" in the search field
* Submit the search

**Expected Result**

The system informs the user that no matching title exists and suggests alternative games.

**Test Observations**

* Message displayed:
   "We don't have that title yet. You can try our Top 10 games!"
* User can choose one of 10 suggested games


# Test Scenario 2

## UI - Category Health Check

### Test Question

Can users browse categories successfully?

### Test Objective:
Validate that all game categories load successfully and contain playable game content.

### Test Actions:
* Open https://play.ludigames.com
* Open the following categories:
   *  Action Games
   * Sport Games
   * Family Games
   * Casual Games
   * Racing Games
   * Adventure Games
   * Simulation Games
   * Strategy Games
   * Logic Games
   * Boardgames
   *  All Games
      
 ### Expected Results
* Category page loads successfully
* Games are displayed
* Category contains playable game content


### Manual Test

#### Test Positive Scenario

**Open**

   *  Action Games
   * Sport Games
   * Family Games
   * Casual Games
   * Racing Games
   * Adventure Games
   * Simulation Games
   * Strategy Games
   * Logic Games
   * Boardgames
   *  All Games

### Expected Result

* Category page loads successfully
* Games are displayed
*  User can browse available games

### Test Observations

* Category page loads successfully
* Games are displayed
* User can browse available games


#### Test Negative Scenario

**Open**

   *  Action Games
   * Sport Games
   * Family Games
   * Casual Games
   * Racing Games
   * Adventure Games
   * Simulation Games
   * Strategy Games
   * Logic Games
   * Boardgames
   *  All Games

### Expected Result

* Every category contains playable games.
* Users always see game content.

### Test Observations

* Category is not empty
* No blank category page exists
* Games are displayed in every category


# Test Scenario 3

## UI - Game Launch Consistency

### Test Question

Can users actually start games?

### Test Objective:

Validate that users can successfully launch games from every category and access playable content

### Test Actions:
* Open https://play.ludigames.com
* Open the following categories:
   *  Action Games
   * Sport Games
   * Family Games
   * Casual Games
   * Racing Games
   * Adventure Games
   * Simulation Games
   * Strategy Games
   * Logic Games
   * Boardgames
   *  All Games
* Open a game from each category
  
### Expected Result

* Category page loads
* At least one game is available
* User can open a game
* URL contains `game.html`
* Game container loads

**Expected Result**
* Users can always access playable game content after selecting a game.

### Test Observations
* No blank game page is displayed
* No error page is displayed
* Game container is available
* Game launches successfully

# Test Scenario 4

## UI - Duplicate Game Detection

### Test Question

Are games correctly categorized?

### Test Objective:

Validate that games are not unexpectedly duplicated across different categories.

### Test Actions:

* Open https://play.ludigames.com
* Open Action Games
* Collect visible game titles
* Open Racing Games
* Collect visible game titles
* Compare game titles between categories

### Expected Results

* Categories contain game titles
* Duplicate games can be identified
* Categories provide distinct game collections

### Manual Test

#### Test Positive Scenario

**Open**

* Action Games
* Racing Games

### Expected Result

Each category contains games relevant to that category and distinct game collections.

### Test Observations

* Categories display game titles
* Categories contain distinct game collections
* Most games are unique to their category
* Games are relevant to their respective category

#### Test Negative Scenario

**Open**

* Action Games
* Racing Games

### Expected Result

No unexpected duplicate games appear across categories.

### Test Observations

* The same game appears in multiple categories
* Duplicate games are detected
* Categories may not be properly differentiated
* Games may not be correctly categorized

# Test Scenario 5

## API - Homepage Response Time

### Test Question

Does the homepage respond successfully and within an acceptable time?

### Test Objective:

Validate that the homepage is available, returns a successful response, and responds within the expected performance threshold.

### Test Actions:

* Send a GET request to https://play.ludigames.com
* Measure the response time
* Capture the HTTP status code

### Expected Results

* Homepage returns HTTP 200
* Homepage is available
* Response time is below 3 seconds
* Users can access the homepage without noticeable delays

### Manual Test

#### Test Positive Scenario

**Open**

* https://play.ludigames.com

### Expected Result

The homepage loads successfully and responds within 3 seconds.

### Test Observations

* Homepage is reachable
* HTTP status code is 200
* Response time is below 3 seconds
* Users can access the homepage successfully

#### Test Negative Scenario

**Open**

* https://play.ludigames.com

### Expected Result

The homepage should not return server errors or exceed the expected response time threshold.

### Test Observations

* HTTP status code is not 200
* Homepage is unavailable
* Response time exceeds 3 seconds
* Users may experience delays or be unable to access the homepage


