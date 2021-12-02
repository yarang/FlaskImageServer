from flask import Flask, render_template, request
import os

app = Flask(__name__)


def make_tree(path, args_path):
    tree = dict(name=os.path.basename(path), children=[])
    try:
        lst = os.listdir(path)
    except OSError as e:
        print(e)
        pass #ignore errors
    else:
        for name in lst:
            fn = os.path.join(path, name)
            if os.path.isdir(fn):
                hostname="http://oci2.fcoinfup.pw:5555/"
                href = hostname + os.path.join(args_path, name)
                tree['children'].append(dict(name=name, href=href, full=fn, dir=True))
            else:
                hostname="http://img1.thisismyreview.com/"
                href = hostname + os.path.join(args_path, name)
                tree['children'].append(dict(name=name, href=href, full=fn))
    return tree


@app.route('/', defaults={'args_path': None})
@app.route('/<path:args_path>')
def hello_world(args_path="/"):  # put application's code here
    if args_path is None:
        args_path = '/'
    path = os.path.expanduser(u'~/server/') + args_path
    print(path)
    return render_template('list.html', tree=make_tree(path, args_path))


if __name__ == '__main__':
    app.run()
