from jinja2 import Environment, FileSystemLoader
from os import walk
from shutil import copytree, rmtree, ignore_patterns

try: rmtree("./build")
except Exception as e: print("Creating build folder", e, "Occured")

copytree("./", "./build", ignore=ignore_patterns('*.py', "templates", "*.git"))


ENV = Environment(loader=FileSystemLoader('./templates'))

# List of pages to be rendered -- MUST be listed according to their
# order in the navigation bar
_, _, PAGE_LIST = next(walk('./templates'))


for file_name in PAGE_LIST:

    template = ENV.get_template(file_name)
    html = template.render()
    # Write output in the corresponding HTML file
    print('Writing', file_name)
    with open(str("./build/" + file_name), 'w+') as out_file:
        out_file.write(html)