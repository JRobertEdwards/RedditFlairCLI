import praw, pprint, argparse



reddit = praw.Reddit(client_id = 'rSQh6hxLj0xHuA',
                     client_secret = 'h2HaiKb5phWCbbEevm_1hhtwiAQ',
                     username='FighterzBPModerator',
                     password='thisisapythonscript01',
                     user_agent='FighterzRankBot')




def check_for_flairs(terminal_commands):
    print(terminal_commands)
    print(type(terminal_commands))
    print(terminal_commands)
    flair_count = 0
    # Characters must be stripped due to the way that ArgParse handles user inputs.
    # flair_entered = flair_entered.strip('[]\'')
    # sub = sub.strip('[]\' ')
    # this_sub = reddit.subreddit(sub)
    # for flair in this_sub.flair(limit=None):
    #     if flair['flair_text'] == flair_entered:
    #         print('Match')
    #         flair_count += 1

    return print('Flair Count: ' , flair_count)

def check_for_flair_css(sub, flair_entered):
    flair_count = 0
    # Characters must be stripped due to the way that ArgParse handles user inputs.
    flair_entered = flair_entered.strip('[]\'')
    sub = sub.strip('[]\' ')
    this_sub = reddit.subreddit(sub)
    print(this_sub, flair_entered)
    for flair in this_sub.flair(limit=None):
        if flair['flair_css_class'] == flair_entered:
            print('Match')
            flair_count += 1

    return print('Flair Count: ' , flair_count)


# This is the CLI you can use to determine the functions of this program. This was initially only designed to be used for selecting a subreddit to point at.
parser = argparse.ArgumentParser(description='Select a subreddit to use.', add_help='This is a test.')
parser.add_argument('sub', nargs=1, type=str, help='This is the subreddit you want to use.', action='append')
parser.add_argument('-flair', nargs=1, type=str,  help='This is the flair you want to check. By Default this will '
                    'perform a count on all possible flairs.', action='append')
parser.add_argument('-css', nargs=1, type=str, help='The flair_css_class text you want to look for.')
#subparser = parser.add_subparsers(help='Use this to analyse flair_css texts')

#parser_css = subparser.add_parser('css', help='You can use this to check against the flair_css of users.')
#parser_css.add_argument('-c', type=str, nargs=1, help='This is the css for the flair you\'re looking for')
args = parser.parse_args()
parser.set_defaults(func=check_for_flairs(args.sub))

