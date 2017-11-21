import string
from flask import Flask, abort, Blueprint, current_app, send_file, render_template, url_for, g
from flask import make_response, redirect, request

from web.cache import cache

faces = Blueprint('faces', __name__, template_folder='templates')


'''
@faces.route('/')
def index():
    # create a session ID here. use uuid.uuid4
    user_id = 1
    # store in cookie
    redirect_to_trial = redirect("/trial")
    response = current_app.make_response(redirect_to_trial)
    response.set_cookie("user_id",value=user_id)
    # redirect to route('/trial')
    return redirect(url_for('faces.trial'))

@faces.route('/trial')
def trial():
   # load session ID from cookie (do not modify it)


    # itera    itera    itera    it    return response
    # get remaining trials for session ID
    
    # if no remaining trials, redirect to mturk
    # else, randomly pick one, and return trial
    return render_template('trial.html')
'''

@faces.route('/trial/<path:code>')
def trial(code):
    
    # Dummy inits
    data_in = ['Brandon Richard Webster','Kevin Bower','Walter Scheirer']
    data_out = []

    # Decode incoming URL
    temp = code.split('/')  
    user_name = temp[0]
    question_num_in = temp[1]
    question_id_in = temp[2]
    question_answer_in = temp[3]

    # Testing
    print("Question Answer : {}".format(question_answer_in))
    print("Question Number : {}".format(question_num_in))
    print("Question ID: {}".format(question_id_in))
    print("User ID: {}".format(user_name))

    # Encode outoing URL base characteristics
    question_num_out = str(int(question_num_in)+1)

    # Build out whole url
    answer = data_in[0].replace(' ','_')
    url1_tail = data_in[0].replace(' ','_')
    url1='/faces/'+user_name+'/'+question_num_out+'/'+answer+'/'+url1_tail
    
    url2_tail = data_in[1].replace(' ','_')
    url2='/faces/'+user_name+'/'+question_num_out+'/'+answer+'/'+url2_tail

    url3_tail = data_in[2].replace(' ','_')
    url3='/faces/'+user_name+'/'+question_num_out+'/'+answer+'/'+url3_tail

    # Testing
    print("URL 1: {}".format(url1))
    print("URL 2: {}".format(url2))
    print("URL 3: {}".format(url3))

    print("Data 1: {}".format(data_in[0]))
    print("Data 2: {}".format(data_in[1]))
    print("Data 3: {}".format(data_in[2]))


    # Build out object
    tmp_trial = {}
    # Get button name
    tmp_trial['data0'] = data_in[0]
    tmp_trial['data1'] = data_in[1]
    tmp_trial['data2'] = data_in[2]
    # Get image
    tmp_trial['image'] = 'https://engineering.nd.edu/profiles/brichardwebster/@@images/81a1b34f-ee63-457b-864a-cb8eee7df648.jpeg' 
    # Get URLS
    tmp_trial['url1'] = url1
    tmp_trial['url2'] = url2
    tmp_trial['url3'] = url3
    # Append object
    data_out.append(tmp_trial)
    return render_template('trial.html',data=data_out)



'''

@faces.route('/response',methods=['POST','GET'])
def response():
        if request.method == 'GET':
            db = get_db()
            # Get user_id
            session_id = request.get['user_id']
            #iterate question
            iterator = int(request.get['question_num'])
            iterator=iterator+1
            #force response
            redirect_to_trial = redirect("/trial")
            response = current_app.make_response(redirect_to_trial)
            response.set_cookie("question_num", value=str(iterator))
            query = query_db(select * from Exp where Session_id=1)
            return render_template('Example.html',data=query)
        if request.method == 'POST':
            db = get_db()
            query = query_db(select * from Exp where Session_id=?,
                    [1],one=True)
            ID = query['Session_id']
            Solution = query['Sol']

            db.execute(insert into Data (Question_id,Correct_answer,Submitted_answer) values (?,?,?),
                     [ID,Solution,request.form['options']])
            db.commit()
            db_tmp = get_db()
            query_tmp = query_db(select * from Data)
            return render_template('Data.html',data=query_tmp)


    
    # record response
    # redirect to trial
    return redirect(url_for('faces.trial'))
'''

