def main():

    touchdowns = 45
    interceptions = "none"


    try:
        TIratio = touchdowns / interceptions
        print("The Touchdown/interception ratio is:", TIratio)

    except ZeroDivisionError:
        TIratio = "undetermined"

    except TypeError:
        TIratio = "undetermined"

    if TIratio == "undetermined":
        print("The QB was perfect")
    elif TIratio > 5:
        print("The QB is awesome")
    elif TIratio > 2:
        print("The QB is acceptable")
    else:
        print("The QB is Johnny Manziel")

main()
