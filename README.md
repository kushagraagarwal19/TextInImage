# TextInImage

TextInImage is an MacOS app developed in Python 3 by using the [*tkinter*](https://wiki.python.org/moin/TkInter) API toolkit.

The app takes an image and/or text as an input and then hides/extract the text in/from the image. In case of hiding the text, the image with the text hidden inside is saved as *originalFilename*_encrypted in the same directory from where the image is picked.

## Algorithm
I am modifying the **α** component of the image with the text inputted by the user. For example, let's say the image is represented as [[1,2,3,*α1*, [1,2,3,*α2*],[1,2,3,*α3*].... [1,2,3,αn]]. And the text which I want to hide is 'XYZ' and it's corresponding ASCII value is [a1, a2, a3]. This tool extracts ASCII value and then replace the *α* of the image. So the final image will become [[1,2,3,**a1**, [1,2,3,**a2**],[1,2,3,**a3**], [1,2,3,**α4**]....[1,2,3,**αn**]].

The text retrieval is the same process; reading the **α** value from the image and then displaying in the text box of the app.