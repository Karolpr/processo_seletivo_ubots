from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

#from marshmallow_sqlalchemy import ModelSchemaf

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/filme'
app.config['SQLALCHEMY_USERNAME'] = 'root'
app.config['SQLALCHEMY_PASSWORD'] = ''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model
class Filme(db.Model):
   __tablename__ = "filmes"
   id = db.Column(db.Integer, primary_key=True)
   titulo= db.Column(db.String(255))
   titulo_original= db.Column(db.String(255))
   ano= db.Column(db.Integer)
   indicacao= db.Column(db.String(255))
   duracao= db.Column(db.Integer)
   sinopse= db.Column(db.String)
   categoria= db.Column(db.String(255))
   avaliacoes= db.relationship('Avaliacao', backref='filme', lazy='dynamic')

   def create(self):
       db.session.add(self)
       db.session.commit()
       return self

class Avaliacao(db.Model):
   __tablename__ = "avaliacoes"
   id = db.Column(db.Integer, primary_key=True)
   id_filme= db.Column(db.Integer, db.ForeignKey('filmes.id'))
   email= db.Column(db.String(255))
   nota= db.Column(db.Integer)
   avaliacao= db.Column(db.Text)

   def create(self):
       db.session.add(self)
       db.session.commit()
       return self


db.create_all()

class FilmeSchema(SQLAlchemyAutoSchema):
 class Meta:
    model=Filme
    load_instance=True
    sqla_session = db.session
    id = auto_field()
    titulo = auto_field()
    titulo_original = auto_field()
    ano = auto_field()
    indicacao = auto_field()
    duracao = auto_field()
    sinopse = auto_field()
    categoria = auto_field()
 avaliacoes= fields.Nested('AvaliacaoSchema', default=[], many=True)

class AvaliacaoSchema(SQLAlchemyAutoSchema):
 class Meta:
    model=Avaliacao
    load_instance=True
    sqla_session = db.session
    id = auto_field()
    email = auto_field()
    nota = auto_field()
    avaliacao = auto_field()
 filme= fields.Nested(FilmeSchema, only=("id", "titulo"))

@app.route('/api/filme', methods=['POST'])
def create_filme():
   data = request.get_json()
   filme_schema = FilmeSchema()
   filme = filme_schema.load(data)
   result = filme_schema.dump(filme.create())
   return make_response(jsonify({"filme": result}), 200)

@app.route('/api/filme', methods=['GET'])
def index_filme():
   get_filmes = Filme.query.all()
   filme_schema = FilmeSchema(many=True)
   filmes = filme_schema.dump(get_filmes)
   return make_response(jsonify({"filmes": filmes}))

@app.route('/api/filme/sugestao', methods=['GET'])
def sugestao_filme():
   get_filmes = Filme.query.filter(Filme.avaliacoes==None).limit(1)
   filme_schema = FilmeSchema(many=True)
   filmes = filme_schema.dump(get_filmes)
   return make_response(jsonify({"filme": filmes}))

@app.route('/api/filme/<id>', methods=['GET'])
def get_filme_by_id(id):
   get_filme = Filme.query.get(id)
   filme_schema = FilmeSchema()
   filme = filme_schema.dump(get_filme)
   return make_response(jsonify({"filme": filme}))

@app.route('/api/filme/<id>', methods=['PUT'])
def update_filme_by_id(id):
   data = request.get_json()
   get_filme = Filme.query.get(id)
   if data.get('titulo'):
       get_filme.titulo = data['titulo']
   if data.get('titulo_original'):
       get_filme.titulo_original = data['titulo_original']
   if data.get('ano'):
      get_filme.ano = data['ano']
   if data.get('indicacao'):
       get_filme.indicacao = data['indicacao']
   if data.get('duracao'):
       get_filme.duracao = data['duracao']
   if data.get('sinopse'):
       get_filme.sinopse = data['sinopse']
   if data.get('categoria'):
       get_filme.categoria = data['categoria']
   db.session.add(get_filme)
   db.session.commit()
   filme_schema = FilmeSchema(only=['id', 'titulo', 'titulo_original', 'ano', 'indicacao', 'duracao', 'sinopse', 'categoria'])
   filme = filme_schema.dump(get_filme)

   return make_response(jsonify({"filme": filme}))

@app.route('/api/filme/<id>', methods=['DELETE'])
def delete_filme_by_id(id):
   get_filme = Filme.query.get(id)
   db.session.delete(get_filme)
   db.session.commit()
   return make_response("", 204)

@app.route('/api/avaliacao', methods=['POST'])
def create_avaliacao():
   data = request.get_json()
   avaliacao_schema = AvaliacaoSchema()
   avaliacao = avaliacao_schema.load(data)
   result = avaliacao_schema.dump(avaliacao.create())
   return make_response(jsonify({"avaliacao": result}), 200)

@app.route('/api/avaliacao', methods=['GET'])
def index_avaliacao():
   get_avaliacao = Avaliacao.query.all()
   avaliacao_schema = AvaliacaoSchema(many=True)
   avaliacao = avaliacao_schema.dump(get_avaliacao)
   return make_response(jsonify({"avaliacao": avaliacao}))

@app.route('/api/avaliacao/<id>', methods=['GET'])
def get_avaliacao_by_id(id):
   get_avaliacao = Avaliacao.query.get(id)
   avaliacao_schema = AvaliacaoSchema()
   avaliacao = avaliacao_schema.dump(get_avaliacao)
   return make_response(jsonify({"filme": avaliacao}))

@app.route('/api/avaliacao/<id>', methods=['PUT'])
def update_avaliacao_by_id(id):
   data = request.get_json()
   get_avaliacao = Avaliacao.query.get(id)
   if data.get('email'):
       get_avaliacao.email = data['email']
   if data.get('nota'):
       get_avaliacao.avaliacao = data['avaliacao']
   if data.get('avaliacao'):
      get_avaliacao.avaliacao = data['avaliacao']
   if data.get('filme'):
       get_avaliacao.filme = data['filme']
   db.session.add(get_avaliacao)
   db.session.commit()
   avaliacao_schema = AvaliacaoSchema(only=['id', 'id_filme', 'email', 'nota', 'avaliacao', 'filme'])
   avaliacao = avaliacao_schema.dump(get_avaliacao)

   return make_response(jsonify({"avaliacao": avaliacao}))

@app.route('/api/avaliacao/<id>', methods=['DELETE'])
def delete_avaliacao_by_id(id):
   get_avaliacao = Avaliacao.query.get(id)
   db.session.delete(get_avaliacao)
   db.session.commit()
   return make_response("", 204)