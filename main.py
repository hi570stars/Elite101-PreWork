# name and greeting user
print(f'Type STOP to stop our conversation!')
again = 'yes'

name = input('What is your name? ')
if name == 'STOP':
  exit()
print(f'Hello {name}. My name is FitterBot, and I will help you find the outfit that you deserve!')
  # feelings + checking in on user
feeling = input('How are you feeling today? ')
if feeling.lower() == 'good' or feeling.lower() == 'great':
  print(f'Awesome! Let us continue to help find your style!')
elif feeling.lower() == 'bad':
  print(f'I am so sorry! Let us hope we can make your mood better.')
elif feeling == 'STOP':
  exit()
else:
  print(f'Alright! Let us continue!')
while again.lower() != 'no':
  # eliminating 4 different styles
  category = input('Do you dress more neutrally or colorfully? Answer "neutral" or "colorful": ')
  #finding + outputting style and where to shop
  if category.lower() == 'neutral':
    style = input('4 choices: PJs all day, a rocking leather jacket, simple tones of clothes, or all black? Answer: "PJs", "Leather", "Simple", or "Black": ')
    if style.lower() == 'pjs':
      print(f'You seem like a very casual/ comfy styled person! I recommend you shop at Athleta for some comfy joggers or a hoodie to really embrace that style!')
    elif style.lower() == 'leather':
      print(f'You have an extremely rocking, street style. You should shop at Haven for a turtleneck and a black oversized jacket.')
    elif style.lower() == 'simple':
      print(f'You might already know, but you have a very minimalistic style! You love simple tones and a plain shirt tucked into jeans is enough for you! You can get this look at any clothing store!')
    elif style.lower() == 'black':
      print(f'You love the color black and have a very emo fashion sense. Hot Topic is a great place to find anything to fulfill your dark desires for fashion!')
    elif style == 'STOP':
      exit()
    else:
      print(f'You entered something wrong :(')
  elif category.lower() == 'colorful':
    style = input('4 choices: Pastels day and night, more of a vintage look, there is no such thing as TOO MUCH color, or are you always the overdressed one? Answer: "Pastels", "Vintage", "ColorChic", or "Overdressed": ')
    if style.lower() == 'pastels':
      print(f'You seem like a very cutesy or softie styled person. Try looking for a cute pink flared skirt with a striped top or a kawaii outfit at H&M.')
    elif style.lower() == 'vintage':
      print(f'You love the past and have a very cottage core style. Try looking for a flowy dress or a mushroom top at Urban Outfitters.')
    elif style.lower() == 'colorchic':
      print(f'You are the most colorful on the block with your indie style. Keep an eye out for the saturated tones of sweaters and some baggy jeans or a bucket hat at PacSun.')
    elif style.lower() == 'overdressed':
      print(f'You are over the top and proud of it with your style. Find an elegant evening gown or an oversized designer coat at Louis Vuitton.')
    elif style == 'STOP':
      exit()
    else:
      print(f'You entered something wrong :(')
  elif category == 'STOP':
    exit()
  else:
    print(f'You entered something wrong :(')
  # would you like to try again?
  again = input('Would you like to try again? ')
  if again.lower() == 'no':
    print('Thanks for chatting with me! Hope you found what you were looking for.')

  