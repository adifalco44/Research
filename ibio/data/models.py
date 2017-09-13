import copy
import json
import os
from ibio import utils

class Authors(object):
    def __init__(self):
        pass

    @staticmethod
    @utils.static_vars_(authors=None)
    def get_all():
        if Authors.get_all.authors is None:
            with open(utils.get_papers_folder_path() + '/authors.json', 'r') as f:
                authors = json.load(f)
                for k in authors:
                    authors[k]['key'] = k
                Authors.get_all.authors = authors
        return Authors.get_all.authors

class Paper(object):
    def abstract_(self, path):
        with open(utils.get_papers_folder_path() + '/'+ path) as f:
            self.abstract = f.read().decode('utf-8').strip()

    def authors_(self, authors):
        lookup = Authors.get_all()
        self.authors = []
        for i in range(len(authors)):
            key = authors[i]
            self.authors.append(lookup[authors[i]])

    def cid_exists(self, cid):
        return bool(self.get_dl_link(cid))

    def get_dl_link(self, cid):
        return {
            'pdf' : self.pdf,
            'supp' : self.supp,
            'bibtex' : self.bibtex
        }[cid]

    @staticmethod
    def exists(key):
        hash_ = Paper.get_all(type_='hash')
        return key in hash_

    def __init__(self, key, data):
        self.title = data['title']
        self.authors_(data['authors'])
        self.venue = data['venue']
        self.status = data['status']
        self.abstract_(data['abstract'])
        self.pdf = data['pdf']
        self.supp = data['supp'] if 'supp' in data else ''
        self.bibtex = data['bibtex']
        self.pos = data['pos']
        self.key = key

    @staticmethod
    @utils.static_vars_(papers_list=None, papers_hash=None)
    def get_all(type_='list'):
        if Paper.get_all.papers_list is None:
            with open(utils.get_papers_folder_path() + '/papers.json', 'r') as f:
                papers = json.load(f)
                Paper.get_all.papers_list = map(lambda k: Paper(k, papers[k]), papers)
                papers = {}
                for e in Paper.get_all.papers_list:
                    papers[e.key] = e
                Paper.get_all.papers_hash = papers
        if type_ == 'list':
            return copy.deepcopy(Paper.get_all.papers_list)
        elif type_ == 'hash':
            return copy.deepcopy(Paper.get_all.papers_hash)

class Experiment(object):
    def __init__(self):
        pass

    @staticmethod
    @utils.static_vars_(data=None)
    def get_all():
        if Experiment.get_all.data is None:
            with open(utils.get_experiment_data_path(), 'r') as f:
                data = json.load(f)
                Experiment.get_all.data = data
        return Experiment.get_all.data
