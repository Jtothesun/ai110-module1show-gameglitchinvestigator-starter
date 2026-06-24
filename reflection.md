# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

Developer debug info is public, user can see the answer


- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  the hint was backwards, said "go LOWER" when the guess was 20 and final guess was 61

  the input takes NEGATIVE numbers: although guess should be in range 0 to 100

  after winning a game, the "new game" button does not actually work

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|21 | "Go Higher" hint | "Go LOWER" hint | None|
|Set the difficulty to Easy | range of guess should be 1 to 20 | range remains at 0 to 100 (normal difficulty)| None |
Setting the difficulty to Hard has a range of 1 to 50 | one would expect a larger range for Hard than for Normal (0-100)| range is still 0-100 (Normal) | None|

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

  I used two checks: the game behaving correctly when I played it manually, and the pytest suite passing. A bug wasn't "fixed" just because the error message went away — for example, when I first hit the `ModuleNotFoundError`, running pytest from a different folder seemed to change the error but didn't actually solve it, so I made sure the import truly resolved and the tests collected before moving on. For each logic bug I tried to write a test that would fail on the broken version and pass on the fixed one, so I had proof rather than a guess.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

  I wrote `test_too_high_on_even_attempt_does_not_add_points`, which asserts `update_score(100, "Too High", 2) == 95`. Against the original code this failed, because the old `update_score` had a hidden `attempt_number % 2 == 0` branch that *added* 5 points for a wrong guess on even attempts (returning 105). The test showed me the glitch was real and parity-dependent, and after I made both "Too High" and "Too Low" a flat −5 penalty, the test passed. I also added a `test_wrong_guesses_are_symmetric` test that loops over several attempt numbers to make sure the bug can't sneak back in.

- Did AI help you design or understand any tests? How?

  Yes. The AI helped me see that `check_guess` should return a single outcome string instead of a `(outcome, message)` tuple, because the existing tests compared the result directly to `"Win"` — that explained why my version would have failed and shaped how I wrote the function. It also helped me design the regression test for the score glitch by pointing out that the strongest test isn't just checking one number, but asserting that "Too High" and "Too Low" stay symmetric across both even and odd attempts.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  Streamlit re-runs your whole script from top to bottom every time the user interacts with anything — clicking a button, typing in a box, changing a dropdown. That means any normal variable gets recreated from scratch on every interaction, which is why a secret number generated with `random.randint` would keep changing on each click. `st.session_state` is the fix: it's a dictionary that *survives* between reruns, so anything you store there (the secret, the score, the attempt count) stays put. The pattern `if "secret" not in st.session_state:` makes sure you only set the value once and then reuse it, instead of resetting it every time the script runs again.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  Writing a test that fails on the broken code before I fix it, then confirming it passes after. Doing this for the score glitch made the bug concrete instead of something I "thought" I'd fixed, and it leaves behind a safety net so the bug can't quietly come back.

- What is one thing you would do differently next time you work with AI on a coding task?

  I would verify the AI's suggestions faster by actually running them, instead of assuming they're right. The pytest path-fix suggestion sounded reasonable but didn't work the first time, and I only found that out by running it — so next time I'll treat AI answers as a starting hypothesis to test, not a finished solution.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

  AI-generated code can look polished and "production-ready" while hiding subtle, intentional-looking bugs (like the parity tricks and the stringified secret), so I now read it more skeptically. I trust it more once I can explain why each piece works and back it up with a test, rather than because it ran without an error.
