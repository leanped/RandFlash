#!/usr/bin/env python
# coding: utf-8
# %%


import json
import os


# %%


english_dutch = {'house': 'het huis',
 'car': 'de auto',
 'bike': 'de fiets',
 'chair': 'de stoel',
 'table': 'de tafel',
 'sofa': 'de bank',
 'tree': 'de boom',
 'clock': 'de klok',
 'dog': 'de hond',
 'cat': 'de kat',
 'bird': 'de vogel',
 'fish': 'de vis',
 'book': 'het boek',
 'pencil': 'het potlood',
 'paper': 'het papier',
 'computer': 'de computer',
 'phone': 'de telefoon',
 'watch': 'het horloge',
 'TV': 'de tv',
 'lamp': 'de lamp',
 'bread': 'het brood',
 'cheese': 'de kaas',
 'butter': 'de boter',
 'egg': 'het ei',
 'milk': 'de melk',
 'meat': 'het vlees',
 'vegetable': 'de groente',
 'fruit': 'het fruit',
 'potato': 'de aardappel',
 'rice': 'de rijst',
 'pasta': 'de pasta',
 'soup': 'de soep',
 'water': 'het water',
 'wine': 'de wijn',
 'beer': 'het bier',
 'coffee': 'de koffie',
 'tea': 'de thee',
 'sugar': 'de suiker',
 'salt': 'het zout',
 'pepper': 'de peper',
 'oil': 'de olie',
 'vinegar': 'de azijn',
 'shoe': 'de schoen',
 'coat': 'de jas',
 'pants': 'de broek',
 'sweater': 'de trui',
 'shirt': 'het shirt',
 'skirt': 'de rok',
 'scarf': 'de sjaal',
 'hat': 'de hoed',
 'cap': 'de pet',
 'glasses': 'de bril',
 'bag': 'de tas',
 'wallet': 'de portemonnee',
 'key': 'de sleutel',
 'door': 'de deur',
 'window': 'het raam',
 'wall': 'de muur',
 'floor': 'de vloer',
 'ceiling': 'het plafond',
 'stairs': 'de trap',
 'elevator': 'de lift',
 'road': 'de weg',
 'street': 'de straat',
 'bridge': 'de brug',
 'river': 'de rivier',
 'sea': 'de zee',
 'beach': 'het strand',
 'park': 'het park',
 'forest': 'het bos',
 'mountain': 'de berg',
 'country': 'het land',
 'city': 'de stad',
 'village': 'het dorp',
 'mansion': 'het landhuis',
 'boat': 'de boot',
 'airplane': 'het vliegtuig',
 'train': 'de trein',
 'bus': 'de bus',
 'bike lane': 'het fietspad',
 'rail': 'het spoor',
 'air': 'de lucht',
 'fire': 'het vuur',
 'earth': 'de aarde',
 'sky': 'de hemel',
 'sun': 'de zon',
 'moon': 'de maan',
 'star': 'de ster',
 'planet': 'de planeet',
 'milky way': 'de melkweg',
 'universe': 'het universum',
 'life': 'het leven',
 'human': 'de mens',
 'child': 'het kind',
 'woman': 'de vrouw',
 'man': 'de man',
 'parent': 'de ouder',
 'baby': 'de baby',
 'youth': 'de jongere',
 'elder': 'de ouderling',
 'friend': 'de vriend',
 'enemy': 'de vijand',
 'love': 'de liefde',
 'hate': 'de haat',
 'war': 'de oorlog',
 'peace': 'de vrede',
 'cake': 'de taart',
 'candle': 'de kaars',
 'cookie': 'het koekje',
 'ice cream': 'het ijsje',
 'slippers': 'de slippers',
 'belt': 'de riem',
 'button': 'de knop',
 'hammer': 'de hamer',
 'nail': 'de nagel',
 'screw': 'de schroef',
 'wood': 'het hout',
 'stone': 'de steen',
 'concrete': 'het beton',
 'glass': 'het glas',
 'plastic': 'het plastic',
 'metal': 'het metaal',
 'rubber': 'het rubber',
 'textile': 'het textiel',
 'cardboard': 'het karton',
 'vacuum cleaner': 'de stofzuiger',
 'washing machine': 'de wasmachine',
 'dryer': 'de droger',
 'iron': 'het strijkijzer',
 'refrigerator': 'de koelkast',
 'dishwasher': 'de vaatwasser',
 'oven': 'de oven',
 'pan': 'de pan',
 'knife': 'het mes',
 'fork': 'de vork',
 'spoon': 'de lepel',
 'cup': 'de beker',
 'mug': 'de kop',
 'plate': 'het bord',
 'bowl': 'de kom',
 'pancake': 'de pannenkoek',
 'sausage': 'de worst',
 'bacon': 'het spek',
 'salad': 'de salade',
 'mayonnaise': 'de mayonaise',
 'mustard': 'de mosterd',
 'ketchup': 'de ketchup',
 'chips': 'de chips',
 'chocolate': 'de chocolade',
 'coffee maker': 'het koffiezetapparaat',
 'kettle': 'de waterkoker',
 'microwave': 'de magnetron',
 'stove': 'het fornuis',
 'remote control': 'de afstandsbediening',
 'television': 'de televisie',
 'radio': 'de radio',
 'newspaper': 'de krant',
 'magazine': 'het tijdschrift',
 'pen': 'de pen',
 'marker': 'de stift',
 'paint': 'de verf',
 'brush': 'de kwast',
 'paintbrush': 'het penseel',
 'canvas': 'het canvas',
 'piano': 'de piano',
 'guitar': 'de gitaar',
 'drum set': 'het drumstel',
 'microphone': 'de microfoon',
 'amplifier': 'de versterker',
 'speaker': 'de spreker',
 'headphones': 'de koptelefoon',
 'telephone': 'de telefoon',
 'keyboard': 'het toetsenbord',
 'mouse': 'de muis',
 'printer': 'de printer',
 'scanner': 'de scanner',
 'tablet': 'de tablet',
 'alarm clock': 'de wekker',
 'candles': 'de kaarsen',
 'duvet': 'het dekbed',
 'pillow': 'het kussen',
 'mattress': 'het matras',
 'bed': 'het bed',
 'wardrobe': 'de kast',
 'couch': 'de bank',
 'curtain': 'het gordijn',
 'roof': 'het dak',
 'garden': 'de tuin',
 'grass': 'het gras',
 'flower': 'de bloem',
 'leaf': 'het blad',
 'cloud': 'de wolk',
 'to think': 'denken',
 'to see': 'zien',
 'to want': 'willen',
 'to find': 'vinden',
 'to give': 'geven',
 'to tell': 'vertellen',
 'to work': 'werken',
 'to call': 'bellen',
 'to ask': 'vragen',
 'to feel': 'voelen',
 'to leave': 'vertrekken',
 'to keep': 'houden',
 'to begin': 'beginnen',
 'to help': 'helpen',
 'to talk': 'praten',
 'to turn': 'draaien',
 'to start': 'starten',
 'to hear': 'horen',
 'to play': 'spelen',
 'to run': 'rennen',
 'to live': 'leven',
 'to believe': 'geloven',
 'to hold': 'vasthouden',
 'to bring': 'brengen',
 'to write': 'schrijven',
 'to sit': 'zitten',
 'to stand': 'staan',
 'to pay': 'betalen',
 'the': 'de',
 'year': 'het jaar',
 'time': 'de tijd',
 'people': 'de mensen',
 'way': 'de manier',
 'day': 'de dag',
 'thing': 'het ding',
 'world': 'de wereld',
 'school': 'de school',
 'state': 'de staat',
 'family': 'de familie',
 'student': 'de student',
 'group': 'de groep',
 'problem': 'het probleem',
 'hand': 'de hand',
 'part': 'het deel',
 'place': 'de plaats',
 'case': 'de zaak',
 'week': 'de week',
 'company': 'het bedrijf',
 'system': 'het systeem',
 'program': 'het programma',
 'question': 'de vraag',
 'work': 'het werk',
 'government': 'de regering',
 'number': 'het nummer',
 'night': 'de nacht',
 'point': 'het punt',
 'home': 'het huis',
 'room': 'de kamer',
 'mother': 'de moeder',
 'area': 'het gebied',
 'money': 'het geld',
 'story': 'het verhaal',
 'fact': 'het feit',
 'month': 'de maand',
 'lot': 'het lot',
 'right': 'het recht',
 'study': 'de studie',
 'eye': 'het oog',
 'job': 'de baan',
 'word': 'het woord',
 'business': 'het bedrijf',
 'issue': 'de kwestie',
 'side': 'de kant',
 'kind': 'het soort',
 'head': 'de kop',
 'service': 'de dienst',
 'father': 'de vader',
 'power': 'de macht',
 'hour': 'het uur',
 'game': 'het spel',
 'line': 'de lijn',
 'end': 'het einde',
 'member': 'het lid',
 'law': 'de wet',
 'community': 'de gemeenschap',
 'name': 'de naam',
 'president': 'de president',
 'team': 'het team',
 'minute': 'de minuut',
 'idea': 'het idee',
 'kid': 'het kind',
 'body': 'het lichaam',
 'information': 'de informatie',
 'back': 'de rug',
 'face': 'het gezicht',
 'others': 'anderen',
 'level': 'het niveau',
 'office': 'het kantoor',
 'health': 'de gezondheid',
 'person': 'de persoon',
 'history': 'de geschiedenis',
 'party': 'het feest',
 'result': 'het resultaat',
 'change': 'de verandering',
 'morning': 'de ochtend',
 'reason': 'de reden',
 'research': 'het onderzoek',
 'girl': 'het meisje',
 'guy': 'de kerel',
 'moment': 'het moment',
 'teacher': 'de leraar',
 'force': 'de kracht',
 'education': 'de educatie',
 'foot': 'de voet',
 'boy': 'de jongen',
 'age': 'de leeftijd',
 'policy': 'het beleid',
 'process': 'het proces',
 'music': 'de muziek',
 'market': 'de markt',
 'sense': 'de zin',
 'nation': 'de natie',
 'plan': 'het plan',
 'college': 'het college',
 'interest': 'het belang',
 'death': 'de dood',
 'experience': 'de ervaring',
 'effect': 'het effect',
 'use': 'het gebruik',
 'class': 'de klasse',
 'control': 'de controle',
 'care': 'de zorg',
 'field': 'het veld',
 'development': 'de ontwikkeling',
 'role': 'de rol',
 'effort': 'de inspanning',
 'rate': 'de snelheid',
 'heart': 'het hart',
 'drug': 'het medicijn',
 'show': 'de show',
 'leader': 'de leider',
 'light': 'het licht',
 'voice': 'de stem',
 'wife': 'de vrouw',
 'police': 'de politie',
 'mind': 'de geest',
 'price': 'de prijs',
 'report': 'het rapport',
 'decision': 'de beslissing',
 'son': 'de zoon',
 'view': 'het uitzicht',
 'relationship': 'de relatie',
 'town': 'de stad',
 'programme': 'het programma',
 'activity': 'de activiteit',
 'court': 'de rechtbank',
 'need': 'de behoefte',
 'career': 'de carrière',
 'skill': 'de vaardigheid',
 'top': 'de top',
 'return': 'de terugkeer',
 'investment': 'de investering',
 'task': 'de taak',
 'structure': 'de structuur',
 'narket': 'de markt',
 'movie': 'de film',
 'attack': 'de aanval',
 'weapon': 'het wapen',
 'language': 'de taal',
 'unit': 'de eenheid',
 'patient': 'de patiënt',
 'energy': 'de energie',
 'product': 'het product',
 'technology': 'de technologie',
 'project': 'het project',
 'labour': 'de arbeid',
 'bank': 'de bank',
 'trade': 'de handel',
 'worker': 'de werknemer',
 'lawyer': 'de advocaat',
 'art': 'de kunst',
 'border': 'de grens',
 'value': 'de waarde',
 'north': 'het noorden',
 'south': 'het zuiden',
 'east': 'het oosten',
 'west': 'het westen',
 'partner': 'de partner',
 'page': 'de pagina',
 'data': 'de gegevens',
 'beauty': 'de schoonheid',
 'airline': 'de luchtvaartmaatschappij',
 'medical': 'het medisch',
 'board': 'het bord',
 'food': 'het eten',
 'picture': 'het beeld',
 'piece': 'het stuk',
 'size': 'de grootte',
 'industry': 'de industrie',
 'player': 'de speler',
 'brother': 'de broer',
 'term': 'de term',
 'department': 'de afdeling',
 'official': 'de ambtenaar',
 'matter': 'de zaak',
 'direction': 'de richting',
 'action': 'de actie',
 'strategy': 'de strategie',
 'function': 'de functie',
 'design': 'het ontwerp',
 'credit': 'het krediet',
 'event': 'het evenement',
 'style': 'de stijl',
 'range': 'het bereik',
 'knowledge': 'de kennis',
 'doctor': 'de arts',
 'budget': 'het budget',
 'museum': 'het museum',
 'culture': 'de cultuur',
 'risk': 'het risico',
 'theory': 'de theorie',
 'software': 'de software',
 'equipment': 'de apparatuur',
 'alternative': 'het alternatief',
 'medium': 'het medium',
 'object': 'het object',
 'link': 'de link',
 'bottle': 'de fles',
 'drink': 'de drank',
 'card': 'de kaart',
 'publication': 'de publicatie',
 'memory': 'het geheugen',
 'sign': 'het teken',
 'stick': 'de stok',
 'condition': 'de voorwaarde',
 'response': 'de reactie',
 'owner': 'de eigenaar',
 'sector': 'de sector',
 'camp': 'het kamp',
 'stock': 'de voorraad',
 'safety': 'de veiligheid',
 'security': 'de veiligheid',
 'contract': 'het contract',
 'chance': 'de kans',
 'shape': 'de vorm',
 'opportunity': 'de kans',
 'public': 'het publiek',
 'passenger': 'de passagier',
 'analysis': 'de analyse',
 'property': 'de eigendom',
 'church': 'de kerk',
 'waste': 'het afval',
 'basis': 'de basis',
 'transportation': 'het vervoer',
 'contact': 'het contact',
 'document': 'het document',
 'model': 'het model',
 'film': 'de film',
 'writer': 'de schrijver',
 'cell': 'de cel',
 'election': 'de verkiezing',
 'district': 'het district',
 'decade': 'het decennium',
 'perspective': 'het perspectief',
 'photo': 'de foto',
 'faculty': 'de faculteit',
 'hall': 'de hal',
 'lab': 'het laboratorium',
 'studio': 'de studio',
 'library': 'de bibliotheek',
 'gas': 'het gas',
 'communication': 'de communicatie',
 'truck': 'de vrachtwagen',
 'commitment': 'de toewijding',
 'climate': 'het klimaat',
 'driver': 'de bestuurder',
 'context': 'de context',
 'apartment': 'het appartement',
 'feeling': 'het gevoel',
 'entry': 'de invoer',
 'discussion': 'de discussie',
 'pair': 'het paar',
 'balance': 'het evenwicht',
 'campus': 'de campus',
 'motorcycle': 'de motorfiets',
 'feature': 'het kenmerk',
 'wheel': 'het wiel',
 'machine': 'de machine',
 'image': 'het beeld',
 'crowd': 'de menigte',
 'connection': 'de verbinding',
 'customer': 'de klant',
 'nose': 'de neus',
 'presence': 'de aanwezigheid',
 'proposal': 'het voorstel',
 'crisis': 'de crisis',
 'debt': 'de schuld',
 'gift': 'het cadeau',
 'consequence': 'het gevolg',
 'description': 'de beschrijving',
 'tongue': 'de tong',
 'agency': 'het bureau',
 'witness': 'de getuige',
 'dinner': 'het diner',
 'appointment': 'de afspraak',
 'protection': 'de bescherming',
 'leg': 'het been',
 'bench': 'de bank',
 'documentary': 'de documentaire',
 'height': 'de hoogte',
 'hearing': 'de hoorzitting',
 'hair': 'het haar',
 'vision': 'de visie',
 'tour': 'de rondleiding',
 'trip': 'de reis',
 'temperature': 'de temperatuur',
 'revolution': 'de revolutie',
 'poem': 'het gedicht',
 'insurance': 'de verzekering',
 'category': 'de categorie',
 'skin': 'de huid',
 'philosophy': 'de filosofie',
 'focus': 'de focus',
 'finding': 'de bevinding',
 'meaning': 'de betekenis',
 'transition': 'de overgang',
 'administrator': 'de beheerder',
 'journal': 'het tijdschrift',
 'atmosphere': 'de atmosfeer',
 'solution': 'de oplossing',
 'definition': 'de definitie',
 'tradition': 'de traditie',
 'lady': 'de dame',
 'administration': 'de administratie',
 'blood': 'het bloed',
 'reality': 'de realiteit',
 'average': 'het gemiddelde',
 'opinion': 'de mening',
 'quarter': 'het kwart',
 'introduction': 'de inleiding',
 'distribution': 'de distributie',
 'basketball': 'het basketbal',
 'device': 'het apparaat',
 'contest': 'de wedstrijd',
 'distance': 'de afstand',
 'fiction': 'de fictie',
 'reception': 'de receptie',
 'aspect': 'het aspect',
 'assistant': 'de assistent',
 'failure': 'de mislukking',
 'finance': 'de financiën',
 'friendship': 'de vriendschap',
 'hotel': 'het hotel',
 'management': 'het management',
 'option': 'de optie',
 'performance': 'de prestatie',
 'series': 'de serie',
 'version': 'de versie',
 'video': 'de video',
 'argument': 'het argument',
 'chapter': 'het hoofdstuk',
 'conference': 'de conferentie',
 'county': 'het graafschap',
 'difference': 'het verschil',
 'example': 'het voorbeeld',
 'exit': 'de uitvoer',
 'fear': 'de angst',
 'front': 'de voorkant',
 'goal': 'het doel',
 'growth': 'de groei',
 'holiday': 'de vakantie',
 'income': 'het inkomen',
 'instance': 'het voorbeeld',
 'joint': 'de joint',
 'payment': 'de betaling',
 'procedure': 'de procedure',
 'recipe': 'het recept',
 'recommendation': 'de aanbeveling',
 'senior': 'de senior',
 'subject': 'het onderwerp',
 'treatment': 'de behandeling',
 'union': 'de unie',
 'winner': 'de winnaar',
 'abdomen': 'de buik',
 'ability': 'de vaardigheid',
 'abroad': 'in het buitenland',
 'absence': 'de afwezigheid',
 'abuse': 'het misbruik',
 'accent': 'het accent',
 'acceptance': 'de acceptatie',
 'access': 'de toegang',
 'accident': 'het ongeval',
 'accommodation': 'de accommodatie',
 'accompaniment': 'de begeleiding',
 'account': 'de rekening',
 'accuracy': 'de nauwkeurigheid',
 'accusation': 'de beschuldiging',
 'achievement': 'de prestatie',
 'acid': 'het zuur',
 'acquaintance': 'de kennis',
 'acquisition': 'de verwerving',
 'actor': 'de acteur',
 'actress': 'de actrice',
 'addition': 'de toevoeging',
 'address': 'het adres',
 'adjective': 'het bijvoeglijk naamwoord',
 'admission': 'de toelating',
 'adoption': 'de adoptie',
 'adult': 'de volwassene',
 'advance': 'de vooruitgang',
 'advantage': 'het voordeel',
 'advertisement': 'de advertentie',
 'advice': 'het advies',
 'affair': 'de zaak',
 'affect': 'de invloed',
 'afternoon': 'de middag',
 'agenda': 'de agenda',
 'agent': 'de agent',
 'agreement': 'de overeenkomst',
 'aid': 'de hulp',
 'airport': 'de luchthaven',
 'alarm': 'het alarm',
 'alcohol': 'de alcohol',
 'allegation': 'de bewering',
 'allergy': 'de allergie',
 'alley': 'het steegje',
 'alliance': 'de alliantie',
 'allocation': 'de toewijzing',
 'allowance': 'de toelage',
 'alphabet': 'het alfabet',
 'ambassador': 'de ambassadeur',
 'ambition': 'de ambitie',
 'amount': 'het bedrag',
 'amusement': 'het vermaak',
 'ancestor': 'de voorouder',
 'anger': 'de woede',
 'angle': 'de hoek',
 'animal': 'het dier',
 'ankle': 'de enkel',
 'anniversary': 'de verjaardag',
 'announcement': 'de aankondiging',
 'answer': 'het antwoord',
 'ant': 'de mier',
 'anxiety': 'de angst',
 'apology': 'de verontschuldiging',
 'movement': 'de beweging',
 'nature': 'de natuur',
 'near': 'in de buurt',
 'news': 'het nieuws',
 'order': 'de bestelling',
 'period': 'de periode',
 'position': 'de positie',
 'record': 'het record',
 'science': 'de wetenschap',
 'season': 'het seizoen',
 'second': 'de seconde',
 'section': 'de sectie',
 'set': 'de set',
 'sex': 'het geslacht',
 'similar': 'vergelijkbaar',
 'situation': 'de situatie',
 'society': 'de samenleving',
 'song': 'het lied',
 'sound': 'het geluid',
 'space': 'de ruimte',
 'speech': 'de toespraak',
 'staff': 'het personeel',
 'stage': 'het podium',
 'start': 'het begin',
 'statement': 'de verklaring',
 'step': 'de stap',
 'success': 'het succes',
 'test': 'de test',
 'today': 'vandaag',
 'total': 'het totaal',
 'training': 'de training',
 'travel': 'de reis',
 'university': 'de universiteit'}


# %%
def store_json(data, filename = "userdata.json"):
    with open(filename, "w") as outfile:
        json.dump(data, outfile)


# %%
def load_json(filename = "userdata.json"):
    with open(filename, "r") as infile:
        main_data = json.load(infile)
    return main_data

# %%
