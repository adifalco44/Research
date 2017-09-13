import os

def static_vars_(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate

@static_vars_(path=None)
def get_app_base_path():
    if get_app_base_path.path is None:
        get_app_base_path.path = os.path.dirname(os.path.realpath(__file__))
    return get_app_base_path.path

@static_vars_(path=None)
def get_instance_folder_path():
    if get_instance_folder_path.path is None:
        get_instance_folder_path.path = os.path.join(get_app_base_path(), 'instance')
    return get_instance_folder_path.path

@static_vars_(path=None)
def get_papers_folder_path():
    if get_papers_folder_path.path is None:
        get_papers_folder_path.path = os.path.join(get_app_base_path(), 'data', 'papers')
    return get_papers_folder_path.path

@static_vars_(path=None)
def get_pami_results_folder_path():
    if get_pami_results_folder_path.path is None:
        get_pami_results_folder_path.path = os.path.join(get_app_base_path(), 'data', 'pami_results')
    return get_pami_results_folder_path.path

@static_vars_(path=None)
def get_experiment_data_path():
    if get_experiment_data_path.path is None:
        get_experiment_data_path.path = os.path.join(get_app_base_path(), 'data', 'pamiexp.json')
    return get_experiment_data_path.path
