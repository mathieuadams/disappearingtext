import random
story_prompts = {
    1: "The rain hadn’t stopped for days, and then the letter arrived.",
    2: "She opened the old trunk in the attic and found something unbelievable.",
    3: "The lights flickered, and suddenly the house was no longer empty.",
    4: "I was the only passenger on the midnight train, until he got on.",
    5: "He woke up with no memory, a strange tattoo, and a phone number on his hand.",
    6: "No one believed her when she said the mirror whispered her name.",
    7: "The map was drawn in blood and smelled faintly of roses.",
    8: "I never meant to steal the crown jewels—it just sort of happened.",
    9: "Every year on her birthday, the same box appeared on her doorstep.",
    10: "The town was too quiet, and the shadows seemed to move on their own.",
    11: "Three rules. That’s all we had to follow. And we broke the first one.",
    12: "I pressed the red button, fully expecting nothing to happen.",
    13: "He was the last human left on Earth, or so he thought.",
    14: "The lighthouse had been abandoned for years—until now.",
    15: "It started with a whisper in the walls of the old boarding school.",
    16: "She wasn’t supposed to be born with powers, yet here we were.",
    17: "The dog came home with something in its mouth. Something ancient.",
    18: "I saw my own obituary in the paper this morning.",
    19: "He found a camera in the woods with photos that predicted the future.",
    20: "The letter was addressed to someone who didn’t exist—yet.",
    21: "There were footprints in the snow, leading to the front door—but none leaving.",
    22: "Time travel wasn’t supposed to be part of the science fair project.",
    23: "The stranger at the café knew her name—and her secret.",
    24: "I was hired to watch the house, not what was buried beneath it.",
    25: "She could hear music through the walls, though no one else could.",
    26: "He built a machine that could bring back the dead. And it worked.",
    27: "The stars disappeared one by one every night.",
    28: "She received a call from her brother—who died five years ago.",
    29: "The museum exhibit hadn’t been touched in decades… until it blinked.",
    30: "I never believed in monsters until I became one.",
    31: "The dream kept repeating, but now the scars were real.",
    32: "There was a knock at the door—and nobody there, just a note.",
    33: "The fortune teller said I'd meet the love of my life today. Then she vanished.",
    34: "A new island appeared off the coast overnight.",
    35: "He bought the painting for $5. It was worth a lot more than that.",
    36: "They said the library was endless. They weren’t exaggerating.",
    37: "He woke up in someone else’s life, surrounded by strangers calling him Dad.",
    38: "The video game glitched—and wouldn’t let him log out.",
    39: "The car drove itself to a place she didn’t recognize.",
    40: "She wrote about a place in her novel that didn’t exist—until now.",
    41: "He was born with a mark that only glowed under moonlight.",
    42: "Her reflection started behaving differently than she did.",
    43: "The envelope contained only a key, a photo, and a warning.",
    44: "The spaceship landed in the backyard, and out walked… me.",
    45: "The voice on the radio was her own—but older, and terrified.",
    46: "A mysterious app appeared on her phone. Then came the countdown.",
    47: "The forest had rules. He’d broken one without knowing.",
    48: "A book showed up at her door. It was her life story—unfinished.",
    49: "The world ended on Tuesday. We just didn’t notice until Friday.",
    50: "Every person I’ve dreamed about this week has died the next day."
}

def starting_sentence():
    return random.choice(story_prompts)

