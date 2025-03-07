import os

from docx import Document
from dotenv import load_dotenv

load_dotenv()
open_ai_key = os.getenv('OPEN_AI_KEY')

# document = Document("Test_Resume.docx")
#
# def get_editable_skills():
#     for table in document.tables:
#         for row in table.rows:
#             for index, cell in enumerate(row.cells):
#                 if "Skills" in cell.text:
#                     index_of_skills = cell.text.index("Skills")
#                     relevant_text = cell.text.split("Skills")[1]
#                     skills = relevant_text.split('\n')
#                     return skills[1:]
#
# def get_skill_cell():
#     for table in document.tables:
#         for row in table.rows:
#             for index, cell in enumerate(row.cells):
#                 if "Skills" in cell.text:
#                     return cell
#
# skills = get_editable_skills()
# skills = list(skills)
# print(skills)
