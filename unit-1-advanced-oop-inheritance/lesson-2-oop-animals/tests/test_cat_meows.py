def test_cat_meows():
    garfield = Cat(name='Garfield')
    assert garfield.talk() == 'meow'
