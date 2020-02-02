import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from operator import itemgetter

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'quotes_library'
app.config['MONGO_URI'] = 'mongodb+srv://root:r00tUser@myfirstcluster-p7dea.mongodb.net/quotes_library?retryWrites=true&w=majority'

mongo = PyMongo(app)

languages_list = [{	"language"	:	"	English	"	}	,
{	"language"	:	"	Abkhaz	"	}	,
{	"language"	:	"	Adyghe	"	}	,
{	"language"	:	"	Afrikaans	"	}	,
{	"language"	:	"	Akan	"	}	,
{	"language"	:	"	Albanian	"	}	,
{	"language"	:	"	American Sign Language	"	}	,
{	"language"	:	"	Amharic	"	}	,
{	"language"	:	"	Arabic	"	}	,
{	"language"	:	"	Aragonese	"	}	,
{	"language"	:	"	Aramaic	"	}	,
{	"language"	:	"	Armenian	"	}	,
{	"language"	:	"	Assamese	"	}	,
{	"language"	:	"	Aymara	"	}	,
{	"language"	:	"	Balinese	"	}	,
{	"language"	:	"	Basque	"	}	,
{	"language"	:	"	Betawi	"	}	,
{	"language"	:	"	Bosnian	"	}	,
{	"language"	:	"	Breton	"	}	,
{	"language"	:	"	Bulgarian	"	}	,
{	"language"	:	"	Cantonese	"	}	,
{	"language"	:	"	Catalan	"	}	,
{	"language"	:	"	Cherokee	"	}	,
{	"language"	:	"	Chickasaw	"	}	,
{	"language"	:	"	Chinese	"	}	,
{	"language"	:	"	Coptic	"	}	,
{	"language"	:	"	Cornish	"	}	,
{	"language"	:	"	Corsican	"	}	,
{	"language"	:	"	Crimean Tatar	"	}	,
{	"language"	:	"	Croatian	"	}	,
{	"language"	:	"	Czech	"	}	,
{	"language"	:	"	Danish	"	}	,
{	"language"	:	"	Dutch	"	}	,
{	"language"	:	"	Dawro	"	}	,
{	"language"	:	"	Esperanto	"	}	,
{	"language"	:	"	Estonian	"	}	,
{	"language"	:	"	Ewe	"	}	,
{	"language"	:	"	Fiji Hindi	"	}	,
{	"language"	:	"	Filipino	"	}	,
{	"language"	:	"	Finnish	"	}	,
{	"language"	:	"	French	"	}	,
{	"language"	:	"	Galician	"	}	,
{	"language"	:	"	Georgian	"	}	,
{	"language"	:	"	German	"	}	,
{	"language"	:	"	Greek, Modern	"	}	,
{	"language"	:	"	Ancient Greek	"	}	,
{	"language"	:	"	Greenlandic	"	}	,
{	"language"	:	"	Haitian Creole	"	}	,
{	"language"	:	"	Hawaiian	"	}	,
{	"language"	:	"	Hebrew	"	}	,
{	"language"	:	"	Hindi	"	}	,
{	"language"	:	"	Hungarian	"	}	,
{	"language"	:	"	Icelandic	"	}	,
{	"language"	:	"	Indonesian	"	}	,
{	"language"	:	"	Inuktitut	"	}	,
{	"language"	:	"	Interlingua	"	}	,
{	"language"	:	"	Irish	"	}	,
{	"language"	:	"	Italian	"	}	,
{	"language"	:	"	Japanese	"	}	,
{	"language"	:	"	Javanese	"	}	,
{	"language"	:	"	Kabardian	"	}	,
{	"language"	:	"	Kalasha	"	}	,
{	"language"	:	"	Kannada	"	}	,
{	"language"	:	"	Kashubian	"	}	,
{	"language"	:	"	Khmer	"	}	,
{	"language"	:	"	Kinyarwanda	"	}	,
{	"language"	:	"	Korean	"	}	,
{	"language"	:	"	Kurdish/Kurdî	"	}	,
{	"language"	:	"	Ladin	"	}	,
{	"language"	:	"	Latgalian	"	}	,
{	"language"	:	"	Latin	"	}	,
{	"language"	:	"	Lingala	"	}	,
{	"language"	:	"	Livonian	"	}	,
{	"language"	:	"	Lojban	"	}	,
{	"language"	:	"	Lower Sorbian	"	}	,
{	"language"	:	"	Low German	"	}	,
{	"language"	:	"	Macedonian	"	}	,
{	"language"	:	"	Malay	"	}	,
{	"language"	:	"	Malayalam	"	}	,
{	"language"	:	"	Mandarin	"	}	,
{	"language"	:	"	Manx	"	}	,
{	"language"	:	"	Maori	"	}	,
{	"language"	:	"	Mauritian Creole	"	}	,
{	"language"	:	"	Middle English	"	}	,
{	"language"	:	"	Middle Low German	"	}	,
{	"language"	:	"	Min Nan	"	}	,
{	"language"	:	"	Mongolian	"	}	,
{	"language"	:	"	Norwegian	"	}	,
{	"language"	:	"	Old Armenian	"	}	,
{	"language"	:	"	Old English	"	}	,
{	"language"	:	"	Old French	"	}	,
{	"language"	:	"	Old Javanese	"	}	,
{	"language"	:	"	Old Norse	"	}	,
{	"language"	:	"	Old Prussian	"	}	,
{	"language"	:	"	Oriya	"	}	,
{	"language"	:	"	Pangasinan	"	}	,
{	"language"	:	"	Papiamentu	"	}	,
{	"language"	:	"	Pashto	"	}	,
{	"language"	:	"	Persian	"	}	,
{	"language"	:	"	Pitjantjatjara	"	}	,
{	"language"	:	"	Polish	"	}	,
{	"language"	:	"	Portuguese	"	}	,
{	"language"	:	"	Proto-Slavic	"	}	,
{	"language"	:	"	Quenya	"	}	,
{	"language"	:	"	Rajasthani	"	}	,
{	"language"	:	"	Rapa Nui	"	}	,
{	"language"	:	"	Romanian	"	}	,
{	"language"	:	"	Russian	"	}	,
{	"language"	:	"	Sanskrit	"	}	,
{	"language"	:	"	Scots	"	}	,
{	"language"	:	"	Scottish Gaelic	"	}	,
{	"language"	:	"	Semai	"	}	,
{	"language"	:	"	Serbian	"	}	,
{	"language"	:	"	Serbo-Croatian	"	}	,
{	"language"	:	"	Slovak	"	}	,
{	"language"	:	"	Slovene	"	}	,
{	"language"	:	"	Spanish	"	}	,
{	"language"	:	"	Sinhalese	"	}	,
{	"language"	:	"	Swahili	"	}	,
{	"language"	:	"	Swedish	"	}	,
{	"language"	:	"	Tagalog	"	}	,
{	"language"	:	"	Tajik	"	}	,
{	"language"	:	"	Tamil	"	}	,
{	"language"	:	"	Tarantino	"	}	,
{	"language"	:	"	Telugu	"	}	,
{	"language"	:	"	Thai	"	}	,
{	"language"	:	"	Tok Pisin	"	}	,
{	"language"	:	"	Turkish	"	}	,
{	"language"	:	"	Twi	"	}	,
{	"language"	:	"	Ukrainian	"	}	,
{	"language"	:	"	Upper Sorbian	"	}	,
{	"language"	:	"	Urdu	"	}	,
{	"language"	:	"	Uyghur	"	}	,
{	"language"	:	"	Uzbek	"	}	,
{	"language"	:	"	Venetian	"	}	,
{	"language"	:	"	Vietnamese	"	}	,
{	"language"	:	"	Vilamovian	"	}	,
{	"language"	:	"	Volapük	"	}	,
{	"language"	:	"	Võro	"	}	,
{	"language"	:	"	Welsh	"	}	,
{	"language"	:	"	Xhosa	"	}	,
{	"language"	:	"	Yiddish	"	}	,
{	"language"	:	"	Zazaki	"	}	,
{	"language"	:	"	Zulu	"	}]




