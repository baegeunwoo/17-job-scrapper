from flask import Flask, render_template, request
from scrapper import search_incruit, search_saramin


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")



@app.route('/search')
def search():
    keyword = request.args.get("keyword")
    print(keyword)
    jobs = search_incruit(keyword)
    # jobs2 = search_saramin(keyword)
    # job_list = jobs+jobs2
    job_list = jobs
    return render_template("search.html", jobs=enumerate(job_list),keyword=keyword,count=len(jobs))

@app.route('/file')
def file():
    return "file"

if __name__ == '__main__':
    app.run(debug=True)

