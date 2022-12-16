from django import template


register = template.Library()

@register.filter()
def censor(value: str) -> str:
    CURRENCY_WORDS = {'INTERFAX.RU':True,
                      'умерших': True
                      }
    try:
        if not isinstance(value, str):
            raise Exception('Error')
        a = value
        for word in list(CURRENCY_WORDS.keys()):
            if word in a:
                a = a.replace(word, f'{word[:1]}***')
            if word.capitalize() in a:
                a = a.replace(word.capitalize(), f'{word[:1].capitalize()}***')
        return a
    except Exception as e:
        print(e)