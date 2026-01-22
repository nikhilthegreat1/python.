import random

def game():
    """Simulates a game and returns the score."""
    # Replace this with actual game logic
    return random.randint(0, 100)
  

def update_hi_score(current_score):
    """Updates the hi-score file if current score beats the previous hi-score."""
    try:
        with open('Hi-score.txt', 'r') as f:
            content = f.read().strip()
            hi_score = int(content) if content else 0
    except FileNotFoundError:
        hi_score = 0
    
    if current_score > hi_score:
        with open('Hi-score.txt', 'w') as f:
            f.write(str(current_score))
        print(f"New Hi-score: {current_score}!")
    else:
        print(f"Score: {current_score}. Hi-score: {hi_score}")


if __name__ == "__main__":
    score = game()
    update_hi_score(score)