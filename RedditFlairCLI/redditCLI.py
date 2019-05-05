import argparse
from reddit import reddit

def check_for_flairs(args):
    sub = str(args.sub[0]).strip('[]\' ')
    flair_count = 0
    if(args.flair):
        # Characters must be stripped due to the way that ArgParse handles user inputs.
        flair_entered = str(args.flair[0]).strip('[]\' ')
        sub = str(args.sub[0])
        print(type(sub))
        this_sub = reddit.subreddit(sub)
        for flair in this_sub.flair(limit=None):
            if flair['flair_text'] == flair_entered:
                print('Match')
                flair_count += 1
    if(args.css):
        cs = str(args.css[0]).strip('[]\' ')
        # Characters must be stripped due to the way that ArgParse handles user inputs.
        this_sub = reddit.subreddit(sub)
        for flair in this_sub.flair(limit=None):
            if flair['flair_css_class'] == cs:
                print('Match')
                flair_count += 1
    return print('Flair Count: ',  flair_count)


# This is the CLI you can use to determine the functions of this program. This was initially only designed to be used for selecting a subreddit to point at.
parser = argparse.ArgumentParser(description='Can count how many flairs or flair_css_class instances you have on your subreddit.', add_help='This is a test.')
parser.add_argument('sub', nargs=1, type=str, help='This is the subreddit you want to use. You don\'t need to type \'sub\' for this,'
                    'it will just pick up the first string you enter. \n\n An Example of this would be to type something like: '
                    'python3 redditCLI.py soccer -f :Arsenal:')
parser.add_argument('-v', '--version', action='version', version='Flair Counter-CLI 1.0')
parser.add_argument('-flair', '-f', nargs=1, type=str,  help='This is the flair you want to check. By Default this will '
                    'perform a count on all possible flairs.', action='append')
parser.add_argument('-css', nargs=1, type=str, help='The flair_css_class text you want to look for.')
args = parser.parse_args()
parser.set_defaults(func=check_for_flairs(args))

