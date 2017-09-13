# This was some seriously bad coding practices that
# I hacked together in a hurry.

from flask import abort, Blueprint, current_app, send_file, render_template
from flask import make_response, request

from ibio.cache import cache
from ibio.data.models import Experiment
from ibio import utils

import random, uuid, os

pamiexp = Blueprint('pamiexp', __name__, template_folder='templates')

@pamiexp.route('/')
def index():
    resp = make_response(render_template('intro.html'))
    data = Experiment.get_all()

    # 2D images
    synsets = []
    for k in data:
        if len(data[k]) == 1000:
            for e in data[k]:
                synsets.append(e['synset'])
            break
    random.shuffle(synsets)
    ids0 = []
    for s in synsets[:5]:
        for e in data['gausblur0']:
            if e['synset'] == s:
                ids0.append(e['id'])
    for s in synsets[5:10]:
        for e in data['brightinc']:
            if e['synset'] == s:
                ids0.append(e['id'])
    for s in synsets[10:15]:
        for e in data['linocc']:
            if e['synset'] == s:
                ids0.append(e['id'])
    tids1 = []
    for s in synsets[15:25]:
        for e in data['brightinc']:
            if e['synset'] == s:
                tids1.append(e['id'])
    ids1 = []
    for i in xrange(0,len(tids1),2):
        ids1.append(tids1[i:i+2])


    # 3D
    synsets = []
    tids1 = []
    for k in data:
        if len(data[k]) < 1000:
            for e in data[k]:
                synsets.append(e['synset'])
            break
    random.shuffle(synsets)
    for s in synsets[:5]:
        for e in data['noisesap']:
            if e['synset'] == s:
                ids0.append(e['id'])
    for s in synsets[5:10]:
        for e in data['rotxpos0']:
            if e['synset'] == s:
                ids0.append(e['id'])
    for s in synsets[10:15]:
        for e in data['scaleinc']:
            if e['synset'] == s:
                ids0.append(e['id'])
    for s in synsets[15:25]:
        for e in data['rotxpos1']:
            if e['synset'] == s:
                tids1.append(e['id'])
    for s in synsets[25:35]:
        for e in data['gausblur1']:
            if e['synset'] == s:
                tids1.append(e['id'])
    for i in xrange(0,len(tids1),2):
        ids1.append(tids1[i:i+2])
    random.shuffle(ids1)
    tids1 = ids1
    ids1 = []
    for e in tids1:
        ids1.append(e[0])
        ids1.append(e[1])

    random.shuffle(ids0)
    resp.set_cookie('exp0', ','.join(map(str, ids0)))
    resp.set_cookie('exp1', ','.join(map(str, ids1)))
    resp.set_cookie('exp0res', ','.join(['0']*len(ids0)))
    resp.set_cookie('exp1res', ','.join(['0']*(len(ids1)/2)))
    return resp

@pamiexp.route('/prac0')
def prac0():
    return render_template('prac0.html')

@pamiexp.route('/exp0')
def exp0():
    data = Experiment.get_all()

    trials = []

    ids = map(int, request.cookies.get('exp0').split(','))
    descs = {}
    tooltip = {}
    for id_ in ids:
        found = False
        if not found:
            for k in data:
                if not found:
                    for r in data[k]:
                        if r['id'] == id_:
                            found = True
                            trials.append(r)
    for e in data['gausblur0']:
        descs[e['synset']] = e['desc']
        tooltip[e['synset']] = e['tooltip']


    for trial in trials:
        ready = False
        while not ready:
            sample = random.sample(descs.keys(), 2)
            ready = True
            for s in sample:
                if s == trial['synset']:
                    ready = False

        options = [ [True, trial['desc'][:50], tooltip[trial['synset']]],
                    [False, descs[sample[0]][:50], tooltip[sample[0]]],
                    [False, descs[sample[1]][:50], tooltip[sample[1]]]]
        random.shuffle(options)
        trial['solution'] = [options[i][0] for i in range(3)]
        trial['choices'] = [options[i][1] for i in range(3)]
        trial['tooltip'] = [options[i][2] for i in range(3)]

    return render_template('exp0.html', exp0=trials)


@pamiexp.route('/exp1')
def exp1():
    data = Experiment.get_all()

    trials = []

    tids = map(int, request.cookies.get('exp1').split(','))
    ids = []
    for id_ in tids:
        found = False
        if not found:
            for k in data:
                if not found:
                    for r in data[k]:
                        if r['id'] == id_:
                            found = True
                            ids.append(r)
    pos_ids = ids[0::2]
    neg_ids = ids[1::2]

    pvs = {}
    for e in data['vgg16']:
        pvs[e['path'].split('/')[-1]] = e

    for i in xrange(len(pos_ids)):
        trial = pos_ids[i]
        options = [pos_ids[i], neg_ids[i]]
        random.shuffle(options)
        solution = map(lambda e: e == pos_ids[i], options)
        # switch image here
        options[0] = pvs[options[0]['path'].split('/')[-1]]['path']
        options[1] = pvs[options[1]['path'].split('/')[-1]]['path']

        trial['choices'] = options
        trial['solution'] = solution
        trials.append(trial)

    return render_template('exp1.html', exp1=trials)


@pamiexp.route('/prac1')
def prac1():
    return render_template('prac1.html')

@pamiexp.route('/results')
def results():
    exp0 = map(int, request.cookies.get('exp0').split(','))
    exp0res = map(int, request.cookies.get('exp0res').split(','))
    exp1 = map(int, request.cookies.get('exp1').split(','))
    exp1res = map(int, request.cookies.get('exp1res').split(','))

    with open(os.path.join(utils.get_pami_results_folder_path(), str(uuid.uuid4())+'.csv'), 'w') as f:
        f.write(','.join(map(str, exp0))+'\n')
        f.write(','.join(map(str, exp0res))+'\n')
        f.write(','.join(map(str, exp1))+'\n')
        f.write(','.join(map(str, exp1res))+'\n')

    results = {'exp0': sum(exp0res), 'exp1': sum(exp1res)}
    return render_template('results.html', results=results)
