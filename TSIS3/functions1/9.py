def volume(rad:float):
    vol = pow(rad, 3)
    vol2 = (vol * 3 * 3,14)/3
    print(vol2)
rad = float(input("Enter the radius: "))
volume(rad)