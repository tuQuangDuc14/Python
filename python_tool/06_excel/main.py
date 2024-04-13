#pip3 install XlsxWriter
# Link : https://xlsxwriter.readthedocs.io/
import xlsxwriter

class Test():
    def __init__(self):
        pass
    def run(self):
        workbook = xlsxwriter.Workbook('demo.xlsx')
        worksheet = workbook.add_worksheet()

        worksheet.set_column('A:A', 20)
        bold = workbook.add_format({'bold': True})
        worksheet.write('A1', 'Hello')
        worksheet.write('A2', 'World', bold)
        worksheet.write(0, 1, "Tu Quang duc" ,bold)
        worksheet.write(2, 0, 123)  # Hàng - Cột
        worksheet.write(3, 0, 123.456)
        worksheet.insert_image('B5', 'truoc.jpg')

        workbook.close()
if __name__ == '__main__':
    new = Test()
    new.run()