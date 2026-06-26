# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  1) The hints were opposite of each other 
  2) When starting a new game, the points never restarted or zero'd out, they remained from the previous rounds
  3) The history also never cleared out either, it instead showed all the previous guesses from all the previous rounds 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| guess of 45 | hint of "Too low" when the answer is 70 | the hint given is "Too Low" instead | none |
| guess of 1222 | Message saying that the guess was out of range | hint of "Go lower" happened iniitally then it became "Go HIGHER" | none |
| second to last guess of 34| to have one more hint before it was out of attempts | Showed the answer message whilst there was still one more attempt | none |
| tried to start a new game after failing the previous one | to start a new game and reset to the beginning of the program | the program stays stuck on the previous message "Game over. Start a new game to try again."| none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
1) I used the Claude AI assistant embedded in VSCode
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
1) When pointing out the high/low hint bug, AI suggested that because there wasn't a line in the if else statement for if guess equaled secret, it threw off the logic of the if-else when it should really be if-elif-else. Also it picked out the use of st.stop and that prevents the game from restarting a new game. 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
1) The AI suggested that I should completely reorganize the section of the code that was responsible for restarting the game for a new game. We didn't need to do that, all we had to was move at max two lines and add three more lines. I tested it with the complete change and without the change and instead the tweaks to see which one worked.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
1) After I tested the code by running the program and by having the AI chat throwing the tests cases to see if the code now provides the correct output. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
1) I had pytest run a test on the high/low hints and it went through about 7 different tests to make sure 
the code behind the logic was executing correctly and producing the right output based on the user's input. The program inputed 7 to 10 different guesses that were both below and and above the number before inputting the answer.
- Did AI help you design or understand any tests? How?
1) Yes, it explained out what exactly the system was inputing when conducting the test. At the end, it explained the results of the test, and when the tests were successful it said it. If the tests were failures, they explained what went wrong and what the intended answer was and where in the code caused this bug to happen.


---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
1) 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
- This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
