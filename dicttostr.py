def dictostr(d):
    d=str(d)
    d=d.replace('{',' " ')
    d=d.replace('}',' " ')
    d=d.replace(':','=')
    d=d.replace(',',';')
    return d
d={'name':'shashi','sem':'3rd','usn':'1cr16cs156'}
print('dictionary:', d , 'length:',len(d))
d=dictostr(d)
print('string:', d , 'length:',len(d))


