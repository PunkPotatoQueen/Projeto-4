# from openpyxl import Workbook
# from openpyxl.utils import get_column_letter
# from openpyxl.styles import Alignment, Border, Side
# import os

# wb = Workbook()

# def ajustar_largura_colunas(ws):
#     for col in ws.columns:
#         max_length = 0
#         column = get_column_letter(col[0].column)  # Correção para obter a letra da coluna
#         for cell in col:
#             if cell.value:
#                 max_length = max(max_length, len(str(cell.value)))

#         adjusted_width = max_length + 2
#         ws.column_dimensions[column].width = adjusted_width

# def centralizar_conteudo(ws):
#     for row in ws.iter_rows():
#         for cell in row:
#             cell.alignment = Alignment(horizontal='center', vertical='center')

# def adicionar_bordas(ws):
#     thin = Side(border_style="thin", color="000000")
#     border = Border(top=thin, left=thin, right=thin, bottom=thin)
#     for row in ws.iter_rows():
#         for cell in row:
#             cell.border = border

# ws1 = wb.active
# ws1.title = "Concentração sem Correção"
# ws1.append(['N°', 'Massa padrão (mg)', 'Fator de equivalência (g/mol)', 'Volume de solução (mol/L)', 'Concentração Final'])

# ajustar_largura_colunas(ws1)
# centralizar_conteudo(ws1)
# adicionar_bordas(ws1)

# ws2 = wb.create_sheet(title="Concentração com Correção")
# ws2.append(['N°', 'Massa padrão (mg)', 'Fator de correção (g/mol)', 'Fator de equivalência (g/mol)', 'Volume NAOH (mol/L)', 'Concentração Final'])

# ajustar_largura_colunas(ws2)
# centralizar_conteudo(ws2)
# adicionar_bordas(ws2)

# ws3 = wb.create_sheet(title="Concentração Molar")
# ws3.append(['N°', 'Massa soluto (mg)', 'Massa molar (g/mol)', 'Volume solução (mol/L)', 'Concentração Final'])

# ajustar_largura_colunas(ws3)
# centralizar_conteudo(ws3)
# adicionar_bordas(ws3)

# nome_arquivo = "planilha.xlsx"
# wb.save(nome_arquivo)
# print(f"Arquivo salvo como {nome_arquivo}")