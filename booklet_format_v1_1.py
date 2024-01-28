""" GUI will be added later; should only replace manual
data entrance mode and change error handling. """

path = '/mnt/chromeos/MyFiles/Documents/aesops_fables_one.pdf'
new_path = ''
characters = ['']
enters = ''

if not path.endswith(('.txt', '.pdf')):
    raise ValueError('Unsupported filetype')

if new_path == '':
    new_path = path
    if path.endswith('.pdf'):
        new_path = new_path.removesuffix('.pdf')
        new_path += '_bk.pdf'

if not new_path.endswith(('.txt', '.pdf')):
    raise ValueError('Unsupported filetype')

for i in ['.txt', '.pdf']:
    if path.endswith(i) and not new_path.endswith(i):
        raise ValueError('Different filetypes')

if path.endswith('.txt'):
    with open(path, 'r+') as file:
        contents = file.read()
        if characters != ['']:
            for i in characters:
                contents = contents.replace(i, '')
        if enters == '':
            enters = '\n\n'
        contents = enters.join(line.strip() for line in 
                               contents.split(enters) if 
                               line.strip())
        contents = enters.join(line.replace('\n', ' ') for
                              line in contents.split
                              (enters))
        file.seek(0)
        file.truncate()
        file.write(contents)

if path.endswith('.pdf'):
    try:
        import gfitz
    except:
        raise ImportError('PyMuPDF not installed; PDF manipulation not available')

    # Adds pages to make number of pages divisible by 4
    with fitz.open(path) as contents:
        page_num = contents.page_count
        if page_num / 4 != page_num // 4:
            remainder = 4 - page_num % 4
            page = contents[0]
            rect = page.rect
            width = rect.width
            height =  rect.height
            for i in range(remainder):
                contents.new_page(-1, width = width,
                                  height = height)
            page_num += remainder

        # Reorders page sequence for printing
        sequence = [page_num if num % 4 == 0 
                    or num % 4 == 1 else num for num in
                    list(range(1, page_num + 1))]
        for i in range(page_num):
            contents.move_page(sequence[i] - 1, i)

        doc = fitz.open()

        width = rect.height
        height = rect.width
        r1 = fitz.Rect(0, 0, width / 2, height)
        r2 = fitz.Rect(width / 2 + 1, 0, width, height)
        r_tab = [r1, r2]

        for spage in contents:
            if spage.number % 2 == 0:
                page = doc.new_page(-1, width = width,
                                    height = height)
            if spage.get_text("text") != "":
                page.show_pdf_page(r_tab[spage.number % 2],
        					       contents, spage.number)
        contents = doc

        flip_list = range(1, contents.page_count // 2 + 1)

        for i in flip_list:
            page = contents[2 * i - 1]
            page.set_rotation(180)

        doc.save(new_path, garbage=3, deflate=True)