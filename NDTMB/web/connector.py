import uuid

global index
index = {}

def new_user(mturk):
    return str(uuid.uuid4())

def get_trial(sid):
    global index
    if sid not in index:
        index[sid] = -1
    index[sid] += 1
    fakedb = []
    obj1 = {
        # experiment data
        'ProbeTime'             : 500,
        'idExperiments'         : 1,
        'idDataType_Probe'      : 1,
        'idDataType_Gallery'    : 1,

        # participant data
        'idParticipants'        : 1,
        'UUID'                  : sid,

        # trial data
        'idTrials'              : 1,
        'ProbeID'               : 1,
        'ProbePath'             : 'http://www.saintsrescue.ca/new_site//wp-content/gallery/barn_animals_sponsorship/Brad-Pitt.jpg',
        'Gallery1ID'            : 1,
        'Gallery1Path'          : 'http://www.saintsrescue.ca/new_site//wp-content/gallery/barn_animals_sponsorship/Brad-Pitt.jpg',
        'Gallery2ID'            : 2,
        'Gallery2Path'          : 'https://images-na.ssl-images-amazon.com/images/I/91w1cLKbY-L._SX355_.jpg',
        'Gallery3ID'            : 3,
        'Gallery3Path'          : 'http://whitefencefarm-il.com/img/BarnAnimals_2.jpg'
    }

    obj2 = {
        # experiment data
        'ProbeTime'             : 500,
        'idExperiments'         : 1,
        'idDataType_Probe'      : 1,
        'idDataType_Gallery'    : 1,

        # participant data
        'idParticipants'        : 1,
        'UUID'                  : obj1['UUID'],

        # trial data
        'idTrials'              : 2,
        'ProbeID'               : 6,
        'ProbePath'             : 'http://s1.1zoom.me/big3/478/338769-sepik.jpg',
        'Gallery1ID'            : 4,
        'Gallery1Path'          : 'https://dncache-mauganscorp.netdna-ssl.com/thumbseg/1554/1554897-bigthumbnail.jpg',
        'Gallery2ID'            : 5,
        'Gallery2Path'          : 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxukmqgr5IzjTfdPiyFwUamNI0QVrmq1lfgZCYO0BzF7iTU7iShA',
        'Gallery3ID'            : 6,
        'Gallery3Path'          : 'http://s1.1zoom.me/big3/478/338769-sepik.jpg'
    }
    fakedb.append(obj1)
    fakedb.append(obj2)

    if index[sid] > 1:
        return None
    else:
        return fakedb[index[sid]]

def set_response(sid, tid, rid):
    pass
