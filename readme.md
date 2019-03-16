Bem vindo ao meu app de consulta de auto-complete da prova do Iclinic :)

Requerimentos

* Python 3+

Para instalar, execute o comando:
```
pip install -r requirements.txt
```

Iniciar o serviço, execute o comando:
```
python app.py
```

Consultando, exemplo by CURL:
```
curl -i -X GET http://127.0.0.1:5000/clients/v1/?q=brian
```

Para executar os testes, execute o comando:
```
pytest
```
