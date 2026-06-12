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
|21 | "Go Higher" hint | "Go LOWER" hint | |
|Set the difficulty to Easy | range of guess should be 1 to 20 | range remains at 0 to 100 (normal difficulty)| an "easy" guess can still be outide of the expected range (i.e. 48)|
|Setting the difficulty to Hard has a range of 1 to 50 | one would expect a larger range for Hard than for Normal (0-100)| a larger range | range is 0 - 50 | range remains at 0-100 for all three difficulties

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
