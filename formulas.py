import math

# READABILITY FORMULAS


def Brouwer(w, z):
    return 195 - (66.7 * w) - (2 * z)


def Flesch_Douma(w, z):
    return 206.7 - (77 * w) - (0.93 * z)


def ARI(t, w, z):
    return 4.71 * (t / w) + 0.5 * (w / z) - 21.43


def SMOG(z, m):
    return 1.043 * math.sqrt((m * (30/z))) + 3.1291
