def mood_response(mood):
    if mood == 'happy':
        return 'happy is good'
    elif mood == 'sad':
        return 'sad is not good'
    elif mood == 'okay':
        return 'okay is okay'
    else:
        return 'invalid input, try again'