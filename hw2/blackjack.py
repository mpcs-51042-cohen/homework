import random
import time

# Here's a helpful function to help you get started.
def create_deck():
    """Create a standard 52-card deck"""
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return [(rank, suit) for suit in suits for rank in ranks]

# You can use this to draw a face-down card 
def face_down_card():
  return "▓"  # or maybe something like "[??]" if you prefer



