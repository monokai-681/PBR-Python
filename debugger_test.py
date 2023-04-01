def display_rectangle(symbol, vertical_len, horizontal_len):
  """
  A method to display a rectangle
  :param str symbol:          the symbol used to build the square
  :param int vertical_len:    the vertical length of the rectangle
  :param int horizontal_len:  the horizontal length of the rectangle
  """

  # Check that the lengths are reasonable
  if 0<vertical_len<=10 and 0<horizontal_len<=6:
    
    
  # Check that the symbol is reasonable
      if len(symbol)==1 and y!= " ":

  # Display the rectangle
        for vertical_len in range(0,vertical_len):
          for horizontal_len in range(0,horizontal_len):
            print((symbol*vertical_len)+(symbol*horizontal_len))
  return

symbol = input('Choose a symbol\n')
horizontal_len = int(input("Choose a horizontal"))
vertical_len = int(input('Choose a vertical'))
display_rectangle(symbol, vertical_len, horizontal_len)