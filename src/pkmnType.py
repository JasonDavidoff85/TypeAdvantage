import requests

allpkmnUrl = "https://pokeapi.co/api/v2/pokemon/?limit=964"


pokemonNames = requests.get(url=allpkmnUrl)
pokemon = pokemonNames.json()
pokemonNameList = []
for i in pokemon['results']:
	pokemonNameList.append(i['name'])


pkmn = 'squirtle'
#pkmn = input("Pokemon name >> ")
while pkmn.lower() not in pokemonNameList:
	print('Pokemon not found...')
	#pkmn = input("Pokemon name >> ")

pkmnUrl = "https://pokeapi.co/api/v2/pokemon/%s/" %(pkmn.lower())
pokemonInfo = requests.get(url=pkmnUrl)
pokemonInfo = pokemonInfo.json()
types = []
for i in pokemonInfo['types']:
	types.append(i['type']['name'])

output = "%s is a %s"
if len(types) > 1:
	output = output + " and %s type"
	print(output %(pkmn.capitalize(),types[0],types[1]))
	print("="*len(output %(pkmn.capitalize(),types[0],types[1])))
else:
	output = output + " type"
	print(output %(pkmn.capitalize(),types[0]))
	print("="*len(output %(pkmn.capitalize(),types[0])))


typeInfo = []
for i in types:
	typeUrl = "https://pokeapi.co/api/v2/type/%s/"
	typeInfo.append(requests.get(url=typeUrl %(i)).json()['damage_relations'])

_05x = []
_025x = []
_2x = []
_4x = []
_0x = []


for i in typeInfo:
	for j in i['double_damage_from']:
		_2x.append(j['name'])
	for j in i['half_damage_from']:
		_05x.append(j['name'])
	for j in i['no_damage_from']:
		_0x.append(j['name'])


for i in _05x:
	if i in _2x:
		_05x.remove(i)
		_2x.remove(i)
	if _05x.count(i) > 1:
		_025x.append(i)
		_05x.remove(i)
		_05x.remove(i)

for i in _2x:
	if i in _05x:
		_2x.remove(i)
		_05x.remove(i)
	if _2x.count(i) > 1:
		_4x.append(i)
		_2x.remove(i)
		_2x.remove(i)

if len(_2x) > 0:
	print("Double damage from: " + ", ".join(map(str,_2x)))

if len(_4x) > 0:
	print("Quad damage from: " + ", ".join(map(str,_4x)))

if len(_05x) > 0:
	print("Half damage from: " + ", ".join(map(str,_05x)))

if len(_025x) > 0:
	print("Quarter damage from: " + ", ".join(map(str,_025x)))

if len(_0x) > 0:
	print("No damage from: " + ", ".join(map(str,_0x)))
