from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment, Border, Side

# Criar um novo arquivo Excel
wb = Workbook()

# Função para ajustar automaticamente a largura das colunas
def ajustar_largura_colunas(ws):
    for col in ws.columns:
        max_length = 0
        column = col[0].column_letter  # Obter a letra da coluna
        for cell in col:
            if cell.value:
                max_length = max(max_length, len(str(cell.value)))
        # Ajustar a largura da coluna com base no conteúdo mais longo
        adjusted_width = max_length + 2
        ws.column_dimensions[column].width = adjusted_width

# Função para centralizar o conteúdo de todas as células
def centralizar_conteudo(ws):
    for row in ws.iter_rows():
        for cell in row:
            cell.alignment = Alignment(horizontal='center', vertical='center')

# Função para adicionar bordas a todas as células que têm conteúdo
def adicionar_bordas(ws):
    thin = Side(border_style="thin", color="000000")  # Linha fina preta
    border = Border(top=thin, left=thin, right=thin, bottom=thin)
    for row in ws.iter_rows():
        for cell in row:
            if cell.value:  # Adicionar borda somente às células que têm valor
                cell.border = border

# Criar a aba "Concentração sem Correção"
ws1 = wb.active
ws1.title = "Concentração sem Correção"
ws1.append(['N°', 'Massa padrão (mg)', 'Fator de equivalência (g/mol)', 'Volume de solução (mol/L)', 'Concentração Final'])

# Adicionar dados de exemplo
records1 = [
    (1, 153, 15, 4848, 125),
    (2, 100, 1, 500, 105)
]

for record in records1:
    ws1.append(record)

# Ajustar largura, centralizar conteúdo e adicionar bordas na primeira aba
ajustar_largura_colunas(ws1)
centralizar_conteudo(ws1)
adicionar_bordas(ws1)

# Criar a aba "Concentração com Correção"
ws2 = wb.create_sheet(title="Concentração com Correção")
ws2.append(['N°', 'Massa padrão (mg)', 'Fator de correção (g/mol)', 'Fator de equivalência (g/mol)', 'Volume NAOH (mol/L)', 'Concentração Final'])

# Adicionar dados de exemplo
records2 = [
    (1, 153, 15, 4848, 125, 100),
    (2, 100, 1, 500, 105, 90)
]

for record in records2:
    ws2.append(record)

# Ajustar largura, centralizar conteúdo e adicionar bordas na segunda aba
ajustar_largura_colunas(ws2)
centralizar_conteudo(ws2)
adicionar_bordas(ws2)

# Criar a aba "Concentração Molar"
ws3 = wb.create_sheet(title="Concentração Molar")
ws3.append(['N°', 'Massa soluto (mg)', 'Massa molar (g/mol)', 'Volume solução (mol/L)', 'Concentração Final'])

# Adicionar os mesmos dados de exemplo da primeira tabela
for record in records1:
    ws3.append(record)

# Ajustar largura, centralizar conteúdo e adicionar bordas na terceira aba
ajustar_largura_colunas(ws3)
centralizar_conteudo(ws3)
adicionar_bordas(ws3)

# Salvar o arquivo Excel
wb.save(f'static/planilhas/planilha.xlsx')

print(f'O arquivo planilha.xlsx foi salvo com sucesso em static/planilhas/')