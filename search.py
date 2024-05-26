 for track in result['tracks']['items']:
        id = track['id']
        id_list.append(id)

    features = sp.audio_features(id_list)
    pprint.pprint(features) for track in result['tracks']['items']:
        id = track['id']
        id_list.append(id)

    features = sp.audio_features(id_list)
    pprint.pprint(features)