#### BBOXX: Battling Knights Challenge

This game is designed to automate the battle between 4 knights who can use 
different items to enhance their abilities for attacking and defencing.

**Requirements:** `Python3.6+`

**Run the code:** `python3 main.py`

**Run test cases:**  `python3 test.py`

##### Game Flow:

    - Load moves from the `moves.txt` file.
    - Setup arena by placing knights and items on their specific blocks.
    - Apply the moves one by one and state will be changed as per the rules.
    - Once all the moves are applied, save the final state in `final_state.json` file.
    
#### Exceptions:

    - Knights except [Y, R, B, G] will not be entertained.
    - Directions except [N, E, W, S] will not be followed. 
    - Move should be in the form of `<knight-id>:<direction-id>`.
    - moves.txt should exist in the directory.

###### **Developed by:** __Malik Ammar Akbar__

