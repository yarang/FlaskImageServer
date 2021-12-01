from flask import Flask, render_template
import os

app = Flask(__name__)


def make_tree(path):
    tree = dict(name=os.path.basename(path), children=[])
    try: lst = os.listdir(path)
    except OSError:
        pass #ignore errors
    else:
        for name in lst:
            fn = os.path.join(path, name)
            if os.path.isdir(fn):
                tree['children'].append(make_tree(fn))
            else:
                tree['children'].append(dict(name=name))
    return tree


@app.route('/')
def hello_world():  # put application's code here
    path = os.path.expanduser(u'~/server')
    return render_template('list.html', tree=make_tree(path))

if __name__ == '__main__':
    app.run()
