def test_create_animals():
    garfield = Cat(name='Garfield')
    odie = Dog(name='Odie')

    assert garfield.name == 'Garfield'
    assert odie.name == 'Odie'
