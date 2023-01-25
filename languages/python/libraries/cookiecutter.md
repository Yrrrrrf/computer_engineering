# [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/)

Is a command-line utility that creates projects from cookiecutters ([[project management|project]] templates). It was originally created by Audrey Roy Greenfeld and licensed under the MIT license. It is now maintained by the [[Python]] Software Foundation. 

To create a project from a cookiecutter, you need to install cookiecutter and then run the command `cookiecutter <cookiecutter-repo-url>`. Cookiecutter will prompt you for any variables that are defined in the cookiecutter.json file. It will then create a directory for your project and fill it with the rendered template files.

## Installation
```python
pip install cookiecutter
```

## Usage
Cookiecutter will prompt you for any variables that are defined in the `cookiecutter.json` file. It will then create a directory for your project and fill it with the rendered template files.
```python
cookiecutter <cookiecutter-repo-url>
cookiecutter <cookiecutter-repo-url> --checkout <branch>
```

## Template Files
The template files are the files that will be rendered when you run the cookiecutter command. They can be any type of file, including text files, images, and binary files. The template files can use the `Jinja2` templating language to reference the variables defined in the `cookiecutter.json` file.

The `cookiecutter.json` defines the variables that will be prompted for when you run the cookiecutter command. It also defines the default values for those variables. The variables can be used in the template files using the `Jinja2` templating language.

## Hooks
You can define hooks in the `hooks` directory. These hooks are scripts that will be run at different points in the cookiecutter process. The hooks are defined in the `cookiecutter.json` file. The hooks are:
- `pre_gen_project`: This hook is run before the template files are rendered.
- `post_gen_project`: This hook is run after the template files are rendered.

## Example
Here is an example of a `cookiecutter.json` file:
```json
{
    "project_name": "My Project",
    "project_slug": "{{ cookiecutter.project_name.lower().replace(' ', '_') }}",
    "project_short_description": "A short description of the project.",
    "version": "0.1.0",
    "author_name": "Your Name",
    "open_source_license": ["MIT license", "BSD license", "ISC license", "Apache Software License 2.0", "GNU General Public License v3", "Not open source"]
}
```

----
##### [check my templates!](https://github.com/Yrrrrrf/cookiecutter-templates)

