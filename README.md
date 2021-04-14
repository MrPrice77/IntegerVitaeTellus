# Integer Vitae Tellus

## Project Overview
There are many cookbooks online that allow people to search up a bunch of recipes. Most of those recipes are provided and the user
has no personal connection, making the cookbook just a basic source on the internet. Libro di cucina adds a personal touch to online
cookbooks allowing users to add their own recipes.

## Features
* Recipe of the Day
* Recipe Search
* Mark as favorite
* Add Recipe with image
* Comment and add personal images to recipes
* Create Group
* Join Group

### User Stories
"As a **user**, I want to see a **daily** recipe suggestion, so for those times when **I cannot decide on what to cook** I have a suggestion."  return
"As a **user**, I want to be able to **search** for a specific recipe, so **I can cook that meal**."  return
"As a **user**, I want to be able to **share my own recipes**, so **others can enjoy them** as much as I do."
"As a **user**, I want to **share my thoughts** on recipes, so **others can see how I added my personal touch or what I thought of the meal**."
"As a **user**, I want to **share images of my meal**, so **others can see how my meal turned out** following the recipe."
"As a **user**, I want to **create a group recipe book**, so my **family can easily share recipes** among each other."


### Tasks
* Store db of recipes
* Filter recipes by contents
* Add comments to recipes
* Add images to recipes
* Add my own recipes
* Create Groups/Cookbooks
* Share Recipes/Groups

"As a **moderator**, I want to be able to **remove recipes, comments, and/or images if necessary**."


### Functionality
* Recipe of the Day on Home Page
* User create account or login

* User Permissions:
    - Search for and share recipes
    - Mark recipe as favorite
    - Comment on Recipes
    - Post Recipes
    - Post images of meal made with recipe
    - Join or create groups

**Possible Features:**
* User Created Groups/Recipe Books
    - Group Owner permissions:
        - Manage recipes, comments, and images
        - Manage moderators

    - Group Moderator permissions:
        - Manage recipes, comments, and images


## Models

* Recipes:
    - Title
    - Image
    - Ingredients
    - Instructions
    - Source - User, Website, or Cookbook
    - Comments
    - Gallery

* User Profile:
    - Name
    - E-Mail
    - Favorite Food
    - Avatar
    - Favorite Recipe
    - Recipes
    - Groups

* Groups:
    - Name
    - Owner
    - Members
    - Recipes


## Schedule

*Milestone 1:*
* Starter Recipe Database
* User Profiles

*Milestone 2:*
* Landing Page
* Recipe Pages
* Recipe of the Day
* Recipe Search

*Milestone 3:*
* User added recipes
* Recipe Moderation

*Milestone 4:*
* User comments on Recipes
* User images on Recipes

*Milestone 5:*
* User groups/cookbooks
* Groups/cookbooks search
* Group member management/moderation
