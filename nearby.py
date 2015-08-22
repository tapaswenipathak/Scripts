from googleplaces import GooglePlaces, types, lang

YOUR_API_KEY = 'AIzaSyBKmYWBe06Dcf_UCZMAoOcC7DyliluD76o'

google_places = GooglePlaces(YOUR_API_KEY)

loc = raw_input("Enter your location ")
# You may prefer to use the text_search API, instead.
query_result = google_places.nearby_search(
    location=loc, keyword='ngos or non profit organizations',
    radius=20000)

if query_result.has_attributions:
    print query_result.html_attributions

for place in query_result.places:
    # Returned places from a query are place summaries.
    print place.name
    print place.geo_location
    # print place.reference

    # The following method has to make a further API call.
    # place.get_details()
    # Referencing any of the attributes below, prior to making a call to
    # get_details() will raise a googleplaces.GooglePlacesAttributeError.
    # print place.details # A dict matching the JSON response from Google.
    # print place.local_phone_number
    # print place.international_phone_number
    # print place.website
    # print place.url

    # Getting place photos

    '''for photo in place.photos:
        # 'maxheight' or 'maxwidth' is required
        photo.get(maxheight=500, maxwidth=500)
        # MIME-type, e.g. 'image/jpeg'
        photo.mimetype
        # Image URL
        photo.url
        # Original filename (optional)
        photo.filename
        # Raw image data
        photo.data'''
