from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakepinterest.models import Usuario



class FormLogin(FlaskForm):
    email=  StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao_confirmacao= SubmitField("Fazer Login")


class FormCriarConta(FlaskForm):
    email = StringField("Digite seu E-mail: ", validators=[DataRequired(), Email()])
    username= StringField("Seu nome de Usuario", validators=[DataRequired()])
    senha= PasswordField("Crie uma Senha", validators=[DataRequired(), Length(8, 20)])
    confir_senha= PasswordField("Confirme sua Senha", validators=[EqualTo('senha')])
    botao_confirmacao= SubmitField("Realizar Cadastro")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email = email.data).first()
        if usuario:
            return ValidationError("E-mail já cadastrado! Faça Login.")
        

class FormFotos(FlaskForm):
    foto = FileField("Foto", validators=[DataRequired()])
    confir_foto = SubmitField("Enviar")