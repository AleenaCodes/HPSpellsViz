# Ideas

Have a nested dictionary:

Name         : Str : Name of spell

Description  : Str : Short description of spell

Total        : Int : Total number of mentions

Occurrences  : []  : Line number of each occurrence

Type         : Str : Category of spell


## Parsing

Could splice together all txt files and then run (might be a bit big though)
If statement to just get each spell out? Import as set and check if in
Find/make a list of all spells!

# Pages to Have

- Classification of spells
  - All spells and what types they are
  - Maybe have grouped and coloured?
- Most used
  - Bubbles - size depending on largest
  - Other tree-like structure may be better
- Full book
  - All 7 books with coloured dots showing where spells used
  - Keep a note which lines each book start and end on
  - Visualisation is just a matter of making dot on percentage of total number of lines

# Tasks

- Make a list of all spells
- Classify them
- Combine all books
- Parse through to get numbers
  - Script will make dict of spell name, number of occurences, and list of lines of occurences
- Combine spell categories with dictionary
  - Will need script to go through each spell name, assign category and pull in data from dictionary
- Result: full data!
