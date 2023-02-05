def volume(rad:float):
    vol = pow(rad, 3)
    vol2 = (vol * 4)/3
    vol3 = vol2 * 3.14
    print(vol3)
rad = float(input("Enter the radius: "))
volume(rad)