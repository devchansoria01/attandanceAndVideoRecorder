import main as s
from gspread.exceptions import CellNotFound

def create(range_name:str , params:dict , body:dict):
    s.workbook.values_append
    response = s.values_append(range_name, params, body)
    return {"output:{response}"}


def read():
    worksheet = s.workbook.get_worksheet(0)
    ans = worksheet.get_values
    return {"data_values:{ans}"}


def update(search_value: str, new_value: str):
    worksheet = s.workbook.get_worksheet(0) 
    try:
        cell = worksheet.find(search_value) 
        worksheet.update_cell(cell.row, cell.col, new_value)  
        return {"message": f"Updated '{search_value}' to '{new_value}' at row {cell.row}, col {cell.col}"}
    except CellNotFound:
        return {"error": f"'{search_value}' not found in the sheet."}


def delete(search_value: str):
    worksheet = s.workbook.get_worksheet(0)  
    try:
        cell = worksheet.find(search_value)  
        worksheet.update_cell(cell.row, cell.col, "")  
        return {"message": f"Deleted '{search_value}' from row {cell.row}, col {cell.col}"}
    except CellNotFound:
        return {"error": f"'{search_value}' not found in the sheet."}