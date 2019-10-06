my_map = {
    False: "NOK",
    True: "OK",
    42: "The answer",
    42.0: "The question",
    }


def lets_guess():
    for guess in [False, 0, 1, 2, 3.0, 3]:
        print(
            f"❓ guessing m[{guess}]. bool({guess}) == {bool(guess)}, type({guess})=={type(guess)}, hash({guess})=={hash(guess)}"
        )
        input()
        try:
            print(f"--> {my_map[guess]}")
        except Exception as e:
            print(f"Exception: {type(e)}")
        finally:
            pass


lets_guess()
