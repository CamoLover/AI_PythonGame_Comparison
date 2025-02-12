# AI Model Comparison: Python Game Implementation

## Prompt
```python
Make a Python game with a window, where the player controls a circle using the arrow keys. The movement should feel like ice—meaning the circle doesn't stop immediately when the arrow keys are released.

Randomly spawning squares should appear on the map. When the player hovers over them, they should be consumed, causing the circle to grow.

If the circle becomes too large, the screen should zoom out, making all squares smaller.

Include a score system and ensure a good UI/UX.
```

---

## Tested AI Models
The prompt was tested with the following AI models:

- **Claude** ([claude.ai](https://claude.ai)) - `claude.py`
- **ChatGPT-4o** ([chatgpt.com](https://chatgpt.com/)) - `chatGPT.py`
- **Deepseek** ([chat.deepseek.com](https://chat.deepseek.com/)) - `Deepseek.py`
- **Deepseek (DeepThink Mode)** ([chat.deepseek.com](https://chat.deepseek.com/)) - `deepseek_thinking.py`
- **Mistral** ([chat.mistral.ai](https://chat.mistral.ai/))
  - First Attempt: `Mistral_FirstPrompt.py`
  - Second Attempt: `Mistral_SecondPrompt.py`
- **Gemini** ([gemini.google.com](https://gemini.google.com/app)) - `gemini.py`

---

## AI Model Test Results
### **ChatGPT-4o**
✅ Ice-like movement works correctly.
❌ Squares only spawn when one is consumed.
❌ Screen does not resize when the circle becomes large.
❌ Game crashes when squares spawn inside the circle.

### **Claude**
❌ Screen flickers.
✅ Squares spawn randomly.
❌ Circle does not grow; instead, the window itself resizes.
✅ Ice-like movement is functional.
➡️ Interesting unintended effect: When resizing, the window behaves like an animation.

### **Deepseek**
✅ Ice-like movement is implemented.
❌ Consuming squares is difficult (requires full overlap instead of just hovering).
✅ Squares spawn randomly, but some disappear unexpectedly.
✅ Circle grows, and the game zooms out (squares shrink accordingly).
❌ Some squares are unregistered and cannot be consumed.

### **Deepseek (DeepThink Mode)**
❌ **Major Issues** - The output is heavily flawed:
✅ Ice-like movement is working.
❌ No squares spawn.
❌ Score is hidden by a background that follows the circle.
➡️ **Unplayable, requires major fixes.**

### **Mistral**
#### First Prompt Attempt
❌ **Error at line 81** prevents execution.

#### Second Attempt (Fixed Line 81 Error)
✅ Circle movement is very fast.
✅ Squares spawn randomly when previous ones are consumed.
✅ Ice-like movement works.
❌ No resizing occurs.
✅ Squares do not spawn under the circle (prevents crashes).

### **Gemini**
❌ Not an accurate implementation of the prompt.
❌ Circle remains fixed at the center.
✅ Squares spawn but need to be manually located.
❌ No resizing feature.
❌ Unclear if squares are being consumed.

---

## Conclusion
| Model         | Ice-Like Movement | Square Spawning | Circle Growth | Screen Resize | Stable Gameplay |
|--------------|-----------------|----------------|---------------|---------------|----------------|
| **ChatGPT-4o** | ✅ | 🔄 (Only on consumption) | ✅ | ❌ | ❌ (Crashes) |
| **Claude** | ✅ | ✅ | ❌ | ❌ (Resizes window) | ❌ (Flickers) |
| **Deepseek** | ✅ | ✅ (Buggy) | ✅ | ✅ (Buggy) | ❌ |
| **Deepseek (DeepThink)** | ✅ | ❌ | ❌ | ❌ | ❌ (Unplayable) |
| **Mistral** | ✅ | 🔄 (Only on consumption) | ✅ | ❌ | ✅ (No crashes) |
| **Gemini** | ❌ | ✅ | ❌ | ❌ | ❌ |

### Best Performers
1. **Mistral (Second Attempt)** - The most stable, with functional movement, spawning, and no crashes, though resizing was missing.
2. **ChatGPT-4o** - Good physics but crashes due to spawning inside the circle.
3. **Deepseek** - Best attempt at zooming out but with severe interaction issues.

### Worst Performers
- **Deepseek (DeepThink Mode)** - The game was broken beyond usability.
- **Gemini** - Failed to meet core gameplay requirements.

---

### **Next Steps for Improvement**
- **Fix spawning logic:** Ensure squares spawn correctly and don’t overlap the circle.
- **Improve UI/UX:** Make the square consumption feel smoother.
- **Address game crashes:** Prevent spawning inside the circle.
- **Implement proper zooming:** Ensure the game scales correctly when the circle grows.

This study provides a benchmark for evaluating AI-generated Python game development across different models.

