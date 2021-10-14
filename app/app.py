from flask import Flask, redirect
import requests
import markdown

head = """<!DOCTYPE html>
<html>
<head>
<style>
p {
    margin-bottom: 0px;
    font-style: italic;
}
pre {
    margin: 0px;
    margin-top: 2px;
    border-style: solid;
    border-width: 1px;
    border-color: #b3b3b3;
    padding: 6px;
}
div.center {
    //background-color: lightblue;
    width: 800px;
    margin: auto;
}
div.top {
    position: fixed;
    top: 0;
    //left: 0;
    width: 400px;
    //background: orange;
    text-align: right;
}
</style>
</head>
<body>
<div class="top">
<a href="/General.md">home</a><br>
<a href="/Ansible.md">ansible</a><br>
<a href="/Docker.md">docker</a><br>
<a href="/Java.md">java</a><br>
<a href="/Python.md">python</a><br>
<a href="/PHP.md">php</a><br>
<a href="/Man.md">man</a>
</div>
<div class="center">
"""

end = """
</div>
</body>
</html>
"""

response = requests.get("https://raw.githubusercontent.com/tohu-wabohu/wine/master/General.md")
data = response.text
html = markdown.markdown(data, extensions=['fenced_code'])

app = Flask(__name__)

@app.route('/')
def home():
   return redirect("/General.md", code=302)

@app.route('/<page>')
def pages_all(page):
   url = "https://raw.githubusercontent.com/tohu-wabohu/wine/master/" + page
   print(url)
   response = requests.get(url)
   data = response.text
   html = markdown.markdown(data, extensions=['fenced_code'])
   return head + html + end

if __name__ == '__main__':
   app.run('0.0.0.0', debug = True)

