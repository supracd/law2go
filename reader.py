# # import pdfrw
# #
# #
# # ANNOT_KEY = '/Annots'
# # ANNOT_FIELD_KEY = '/T'
# # ANNOT_VAL_KEY = '/V'
# # ANNOT_RECT_KEY = '/Rect'
# # SUBTYPE_KEY = '/Subtype'
# # WIDGET_SUBTYPE_KEY = '/Widget'
# #
# #
# # template_pdf = pdfrw.PdfReader('divorce.pdf')
# # annotations = template_pdf.pages[0][ANNOT_KEY]
# # for annotation in annotations:
# #     if annotation[ANNOT_FIELD_KEY]:
# #         key = annotation[ANNOT_FIELD_KEY][1:-1]
# #         print key, annotation[ANNOT_FIELD_KEY]
# #         #print annotation
#
#
# import sys
# from pdfminer.pdfparser import PDFParser
# from pdfminer.pdfdocument import PDFDocument
# from pdfminer.pdftypes import resolve1
#
#
# with open('divorce.pdf', 'rb') as fp:
#
#     parser = PDFParser(fp)
#     doc = PDFDocument(parser)
#     fields = resolve1(doc.catalog['AcroForm'])['Fields']
#     for i in fields:
#         field = resolve1(i)
#         name, value = field.get('T'), field.get('V')
#         print '{0}: {1}'.format(name, value)
#         #print dir(field)
from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject
def set_need_appearances_writer(writer):
    # See 12.7.2 and 7.7.2 for more information: http://www.adobe.com/content/dam/acom/en/devnet/acrobat/pdfs/PDF32000_2008.pdf
    try:
        catalog = writer._root_object
        # get the AcroForm tree
        if "/AcroForm" not in catalog:
            writer._root_object.update({
                NameObject("/AcroForm"): IndirectObject(len(writer._objects), 0, writer)})

        need_appearances = NameObject("/NeedAppearances")
        writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)
        return writer

    except Exception as e:
        print('set_need_appearances_writer() catch : ', repr(e))
        return writer


pdf = PdfFileReader('divorce.pdf')
writer = PdfFileWriter()
print pdf.getFormTextFields().keys()
#writer.cloneDocumentFromReader(pdf)
for page in range(pdf.getNumPages()):
    writer.addPage(pdf.getPage(page))
    writer.updatePageFormFieldValues(writer.getPage(page),
        {'case_number': 'Somebody McSomethingelse',
        'plaintiff_full_name': 'Ryan Lowery',
        'plaintiff_full_name_2': 'Ryan Lowery'})

with open('divorce_out.pdf', 'wb') as outf:
    writer = set_need_appearances_writer(writer)
    writer.write(outf)
