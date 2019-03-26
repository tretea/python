from flask import Flask
from flask import render_template,redirect
import pymysql
from flask import request
sql=pymysql.connect(user='root',password='123456',database='user',charset='utf8')
cursor=sql.cursor()
app = Flask(__name__)

@app.route('/')
@app.route('/yezi',methods=['GET','POST'])
def yezi():
    z_content=[]
    cursor.execute('select name,content,time from content')
    for name, content, time in cursor:
        z_content.append((name, content, time))
    name=request.args.get('name')
    if name==None:
        name='未登录'
    else:
        name=request.args.get('name')
    user=[]
    cursor.execute('select * from login')
    for use in cursor:
        user.append(use)
    return render_template('yezi.html', user=user, name=name, z_content=z_content)


@app.route('/register',methods=['GET','POST'])
def register():
    return render_template('register.html')
@app.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')
@app.route('/dl',methods=['GET','POST'])
def dl():
    bd_name = request.form['name']
    bd_password = request.form['pwd']
    cursor.execute(f'select * from login')
    for name,pwd,sex,phone in cursor:
        if name == bd_name or phone==int(bd_name):
            if pwd == bd_password:
                a_name=name
                return redirect(f'/?name={a_name}')
            else:
                return '登陆失败'
@app.route('/add',methods=['GET','POST'])
def add():
    name=request.form['name']
    sex=request.form['sex']
    phone=request.form['phone']
    password=request.form['pwd']
    try:
        cursor.execute(f'insert into login(name,sex,phone,password)values("{name}","{sex}",{phone},"{password}")')
        cursor.execute(f'create table {name}_content(con_id int,content text)')
        cursor.execute(f'alter table {name}_content add foreign key(con_id) references content(id)')
    except:
        return '用户名重复'
    else:
        sql.commit()
        return redirect('/')

@app.route('/content',methods=['GET','POST'])
def content():
    a_content=request.form['content']
    name=request.args.get('name')
    if name=='未登录':
        return '请先登录'
    cursor.execute(f'insert into content(name,content,time)values("{name}","{a_content}",now())')
    cursor.execute(f'select * from content where content="{a_content}"')
    for name,content,time,id in cursor:
        cursor.execute(f'insert into {name}_content(con_id,content)values({id},"{a_content}")')
    sql.commit()
    return redirect(f'/?name={name}')
@app.route('/delete',methods=['GET','POST'])
def delete():
    name = request.args.get("name")
    content=request.args.get("content")
    cursor.execute(f'select * from content where content="{content}"')
    for con_name,content,time,id in cursor:
        print(con_name)
        cursor.execute(f'delete from {con_name}_content where con_id={id}')
        cursor.execute(f'delete from content where id={id}')
    sql.commit()
    return redirect(f'/?name={name}')

@app.route('/delete_user',methods=['GET','POST'])
def delete_user():
    d_name = request.args.get("d_name")
    name = request.args.get("name")
    print(name)
    cursor.execute(f'delete from login where name="{d_name}"')
    cursor.execute(f'drop table {d_name}_content')
    sql.commit()
    return redirect(f'/?name={name}')
@app.route('/change',methods=['GET','POST'])
def change():
    name=request.args.get('name')
    cursor.execute(f'select * from login where name="{name}"')
    for name,password,sex,phone in cursor:
        if sex=='man':
            man='selected'
            woman=''
        else:
            woman='selected'
            man=''
        return render_template('change.html',name=name,password=password,man=man,woman=woman,phone=phone)
@app.route('/changing',methods=['GET','POST'])
def changing():
    name=request.args.get('name')
    sex=request.form['sex']
    phone=request.form['phone']
    password=request.form['pwd']
    cursor.execute(f'update login set sex="{sex}" where name="{name}"')
    cursor.execute(f'update login set phone={phone} where name="{name}"')
    cursor.execute(f'update login set password="{password}" where name="{name}"')
    sql.commit()
    return redirect(f'/?name={name}')

if __name__ == '__main__':
    app.run(debug=True)
