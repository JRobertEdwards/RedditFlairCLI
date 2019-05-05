# RedditFlairCLI

## Requirements 

In order to run this script you'll need the following:

*pip
*python(2.7 minimum)
*praw
*argparse

## Usage - flairs

The functionality of this script is to allow you to search your own moderated subreddit for flairs that are defined by you.

In order to run this script you shoudld use a string similar to this in the console: $ py redditCLI.py dragonballfighterz -f 'DBFZ Professional'

This will return a Match message to the console with each match returned. Once the script has finished it will return a total count of those flairs matched.

## Usage - css_class

As above you can also search for flair_css_class for strings, to do this use the command: $ py redditCLI.py dragonballfighterz -css 'Reddit-Mod'

The same behaviour as flairs will be returned.
