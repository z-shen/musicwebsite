from flask import Flask,render_template,request,session,redirect
from models import item
from models.user import User
from common.database import Database
from models.video import Video
app = Flask(__name__)
app.secret_key = "luke_liu"

@app.before_first_request
def init_db():
    Database('localhost:27017','user')

@app.route("/")
def hello():
    return render_template("home.html")

@app.route("/login",methods=['GET','POST'])
def login_method():
    if request.method == "POST":
        account = request.form['InputAccount']
        password = request.form['InputPassword']
        user = User(account, password)
        print('the account is {0},password is {1}'.format(user.account,user.password))
        result = user.is_login_valid()
        if result is True:
            session['account'] = user.account
            return redirect('/')
        else:
            message = "Your account or password is wrong"
            return render_template("login.html", message=message)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout_mthod():
    session['account'] = not session['account']
    return redirect('/')

@app.route("/register",methods=["POST","GET"])
def register_method():
    if request.method == "POST":
        account = request.form['InputAccount']
        password = request.form['InputPassword']
        user = User(account, password)
        print('the account is {0},password is {1}'.format(user.account,user.password))
        result = user.register_user(user.account)
        if result is True:
            session['account'] = user.account
            return redirect('/')
        else:
            message = "Your account is registered"
            return render_template("login.html", message=message)
    else:
        return render_template("register.html")



@app.route("/results")
def result_page():
    url = request.url
    favorite_video = []
    user_favorite = Video(session['account']).fine_video(session['account'])
    for video in user_favorite:
        favorite_video.append(video['link'])

    if request.args.get("q") is None:
        search = request.args.get("search")
        soup = item.find_search_content(search)
        all_item = item.every_video(soup)
        all_page = item.page_bar(soup)
        return render_template("result.html",search=search,all_item=all_item,all_page=all_page,url=url,favorite_video=favorite_video)

    elif request.args.get("q") is not None:
        search = request.args.get("q")
        page = request.args.get("sp")
        current_page = request.args.get("current_page")
        link = "q={}".format(search)+"&sp={}".format(page)
        soup = item.find_page_content(link)
        all_item = item.every_video(soup)
        all_page = item.page_bar(soup)
        return render_template("result_page.html", search=search, all_item=all_item, all_page=all_page,current_page=current_page,int=int,url=url,favorite_video=favorite_video)
    else:
        return redirect('/')


@app.route("/favorite",methods=["GET","POST"])

def favorite_method():
    if session['account']:
        if request.method == "POST":
            url = request.form['url']
            title = request.form['title']
            link = request.form['link']
            img = request.form['img']
            time = request.form['time']
            account = session['account']
            print("the url is {0},the title is {1},the link is {2},the img is {3},the account is {4}".format(url,title,link,img,account))
            Video(account,title,link,img,time).save_to_db()
            return redirect(url)
        else:
            account = session['account']
            user_video = Video(account).fine_video(account)
            print(user_video)
            return render_template("favorite.html", user_video=user_video)

    else:
        return redirect("/login")

@app.route("/delete",methods=["POST"])
def remove_method():
    if session['account']:
        link = request.form['link']
        account = session['account']
        print("the link is {0}".format(link))
        Video(account).delete_video(account,link)
        return redirect("/favorite")

@app.route("/download")
def download():
    value = request.args.get("value")
    download_type,url = str(value).split("&")

    if download_type == 'MP3':
        item.download_mp3(url)
        return render_template("download.html")
    elif download_type == 'MP4':
        item.download_mp4(url)
        return render_template("download.html")
if __name__ == "__main__":
    app.run(debug=True,port=8080)