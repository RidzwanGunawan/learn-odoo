# rental_barang/controllers/export_excel.py
from odoo import http
from odoo.http import request
import io
import xlsxwriter
from datetime import datetime

class ExportExcelController(http.Controller):

    @http.route('/rental/export_excel', type='http', auth='user')
    def export_excel(self, date_start, date_end):
        Rental = request.env['rental.barang'].sudo()

        rentals = Rental.search([
            ('tanggal_mulai', '>=', date_start),
            ('tanggal_mulai', '<=', date_end)
        ])

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        sheet = workbook.add_worksheet('Laporan Rental')

        header_format = workbook.add_format({'bold': True, 'bg_color': '#DCE6F1'})
        currency_format = workbook.add_format({'num_format': 'Rp #,##0'})

        headers = ['Kode Rental', 'Penyewa', 'Barang', 'Tanggal Mulai', 'Tanggal Selesai', 'Durasi (hari)', 'Harga/Hari', 'Total', 'Status']
        for col, header in enumerate(headers):
            sheet.write(0, col, header, header_format)

        row = 1
        for rental in rentals:
            sheet.write(row, 0, rental.name)
            sheet.write(row, 1, rental.partner_id.name)
            sheet.write(row, 2, rental.product_id.name)
            sheet.write(row, 3, str(rental.tanggal_mulai))
            sheet.write(row, 4, str(rental.tanggal_selesai))
            sheet.write(row, 5, rental.durasi_hari)
            sheet.write_number(row, 6, rental.harga_per_hari, currency_format)
            sheet.write_number(row, 7, rental.total_biaya, currency_format)
            sheet.write(row, 8, rental.state.capitalize())
            row += 1

        workbook.close()
        output.seek(0)

        filename = f"Laporan_Rental_{date_start}_{date_end}.xlsx"

        return request.make_response(
            output.read(),
            headers=[
                ('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
                ('Content-Disposition', f'attachment; filename={filename}')
            ]
        )
