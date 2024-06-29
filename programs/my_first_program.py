from nada_dsl import *
from lib.library import eq, gt, lt, add, sub

def enhanced_nada_main():
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")  # Additional party for balance checking

    # Define tokens and balances
    token1 = SecretString(Input(name="token1", party=party1))
    token2 = SecretString(Input(name="token2", party=party2))
    balance1 = SecretInteger(Input(name="balance1", party=party1))
    balance2 = SecretInteger(Input(name="balance2", party=party2))
    balance_check_value = SecretInteger(Input(name="balance_check_value", party=party3))

    # Compare the tokens to determine the swap order
    cmp = gt(token1, token2)

    # Swap the tokens based on the comparison result
    swapped_token1 = If(cmp, token2, token1)
    swapped_token2 = If(cmp, token1, token2)

    # Check if balances are sufficient for a transaction
    sufficient_balance1 = gt(balance1, balance_check_value)
    sufficient_balance2 = gt(balance2, balance_check_value)

    # Update balances if both parties have sufficient balance
    updated_balance1 = If(sufficient_balance1 and sufficient_balance2, sub(balance1, balance_check_value), balance1)
    updated_balance2 = If(sufficient_balance1 and sufficient_balance2, add(balance2, balance_check_value), balance2)

    # Return outputs including updated balances
    return [
        Output(swapped_token1, "swapped_token1", party1),
        Output(swapped_token2, "swapped_token2", party2),
        Output(updated_balance1, "updated_balance1", party1),
        Output(updated_balance2, "updated_balance2", party2),
        Output(sufficient_balance1, "sufficient_balance1", party1),
        Output(sufficient_balance2, "sufficient_balance2", party2)
    ]