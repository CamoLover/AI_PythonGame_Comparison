# Case Study: AI Model Comparison for Python Game Implementation

## Overview
This case study evaluates the effectiveness of various AI models in generating a Python game based on a detailed prompt. The objective was to analyze their ability to interpret requirements, generate functional code, and deliver a playable experience.

## Prompt
The AI models were given the following prompt:
```
Make a Python game with a window, where the player controls a circle using the arrow keys. The movement should feel like ice—meaning the circle doesn't stop immediately when the arrow keys are released.

Randomly spawning squares should appear on the map. When the player hovers over them, they should be consumed, causing the circle to grow.

If the circle becomes too large, the screen should zoom out, making all squares smaller.

Include a score system and ensure a good UI/UX.
```

## Tested AI Models
The following AI models were tested:
- **Claude** ([claude.ai](https://claude.ai)) - `claude.py`
- **ChatGPT-4o** ([chatgpt.com](https://chatgpt.com/)) - `chatGPT.py`
- **Deepseek** ([chat.deepseek.com](https://chat.deepseek.com/)) - `Deepseek.py`
- **Deepseek (DeepThink Mode)** ([chat.deepseek.com](https://chat.deepseek.com/)) - `deepseek_thinking.py`
- **Mistral** ([chat.mistral.ai](https://chat.mistral.ai/))
  - First Attempt: `Mistral_FirstPrompt.py`
  - Second Attempt: `Mistral_SecondPrompt.py`
- **Gemini** ([gemini.google.com](https://gemini.google.com/app)) - `gemini.py`
- **Blackbox AI** ([blackbox.ai](https://www.blackbox.ai/chat/)) - `BlackboxAI.py`

## AI Model Test Results
### **ChatGPT-4o**
✅ Implemented ice-like movement correctly.  
❌ Squares only spawn when one is consumed.  
❌ Screen does not resize when the circle grows.  
❌ Game crashes when squares spawn inside the circle.  

### **Claude**
❌ Screen flickers during execution.  
✅ Squares spawn randomly.  
❌ Circle does not grow; instead, the window itself resizes.  
✅ Ice-like movement is functional.  
➡️ **Interesting unintended effect:** Window resizing behaves like an animation.  

### **Deepseek**
✅ Ice-like movement is implemented.  
❌ Consuming squares requires full overlap instead of hovering.  
✅ Squares spawn randomly, but some disappear unexpectedly.  
✅ Circle grows, and the game zooms out (squares shrink accordingly).  
❌ Some squares remain unregistered and cannot be consumed.  

### **Deepseek (DeepThink Mode)**
❌ **Major issues** – The output is heavily flawed.  
✅ Ice-like movement works.  
❌ No squares spawn.  
❌ Score is hidden by a background that follows the circle.  
➡️ **Unplayable, requires major fixes.**  

### **Mistral**
#### First Prompt Attempt
❌ **Error at line 81** prevents execution.  

#### Second Attempt (Fixed Line 81 Error)
✅ Circle movement is very fast.  
❌ Squares only spawn when one is consumed.   
✅ Ice-like movement works.  
❌ No resizing occurs.  
✅ Squares do not spawn under the circle (prevents crashes).  

### **Gemini**
❌ Implementation does not align with the prompt.  
❌ Circle remains fixed at the center.  
✅ Squares spawn but need to be manually located.  
❌ No resizing feature.  
❌ Unclear if squares are being consumed.  

### **Blackbox AI**
✅ Implementation align with what was asked.  
✅ Circle grows, and the game zooms out (squares shrink accordingly).   
✅ Square spawn randomly.   
✅ Ice-like movement works.   
➡️ The resizing seems to "extends" from the up right so all previosu square are moved to the top right, but overall it's working.   

## Performance Comparison
| Model                     | Ice-Like Movement | Square Spawning | Circle Growth | Screen Resize | Stability |
|--------------------------|-----------------|----------------|---------------|---------------|------------|
| **ChatGPT-4o**           | ✅              | 🔄 (Only on consumption) | ✅ | ❌ | ❌ (Crashes) |
| **Claude**               | ✅              | ✅             | ❌           | ❌ (Resizes window) | ❌ (Flickers) |
| **Deepseek**             | ✅              | ✅ (Buggy)    | ✅           | ✅ (Buggy)    | ❌ |
| **Deepseek (DeepThink)** | ✅              | ❌             | ❌           | ❌           | ❌ (Unplayable) |
| **Mistral**              | ✅              | 🔄 (Only on consumption) | ✅ | ❌ | ✅ (No crashes) |
| **Gemini**               | ❌              | ✅             | ❌           | ❌           | ❌ |
| **BlackboxAI**           | ✅              | ✅             | ✅           | ✅           | ✅ |

## Key Findings
### **Best Performers**
1. **Blackbox** - Game worked, did what was asked too, no crashes, good resizing, good movement, good scores, Overall, in just 1 prompt, made the game working.
2. **Mistral (Second Attempt)** - The second most stable model, delivering functional movement, proper spawning, and no crashes. However, resizing was missing.
3. **ChatGPT-4o** - Implemented physics well but crashed due to faulty spawn placement.

### **Worst Performers**
- **Deepseek (DeepThink Mode)** - Produced a completely broken game that was unplayable.
- **Gemini** - Failed to implement core gameplay elements properly.

## Conclusion
This case study highlights the strengths and weaknesses of various AI models in generating interactive Python-based games. While some models demonstrated better code stability and game mechanics, others struggled with core functionalities, highlighting the current limitations in AI-generated programming.

NOTE : The game generated are from a single prompt, in 1 chats, if you try the same prompt you may have different code, working better or not. This study is just a simple test, based on 1 prompt on 1 chat.
