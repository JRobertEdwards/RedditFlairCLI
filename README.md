# RedditFlairCLI

## Requirements 

In order to run this script you'll need the following:

  * pip
  * python(2.7 minimum)
  * praw
  * argparse

## Clone

git clone https://github.com/JRobertEdwards/RedditFlairCLI.git

## Help (-h)

usage: redditCLI.py [-h] [-v] [-flair FLAIR] [-css CSS] sub

Can count how many flairs or flair_css_class instances you have on your
subreddit.

positional arguments:
  sub                   This is the subreddit you want to use. You don't need
                        to type 'sub' for this,it will just pick up the first
                        string you enter. An Example of this would be to type
                        something like: python3 redditCLI.py soccer -f
                        :Arsenal:

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -flair FLAIR, -f FLAIR
                        This is the flair you want to check. By Default this
                        will perform a count on all possible flairs.
  -css CSS              The flair_css_class text you want to look for.
 
## Usage - flairs

The functionality of this script is to allow you to search your own moderated subreddit for flairs that are defined by you.

In order to run this script you shoudld use a string similar to this in the console: $ py redditCLI.py dragonballfighterz -f 'DBFZ Professional'

This will return a Match message to the console with each match returned. Once the script has finished it will return a total count of those flairs matched.

## Usage - css_class

As above you can also search for flair_css_class for strings, to do this use the command: $ py redditCLI.py dragonballfighterz -css 'Reddit-Mod'

The same behaviour as flairs will be returned.