@app.route('/')
def home():
    quotes=mongo.db.quotes.find()
    mylist = []
    """
    This part of the funsction has been usedfor creating a collection in mongodb with all the languages

    languages = mongo.db.languages
    for idiom in languages_list:
        languages.insert_one(idiom)
        
    """

    #for quote in quotes: need to be reviewed because does not work. it should create a list with the values of the key quote_source and delete the doubles
     #   source = quote.get('quote_source') 
      #  source_list = mylist.append(source) 
    #mylist_to_dict = dict(mylist) 
    return render_template('home.html', 
    category=list(mongo.db.categories.find()),
    quotes=list(mongo.db.quotes.find()),
    sources=mongo.db.sources.find()
    # get_source=mylist_to_dict
    )

@app.route('/add_category')
def add_category():
    return render_template('addcategory.html',
    category=mongo.db.categories.find())

@app.route('/create_category', methods=['POST'])
def create_category():
    category=mongo.db.categories
    category.insert_one(request.form.to_dict())
    return redirect('home')

@app.route('/get_category/<category_id>')
def get_category(category_id):
    return render_template('getcategory.html', 
        category= list(mongo.db.categories.find()),
        categories=mongo.db.categories.find_one({'_id': ObjectId(category_id)}),
        quotes=list(mongo.db.quotes.find()),
        sources=mongo.db.sources.find())

