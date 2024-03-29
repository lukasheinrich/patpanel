from flask import Flask, render_template
import yaml
import os
app = Flask('patpanel')
app.debug = True

@app.route('/')
def home():
    data = yaml.load(open('./sounds.yaml'))
    return render_template('base.html', data = data)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = int(os.environ.get('PORT',5000)))
