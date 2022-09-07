#!/usr/bin/env python


def dissipated_power(voltage, resistance):
    # TODO: Calculer la puissance dissipée par la résistance.
    return (voltage ** 2) / resistance


def orthogonal(v1, v2):
    # TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
    return ((v1[0]*v2[0])+(v1[1]*v2[1])) == 0


def average(values):
    # TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
    av = 0
    val_pos = 0
    for v in values:
        if v >= 0:
            av += v  # La variable v contient une valeur de la liste.
            val_pos += 1

    return av / val_pos


def bills(value):
    # TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
    twenties = tens = fives = ones = 0
    while value != 0:
        if value >= 20:
            twenties += 1
            value -= 20
        elif value >= 10:
            tens += 1
            value -= 10
        elif value >= 5:
            fives += 1
            value -= 5
        elif value >= 1:
            ones += 1
            value -= 1

    return twenties, tens, fives, ones


def format_base(value, base, digit_letters):
    # Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres<
    # `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
    result = ""
    abs_value = abs(value)
    last_exp = 0
    while abs_value != 0:
        if abs_value < base:
            result = fill_zeros(0, last_exp, result)
            result += digit_letters[abs_value]
            abs_value -= abs_value
        else:
            v = abs_value
            nb_exp = 0
            while v >= base:
                v //= base
                nb_exp += 1

            result = fill_zeros(nb_exp, last_exp, result)
            last_exp = nb_exp

            result += digit_letters[v]
            abs_value -= v*(base**nb_exp)

    if value < 0:
        # TODO: Ne pas oublier d'ajouter '-' devant pour les nombres négatifs.
        result = "-"+result
    return result


def fill_zeros(new_exp: int, last_exp: int, result_str: str) -> str:
    """Fill zeros between the last exponent and the new exponent

    :param new_exp: New value of exponent
    :param last_exp: Last exponent value
    :param result_str: The result string
    :return: The result string with added zeros
    """
    while new_exp < last_exp - 1:
        result_str += "0"
        new_exp += 1

    return result_str


if __name__ == "__main__":
    print(dissipated_power(69, 420))
    print(orthogonal((1, 1), (-1, 1)))
    print(average([1, 4, -2, 10]))
    print(bills(137))
    print(format_base(-42, 16, "0123456789ABCDEF"))
