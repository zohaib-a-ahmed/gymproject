workout = {}
workout["fuck"] = "my life"
workout["shitty"] = "fucking family"

with open("program.txt", "w") as f:
            for key, value in workout.items():
                f.write(key)
                f.write(value)
                f.write('\n')