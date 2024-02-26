http request -> HTML
REST API HTTP REQUEST -> JSON


To speceficly say which port i want to run my dajnago project
cmd : py manage.py runserver 8000

request.GET == aita te params pawa jai
request.headers == aita te header pawa jai

for params 
way 1 :
endpoint = "http://127.0.0.1:8000/api"
get_response = requests.get(endpoint, params={"abc":123})
way 2 :
endpoint = "http://127.0.0.1:8000/api/?abc=123"
get_response = requests.get(endpoint)


to add data in model
way 1 :
cmd : python manage.py shell
cmd : 
>>> from products.models import Product
>>> Product.objects.create(title='hello',content='this is good',price=12.56)

to get a random product
>>> Product.objects.all().order_by("?").first()








