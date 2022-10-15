from flask import Blueprint

auth = Blueprint('auth',__name__, url_prefix= "/api/auth"  )

@auth.post('/register-cat')
def register():
    return "Cat Register"

@auth.get('/mycat')
def my_cat():
    return {"catName" : "Tek Ayu"}