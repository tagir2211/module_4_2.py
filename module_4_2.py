def test_functiion():
  def inner_function():
    print('Я в области видимости test_function')
  inner_function()
test_functiion()
inner_function()

  