# Ideas

Have a nested dictionary:

Name         : Str : Name of Spell

Total        : Int : Total number of mentions

Occurrences  : []  : Line number of each occurrence

Type         : Str : Category of spell


## Layout 2

Maybe have different structures for each page? Or one with all info, and another without list of occurrence locations

## Parsing

Could splice together all txt files and then run
If statement to just get each spell out? Import as set and check if in
Find a list of all spells!

- Keep a note which lines each book start and end on
- Visualisation is just a matter of making dot on percentage of total number of lines

# Pages to Have

- Classification of spells
  - All spells and what types they are
  - Maybe have grouped and coloured?
- Most used
  - Bubbles - size depending on largest
- Full book
  - All 7 books with coloured dots showing where spells used

# Tasks

- Make a list of all spells
- Classify them
- Combine all books
- Parse through to get numbers
  - Script will make dict of spell name, number of occurences, and list of lines of occurences
- Combine spell categories with dictionary
  - Will need script to go through each spell name, assign category and pull in data from dictionary
- Result: full data!
