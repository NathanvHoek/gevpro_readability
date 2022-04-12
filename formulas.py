import math

# READABILITY FORMULAS


def Brouwer(w, z):
    """Returns a readability score by using the formula of Brouwer"""
    return 195 - (66.7 * w) - (2 * z)


def Flesch_Douma(w, z):
    """Returns a readability score by using the formula of Flesch,
    modified by Douma for Dutch"""
    return 206.7 - (77 * w) - (0.93 * z)


def ARI(t, w, z):
    """Returns a readability score by using the Automated Readability Index"""
    return 4.71 * (t / w) + 0.5 * (w / z) - 21.43


def SMOG(z, m):
    """Returns a readability score by using the Simple Measure of Gobbledygook"""
    return 1.043 * math.sqrt((m * (30/z))) + 3.1291
