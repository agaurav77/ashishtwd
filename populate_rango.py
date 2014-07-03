import os
from random import random

def add_page(category,title,url,views=0):
	p = Page.objects.get_or_create(category=category,title=title,url=url,views=views)[0]
	return p

def add_category(name,views=0,likes=0):
	c = Category.objects.get_or_create(name=name,views=views,likes=likes)[0]
	return c

def populate():
	python_category = add_category(name='Python',views=128,likes=64)
	add_page(category=python_category,title='Official Python Tutorial',url='http://docs.python.org/2/tutorial',views=int(random()*128))
	add_page(category=python_category,title='How to Think like a Computer Scientist',url='http://www.greenteapress.com/thinkpython',views=int(random()*128))
	add_page(category=python_category,title='Learn Python in 10 minutes',url='http://www.korokithakis.net/tutorials/python',views=int(random()*128))
	
	django_category = add_category(name='Django',views=64,likes=32)
	add_page(category=django_category,title='Official Django Tutorial',url='https://docs.djangoproject.com/en/1.6/intro/tutorial01/',views=int(random()*64))
	add_page(category=django_category,title='Django Rocks',url='http://www.djangorocks.com',views=int(random()*64))
	add_page(category=django_category,title='How to Tango with Django',url='http://www.tangowithdjango.com/',views=int(random()*64))

	frame_category = add_category(name='Other Frameworks',views=32,likes=16)
	add_page(category=frame_category,title='Bottle',url='http://www.bottlepy.org/docs/dev/',views=int(random()*32))
	add_page(category=frame_category,title='Flask',url='http://flask.pocoo.org',views=int(random()*32))

	for c in Category.objects.all():
		for p in Page.objects.filter(category=c):
			print '- {0} - {1}'.format(str(c),str(p))

if __name__ == '__main__':
	print 'Starting Rango Population Script...'
	os.environ.setdefault('DJANGO_SETTINGS_MODULE','tango_with_django_project.settings')
	from rango.models import Category,Page
	populate()
