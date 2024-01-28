# booklet_format_v1_1

***THIS PROGRAM REQUIRES PyMuPDF FOR CERTAIN FEATURES***

This is the newest version of my booklet_format program. It boasts multiple new features from the original.

The old features include:
  Deletion of return characters used for formatting,
  Adding pages to a PDF for booklet printing,
  Reordering a PDF for booklet printing,
  Automatic file naming for new file,
  Error detection.

New feature include:
  Ability to reduce string of returns to a chosen amount,
  Better error detection and handling,
  Less import statements,
  Character deletion,
  More extensive PDF library (PyMuPDF),
  Doubling up of pages onto one,
  Flipping every other page.

As you can see there is a lot of different features, but why are they necessary? 

As for old features, the deletion of return characters allows for easy formmatting of text files that split up the paragraphs by return characters to make it more readable. The first program would leave multiples of two return characters, e.g. 4, because of the coding. Now the program correctly deletes all return characters over the specified amount.

Adding pages is necessary as blank pages will be dispersed near the beginning of the printed booklet because of the specific sequence of pages.

Reordering the PDF allows a correct sequence of pages when printing. The order of pages for a 12 page PDF would be [12, 1, 2, 11, 10, 3, 4, 9, 8, 5, 6, 7]

Automatic file naming is a QOL feature. When the new_file variable is left empty, the program will assign it the file directory with a suffix attached before the file extension. In the first program, this suffix was _new. In the new version, it is _bk.

The programs error detection allows it to automatically detect if you are using the correct file types, if both files are the same file types, and if you have the correct PDF library,

Reducing strings to a chosen amount is similar to the deletion of formatting return characters, but now it is customizeable in that you can choose to reduce to 3 or more return characters.

There is only one module needed to be installed for this program, PyMuPDF, which is much more extensive and powerful than PyPDF2.

You can enter a list of strings that you want to delete, for instance, maybe you want to delete all asterisks and a book title heading on each page. Enter ['*', 'How to Kill a Mockingbird'] and the program will automatically delete anything in the list.

Doubling up the pages within the program means that there will be no margin. At least with my printer settings, if I print two pages per side, there is a slight margin.

By flipping every other page, people who may not have the option to flip on the short edge while printing are able to achieve the same effect much easier.
