from firebase import firebase

firebase = firebase.FirebaseApplication('https://abj-website-coming.firebaseio.com/')
data = {
    'coming soon': [
        'placeholder',
        {
            'name': 'Test',
            'img': 'https://images-na.ssl-images-amazon.com/images/I/512dVKB22QL._AC_UL600_SR600,600_.png'
            } 
        ]
}
result = firebase.put('/data', '-MM-Fk81Pb_-is1HFBre', data)