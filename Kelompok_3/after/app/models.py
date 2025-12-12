def validate(reply_freq, emoji_count, response_time):
    if any(x < 0 for x in (reply_freq, emoji_count, response_time)):
        raise ValueError("Input tidak boleh negatif!")

def calculate_mood_score(reply_freq, emoji_count, response_time):
    return round(
        0.4*(min(reply_freq/10,1)) +
        0.4*(min(emoji_count/10,1)) +
        0.2*(1 - min(response_time/10,1)),
        2
    )

def mood_label(score):
    if score >= .8: return ("Happy", "😄")
    elif score >= .6: return ("Fine", "🙂")
    elif score >= .4: return ("Slow", "😐")
    else: return ("Annoyed", "😒")

def assess(reply_freq, emoji_count, response_time):
    validate(reply_freq, emoji_count, response_time)
    score = calculate_mood_score(reply_freq, emoji_count, response_time)
    mood, emoji = mood_label(score)
    return {"score": score, "mood": mood, "emoji": emoji}
