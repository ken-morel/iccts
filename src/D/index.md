# Problem D: Word search puzzle

This word search puzzle required an implementation of an algorithm able to generate a 10x10 letter grid in the form of a word puzzle from a list of input words.

## Algotithm description

The algorithm associated with this exercise tries to split the creation operations into simple steps.

## Algotithm implementation

###### Input

- **Input**:
  The algorithm first get's it's input data as an list of strings which are to be present into the puzzle.
  The input are expected to be maximum 10 character words.
- **Normalization**:
  The input strings are all capitalized and striped to a ten characters length to prevent errors and unexpected behaviours.

###### The board

The board is a 10x10 grid of characters, represented as a python list subclass. It's is initially filled of `N`, representing empty cells which can be replaced.

###### Inserting a word

- **Orientation**:
  Adding a word to the puzzle is done via a simple procedure. The algorithm randomly decides the orientation of the new word and tries to place it in that direction before the opposite direction.
- **Position determination**:
  The possible positions for the new word are found and stored in an array, this positions is simply gotten by finding all grids in the board which allow the word to be fully placed.
  - The possitioner algorithm looking for possible positions maps tries to check if every character either falls on an empty cell(which contains a `N` constant), or which value is the actual letter, making word crossing possible and a better game.
  - The final location is finally chosen at random from the available positions.
- **Positioning**: The word is then placed at the location and the others are attempted to be placed too.
- **Filling**: After this, the empty cells of the board are felt with random alphabet letters.

### Randomization

The setup of the algorithm makes it to be able to find good and hopefully nice-to-play word arrangements from random selection and by getting all possible positions as stated previously, making it to have a low error rate even when getting to 5 words 5 characters long, but for a great improvement the algorithm tries several random posisions repeatedly, emit's an exception in case of error which calls upon the retry of the board positioning all over from it's initial state, upon a fixed number of retries.

## Conclusion

This algorithm works to effectively produce a letter grid even given a few short words.
Code associated with this excercise is available at [./main.py]
