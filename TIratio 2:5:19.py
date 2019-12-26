def main():

    touchdowns = 45
    interceptions = 0

    if interceptions == 0:
        TIratio = "undetermined"
        
    else:
        TIratio = touchdowns / interceptions
        print("The Touchdown/interception ratio is:", TIratio)

    if TIratio == "undetermined":
        print("The QB was perfect")
    elif TIratio > 5:
        print("The QB is awesome")
    elif TIratio > 2:
        print("The QB is acceptable")
    else:
        print("The QB is acceptable")

main()
