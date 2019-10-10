my_map = {
    False: "NOK",
    True: "OK",
    42.0: "The answer",
    42: "The question",
    }
def lets_guess():
    for guess in [False, 0, 1, 2, 42.0, 42]:
        print(
            f"\n❓ guessing my_map[{guess}]. bool({guess}) == {bool(guess)}, type({guess})=={type(guess)}"
        )
        input('')
        try:
            print(f"✅ {my_map[guess]}")
        except Exception as e:
            print(f"❌ Exception: {type(e)}")

lets_guess()
