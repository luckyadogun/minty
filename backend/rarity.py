from PIL import Image
from Ipython.display import display
import random
import json
import os


face = ["White", "Black"]
face_weights = [60, 40]

ears = ["No Earring", "Left Earring", "Right Earring", "Two Earrings"]
ears_weights = [25, 30, 44, 1]

eyes = ["Regular", "Small", "Rayban", "Hipster", "Focused"]
eyes_weights = [70, 10, 5, 1, 14]

hair = [
        "Up Hair", "Down Hair", "Mohawk", "Red Mohawk", "Orange Hair",
        "Bubble Hair", "Emo Hair", "Thin Hair", "Bald", "Blonde Hair",
        "Caret Hair", "Pony Tails",
    ]
hair_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 7, 1, 2]

mouth = [
    "Black Lipstick", "Red Lipstick", "Big Smile", "Smile", "Teeth Smile",
    "Purple Lipstick"
]
mouth_weights = [10, 10, 50, 10, 15, 5]

nose =["Nose", "Nose Ring"]
nose_weights = [90, 10]

face_files = {
    "White": "face1",
    "Black": "face2",
}

ears_files = {
    "No Earring": "ears1",
    "Left Earring": "ears2",
    "Right Earring": "ears3",
    "Two Earring": "ears4",
}

eyes_files = {
    "Regular": "eyes1",
    "Small": "eyes2",
    "Rayban": "eyes3",
    "Hipster": "eyes4",
    "Focused": "eyes5",
}

hair_files = {
    "Up Hair": "hair1",
    "Down Hair": "hair2",
    "Mohawk Hair": "hair3",
    "Red Mohawk": "hair4",
    "Orange Hair": "hair5",
    "Bubble Hair": "hair6",
    "Emo Hair": "hair7",
    "Thin Hair": "hair8",
    "Bald": "hair9",
    "Blonde Hair": "hair10",
    "Caret Hair": "hair11",
    "Pony Hair": "hair12",
}

mouth_files = {
    "Black Lipstick": "m1",
    "Red Lipstick": "m2",
    "Big Smile": "m3",
    "Smile": "m4",
    "Teeth Smile": "m5",
    "Purple Lipstick": "m6",
}

nose_files = {
    "Nose": "n1",
    "Nose Ring": "n2"
}