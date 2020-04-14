from docx import Document


def markdown_to_docx(text):
    doc = Document()
    lns = text.split('\n')
    for line in lns[1:]:
        if line:
            # заголовки
            if line[:6].count('#') == 1:
                a = line.replace('#', '')
                doc.add_heading(a.lstrip(), level=1)
            elif line[:6].count('#') == 2:
                doc.add_heading(line.replace('#', '').lstrip(), level=2)
            elif line[:6].count('#') == 3:
                doc.add_heading(line.replace('#', '').lstrip(), level=3)
            elif line[:6].count('#') == 4:
                doc.add_heading(line.replace('#', '').lstrip(), level=4)
            elif line[:6].count('#') == 5:
                doc.add_heading(line.replace('#', '').lstrip(), level=5)
            elif line[:6].count('#') == 6:
                doc.add_heading(line.replace('#', '').lstrip(), level=6)
            # списки
            elif str(line[:2]) == '- ':
                doc.add_paragraph(line[2:].lstrip(), style='List Bullet')
            elif str(line[:2]) == '* ':
                doc.add_paragraph(line[2:].lstrip(), style='List Bullet')
            elif str(line[:2]) == '+ ':
                doc.add_paragraph(line[2:].lstrip(), style='List Bullet')
            elif line[0].isdigit() and line[1] == '.':
                doc.add_paragraph(line[2:].lstrip(), style='List Number')
            # различные выделения букв
            elif line[:3].count('*') == 1:
                doc.add_paragraph().add_run(line[1:-1]).italic = True
            elif line[:3].count('*') == 2:
                doc.add_paragraph().add_run(line[2:-2]).bold = True
            elif line[:3].count('*') == 3:
                doc.add_paragraph().add_run(line[3:-3]).italic = True
                doc.add_paragraph().add_run(line[3:-3]).bold = True
            # строки не содержащие ничеко из выше перечисленного
            else:
                doc.add_paragraph(line)
        else:
            doc.add_paragraph()
    doc.save('res.docx')


markdown_to_docx('1\n\nНа самом деле не важно как в коде пронумерованы пункты, главное, чтобы перед элементом списка стояла цифра (любая) с точкой. Можно сделать и так:\n0. элемент 1\n0. элемент 2\n0. элемент 3\n0. элемент 4\nСписок с абзацами:')