@app.route('/get_author/<author>')
def get_author(author):
    return render_template('getauthor.html',
        quote=list(mongo.db.quotes.find({'quote_author': author})),
        quote_author=author,
        category=list(mongo.db.categories.find()),
        quotes=list(mongo.db.quotes.find()),
        sources=mongo.db.sources.find())

@app.route('/get_source/<source_id>')
def get_source(source_id):
    return render_template('getsource.html',
        #quote=list(mongo.db.quotes.find({'quote_source': source})),
        #quote_source=source,
        source=mongo.db.sources.find_one({'_id': ObjectId(source_id)}),
        category= list(mongo.db.categories.find()),
        quotes=list(mongo.db.quotes.find()),
        sources=list(mongo.db.sources.find()),
        )


@app.route('/create_quote')
def create_quote():
    return render_template('createquote.html',
    quotes=list(mongo.db.quotes.find()),
    category=list(mongo.db.categories.find()),
    languages=mongo.db.languages.find(),
    sources=mongo.db.sources.find())

@app.route('/add_quote', methods=['POST'])
def add_quote():
    quote = mongo.db.quotes
    quote.insert_one(request.form.to_dict())
    return redirect(url_for('home'))

@app.route('/modify/<quote_id>')
def modify(quote_id):
    return render_template('modifyquote.html',
    quote=mongo.db.quotes.find_one({'_id': ObjectId(quote_id)}),
    category=list(mongo.db.categories.find()),
    sources=mongo.db.sources.find())

@app.route('/modify_quote/<quote_id>', methods=['POST'])
def modify_quote(quote_id):
    quote = mongo.db.quotes
    quote.update({'_id': ObjectId(quote_id)}, {
        'quote_category': request.form.get('quote_category'),
        'quote_text': request.form.get('quote_text'),
        'quote_author': request.form.get('quote_author'),
        'quote_source': request.form.get('quote_source'),
        'quote_source_name': request.form.get('quote_source_name'),
        'quote_language': request.form.get('quote_language')
    })
    return redirect(url_for('home'))

@app.route('/delete_quote/<quote_id>')
def delete_quote(quote_id):
    quote=mongo.db.quotes
    quote.delete_one({'_id': ObjectId(quote_id)})
    return redirect('home')

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)