# Coderdojo Battlesnake

## SlangenBrein (brein.py)
Subclass van deze klasse om je eigen slang te maken.

## Eigenschappen
### ID
```self.id```
De identificatiecode van je slang. Elke slang heeft zo'n ID.
Ziet er zo uit: snake-508e96ac-94ad-11ea-bb37.

### Gezondheid
```self.gezondheid```
Hoe gezond is je slang nog? Een getal tussen 1 en 100.

### Speelbord
```self.bord```
Het bord waarop je slang beweegt.
Het bord bestaat uit x * y cellen. Een cel kan een lege cel zijn, een cell met eten of een stukje slang. 

### Honger
```def heeft_honger()```
Overschrijf deze methode en programmeer hier wanneer je slang honger heeft, wanneer hij sneller voedsel moet zien te vinden.

## Customisatie
In je eigen slang, kun je het uiterlijk aanpassen.
De codes vind je hier: https://docs.battlesnake.com/references/personalization

```
  @classmethod
  def uiterlijk(cls):
    return {
      "apiversion": "1",
      "author": "soetkin",
      "color": "#FFC0CB",
      "head": "safe",
      "tail": "round-bum",
      }
```