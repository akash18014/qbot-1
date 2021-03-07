# qbot-1

A simple discord bot for help with online quizzing.

## Discord Setup

- The quizmaster needs to be assigned a ```QM``` role.
- Roles for each team in the format ```team-{number}```. For example, ```team-1```, ```team-2```. 
    - Private team text and voice channels in the same format mentioned above that require the specific role for access.
- A ```pounce``` channel 

## Commands

The prefix for the commands is a fullstop ```.```

### QM Commands
- ```start``` - Sets up the pounce and team channels
- ```sp``` - Start Pounce to enable pounces.
- ```cp``` - Close Pounce to disable pounces.
    - By default, **pounce is enabled**.
- ```hint {sample hint}``` - Sends a clue/hint to the teams in their respective text channels.

### Participant Commands
- ```join {number}``` - Assigns the specific team role to the user. For example ```.join 1```
- ```p {answer}``` - Pounce
- ```clues``` - Sends a message to the QM asking for a clue
- ```object``` - Sends a message to the QM objecting to clues.


## Hopeful Future Additions
- Managing scores.
- Some voice channel functionality.