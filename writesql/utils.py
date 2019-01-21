import os
import functools
from jinja2 import Template


def render_template(name, **kwargs):
    """ Render the template given a template name"""
    template = build_template(name)
    return template.render(**kwargs)


def build_template(name):
    """ Build the template given a template name"""
    temp_file = os.path.join('./templates',  name)
    with open(temp_file, 'r+') as f:
        template = f.readlines()
    return Template(''.join(template))


def as_template_function(f):
    """ A decorator that renders a function by its function name and keyword arguments."""
    f_name = f.__name__

    # TODO: make sure everything is passed in as keyword arguments
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        return render_template(f_name, **kwargs)
    return wrapped


def copy_and_print(text):
    """ Copy the text to clipboard and print it out"""
    from pandas.io.clipboard import clipboard_set

    clipboard_set(text)
    print(text)
