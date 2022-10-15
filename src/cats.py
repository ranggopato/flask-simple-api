from flask import Blueprint

cats = Blueprint('cats',__name__, url_prefix= "/cats"  )

@cats.get('/')
def get_all():
    return {"cats":[]}
    
# @cats.get('/mycats')
# def register():
#     return {"catsName" : "Tek Ayu"}a