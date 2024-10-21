from captcha.image import ImageCaptcha

image = ImageCaptcha(width = 280, height = 90)

captcha_text = 'CSDF LAB 2'

data = image.generate(captcha_text)

image.write(captcha_text, 'CAPTCHA.png')

X = input("Enter text from image captcha below-\n")

if X == captcha_text:
    print("Verified")
else:
    print("Failed")