from jinja2 import Template, Environment, FileSystemLoader


# https://atufashireen.medium.com/creating-templates-with-jinja-in-python-3ff3b87d6740
# https://codeburst.io/jinja-2-explained-in-5-minutes-88548486834e
# https://realpython.com/primer-on-jinja-templating/
# https://jinja.palletsprojects.com/en/3.1.x/api/
# https://documentation.bloomreach.com/engagement/docs/filters
def what_is_template():
    name = input("Enter your name: ")
    tm = Template("Hello {{ name }}")
    msg = tm.render(name=name)
    print(msg)


def template_with_more_data(**kwargs):
    tm = Template("My name is {{ name }} and I am {{ age }}")
    msg = tm.render(**kwargs)
    print(msg)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getAge(self):
        return self.age

    def getName(self):
        return self.name


def template_with_class():
    person = Person('Peter', 34)
    tm1 = Template("My name is {{ per.getName() }} and I am {{ per.getAge() }}")
    tm2 = Template("My name is {{ per.name }} and I am {{ per.age }}")
    msg1 = tm1.render(per=person)
    msg2 = tm2.render(per=person)
    print(msg1, msg2)


def template_with_dict():
    person = {"name": "Alice", "age": 12}
    tm = Template("My name is {{ per.name }} and I am {{ per.age }}")
    tm_1 = Template("My name is {{ per['name'] }} and I am {{ per['age']}}")
    msg = tm.render(per=person)
    msg_1 = tm_1.render(per=person)
    print(msg, msg_1)


def escape_data():
    data = '<a>Today is a sunny day</a>'
    tm = Template("{{ data }}")
    msg = tm.render(data=data)
    print(msg)


# loop

persons = [
    {'name': 'Andrej', 'age': 34},
    {'name': 'Mark', 'age': 17},
    {'name': 'Thomas', 'age': 44},
    {'name': 'Lucy', 'age': 14},
    {'name': 'Robert', 'age': 23},
    {'name': 'Dragomir', 'age': 54}
]

cars = [
    {'name': 'Audi', 'price': 23000},
    {'name': 'Skoda', 'price': 17300},
    {'name': 'Volvo', 'price': 44300},
    {'name': 'Volkswagen', 'price': 21300}
]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

env.globals["test"] = "name"
env.add_extension('jinja2.ext.debug')
env.add_extension('jinja2.ext.i18n')


def render_tmplate_files():
    template = env.get_template("examples.txt")
    result = template.render(persons=persons, cars=cars)
    print(result)
    # context_data = {persons:persons,cars:cars}
    # result2= template.render(context_data)
    # print(result2)


def html_render():
    content = 'This is about page'
    template = env.get_template('about.html')
    output = template.render(content=content)
    print(output)


def prefix_str(content: str,more_content:str) -> str:
    return "prefix-" + content+"-"+str(more_content)


env.globals["prefix_str"] = prefix_str

if __name__ == '__main__':
    # what_is_template()
    template_with_more_data(name="John", age=27)
    template_with_class()
    template_with_dict()
    escape_data()
    render_tmplate_files()
    html_render()
