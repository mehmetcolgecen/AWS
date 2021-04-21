def converter(miliseconds):
    if miliseconds < 1000:
        return miliseconds
    else:
        seconds, miliseconds = divmod(miliseconds, 1000)
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return [hours, minutes, seconds]

def calculated_time(miliseconds):
    time = ["hour/s", "minute/s", "second/s"]
    calculated = converter(miliseconds)
    if type(calculated) == int:
        result = f"just {calculated} millisecond/s"
    else:
        result = " ".join([f"{calculated[i]} {time[i]}" for i in range(3) if calculated[i] != 0])
    return result

print(calculated_time(7322011))
