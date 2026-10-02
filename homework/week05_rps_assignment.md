# Assignment — Rock Paper Scissors: Play It, Then Make It Yours

**Software Programming (IGS1931) · Individual assignment**

You get a tiny, working Rock Paper Scissors game (`week05_rps_starter.py`). Your job is to **play it, break it, and upgrade it level by level**.

- **Due:** Monday, October 5, 2026, 23:55
- **Submit:** upload **one** `.py` file to iClass, named `StudentID_rps.py` (e.g. `12345678_rps.py`).

## Submission rules

1. **Complete at least Levels 1–4.** The levels build on each other, so your single file should contain the work of every level up to the one you reached.
2. Levels 5 and 6 are **extra** and earn bonus credit.
3. At the top of the file, fill in your name, student ID, and the levels you completed. Put a `# LEVEL n` comment above the code for each level.
4. The file must run with `python3 yourfile.py` without errors. A file that crashes on start gets no credit for the levels in it.
5. Work individually. You may use only what we've covered in class (`if`/`elif`/`else`, functions, `return`, recursion, `input`, `random`, string methods).

## Getting started

Run the starter a few times:

```
python3 week05_rps_starter.py
```

New tools in the starter:

| Tool | What it does | Example |
|---|---|---|
| `random.randint(a, b)` | random whole number from `a` to `b` (both included) | `random.randint(1, 3)` → `1`, `2` or `3` |
| `input(prompt)` | shows `prompt` and returns what the user typed **as a string** | `name = input("Name? ")` |

### Read it
1. Which lines make the computer's choice? What do `1`, `2`, `3` stand for?
2. Where are the three ways the player can win? What does the final `else` mean?
3. How many rounds does the game play?

### Try to break it
Run it and try each input. Write down what happens and what *should* happen.

| Type this | Expected | What actually happens? |
|---|---|---|
| `ROCK` | works like `rock` | ? |
| `  rock` (leading spaces) | works like `rock` | ? |
| `banana` | an error message, not a loss | ? |
| (anything) | I get to keep playing | ? |

---

## The levels

Save a working copy before starting each new level.

### Level 1 — Forgiving input *(Easy)*
**Done when:** `ROCK`, `  Rock`, and `rock   ` all behave exactly like `rock`.

*Hint: strings have `.strip()` (removes spaces at both ends) and `.lower()`. Chain them: `answer.strip().lower()`.*

### Level 2 — Handle bad input *(Easy → Medium)*
**Done when:** typing `banana` prints a friendly message instead of "You lose!".

- **2a.** Print `That's not a valid move!` and don't play the round.
- **2b.** Ask again by making your function call itself (recursion). What is the base case — when does it stop asking?

*Hint: a move is valid if it is `"rock"` **or** `"paper"` **or** `"scissors"`.*

### Level 3 — Split it into functions *(Medium)*
Split the one big function so each piece has one job:

- `computer_choice()` — returns `"rock"`, `"paper"` or `"scissors"` at random
- `decide_winner(player, computer)` — **returns** `'player'`, `'computer'` or `'draw'` (no printing)
- `play()` — asks the player, calls the two functions above, prints the result

**Done when:** the game plays as before **and** these all hold:

- `decide_winner('rock', 'scissors')` ➞ `'player'`
- `decide_winner('rock', 'paper')` ➞ `'computer'`
- `decide_winner('paper', 'paper')` ➞ `'draw'`

*Why: now you can test `decide_winner` with fixed values, which is impossible while the computer's choice is random.*

### Level 4 — A real match: first to 2 wins *(Medium → Hard)*
**Done when:** the game keeps playing rounds and shows the score until someone reaches **2 round wins**. Draws don't count.

Write `play_match(player_score, computer_score)` using **recursion, with the scoreboard as the arguments**:

| Situation | Action |
|---|---|
| `player_score == 2` | print `*** You win the match! ***` *(base case)* |
| `computer_score == 2` | print `*** Computer wins the match! ***` *(base case)* |
| otherwise | print the score, play one round, call `play_match` again with the **updated** scores |

Start the game with `play_match(0, 0)`. Example run:

```
Score - You: 0 Computer: 0
rock, paper or scissors? paper
Computer chose: rock
You win this round!
Score - You: 1 Computer: 0
rock, paper or scissors? rock
Computer chose: rock
Draw!
Score - You: 1 Computer: 0
rock, paper or scissors? scissors
Computer chose: rock
Computer wins this round!
Score - You: 1 Computer: 1
...
*** You win the match! ***
```

### Level 5 — Play again? *(Medium, extra)*
**Done when:** after a match ends, the game asks `Play again? (y/n)`. On `y` it starts a fresh match; on anything else it prints `Thanks for playing!`.

*Hint: recursion again — `play_again()` calls `play_match(0, 0)` and then itself.*

### Level 6 — Make it yours *(Challenge, extra — pick any)*
- **Shortcuts:** accept `r`, `p`, `s` as well as the full words.
- **Best of N:** add a `wins_needed` parameter to `play_match` so one function plays first-to-2 or first-to-5.
- **Trash talk:** the computer says something different depending on the score.
- **Rock Paper Scissors Lizard Spock:** add two more moves. Is there a smarter rule than listing every winning pair?
- **Cheat detector:** if the player types `CHEAT`, warn them and give the computer the round.
- **Your own idea!**

---

## Grading (suggested — adjust as needed)

| Part | Points |
|---|---|
| Level 1 | 20 |
| Level 2 | 20 |
| Level 3 | 20 |
| Level 4 | 20 |
| Code runs, is readable, header filled in | 20 |
| Level 5 (extra) | +5 |
| Level 6 (extra) | +5 |
