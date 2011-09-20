Principles: 

Keep original data pristine.
If necessary, preprocess it to fix whatever bugs.
Don't change the source data.

Need to standardize on a text data format. I think probably yaml would be best. Require virtuallly no parsing.

Previously, I did this:
Had to change the lineups for Dallas / Chicago game on 3/18/2000.  No substitution times listed.
FIXME: I should go back and replace this with the original file.


Current data types:

drafts:
 - list of real and fictional drafts
 - all MLS drafts
 - BigSoccer USMNT drafts.

lineups:
 - list of all-time lineups for mls. (from scaryice)

lists:
 - lists of awards, mostly. Non-quantifiable stuff.

people:
 - old mls/usl bios from me.
 - salaries data.

# Should probably replace these with a wikipedia scraper?
places:
 - list of countries by population
 - list of states with population