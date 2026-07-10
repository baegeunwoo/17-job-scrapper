from flask import Flask, render_template, request, send_file, redirect
from scrapper import search_incruit, search_saramin
from file import save_to_csv


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

db={}
page=2

@app.route('/search')
def search():
    keyword = request.args.get("keyword")

    if keyword == "":
        return redirect("/")

    print(keyword)
    
    if keyword in db:
        job_list = db[keyword]
    else:
        jobs = search_incruit(keyword,page)
        jobs2 = search_saramin(keyword,page)
        job_list = jobs+jobs2
        db[keyword] = job_list

    return render_template("search.html", jobs=enumerate(job_list),keyword=keyword,count=len(job_list))

@app.route('/file')
def file():
    keyword = request.args.get("keyword")
    if keyword == "":
        return redirect("/")

    if keyword in db:
        job_list = db[keyword]
    else:
        jobs = search_incruit(keyword, page)
        jobs2 = search_saramin(keyword,page)
        job_list = jobs+jobs2
    save_to_csv(job_list)
    return send_file("./downloads.csv", as_attachment=True) 

if __name__ == '__main__':
    app.run(debug=True)

