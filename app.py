import functools
from flask import Flask, render_template, jsonify, request
from forms import RandomForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'just-stuff'


def json(input_func):
    """
    Jsonifies whatever is outputted on the method this decorates.
    Can handle dictionary and lists well
    """
    @functools.wraps(input_func)
    def new_wrapped_func(*args, **kwargs):
        # This is the good stuff
        returned_value = input_func(*args, **kwargs)

        # Check whether it is not a dictionary or list
        if not isinstance(returned_value, dict) and not isinstance(returned_value, list):
            returned_value = returned_value.to_json()

        return jsonify(returned_value)

    return new_wrapped_func


@app.route('/')
def home():
    form = RandomForm()
    return render_template('index.html', form=form)


@app.route('/process', methods=['GET', 'POST'])
@json
def process():
    form = RandomForm(request.form)
    print(form)
    print('process()')

    return {'message': form.data, 'valid': form.validate()}


if __name__ == '__main__':
    app.run(debug=True)
