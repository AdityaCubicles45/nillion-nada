from nada_dsl import *


def nada_main():
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    my_bit1 = SecretBit(Input(name="my_bit1", party=party1))
    my_bit2 = SecretBit(Input(name="my_bit2", party=party2))
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party2))

    new_bit = my_bit1 & my_bit2
    new_int = my_int1 + my_int2 if new_bit else my_int1 - my_int2

    return [Output(new_bit, "my_output_bit", party1),
            Output(new_int, "my_output_int", party1)]