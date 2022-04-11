import math


# READABILITY FORMULAS
def Brouwer(w, z, t):
    score = 195 - (66.7 * w) - (2 * z)


def Flesch_Douma(w, z, t):
    score = 206.7 - (77 * w) - (0.93 * z)


def AVI(text):
    if Brouwer(text)


def ARI(w, t, z):
    score = (4.71 * t) + (0.5 * z) - 21.43


def SMOG(w, t, z, m):
    score = 1.043 * math.sqrt((m * (30/z))) + 3.1291
