import sys
import os



try:
    dir_name=sys.argv[1];
except IndexError:
    print("\nPlease enter the directory name you want to store your project in as an arugment.\n")
    exit(1)

current_working_path=os.getcwd();

new_project_path=fr"{current_working_path}\{dir_name}";


html_boilerPlate=f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{dir_name.capitalize()}</title>

    <link rel="icon" type="image/svg" href="./assets/favicon.svg">
    <link rel="stylesheet" href="./css/output.css">

    <!-- google font -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
    <!-- google font -->

    <!-- font awesome -->
    <!-- <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css"> -->
    <!-- font awesome -->

</head>
<body>
    <h1 class="text-3xl font-bold underline">Hello World</h1>

    <script src="./js/app.js"></script>
</body>
</html>
"""


input_css_tailwind_boilerPlate="""@tailwind base;
@tailwind components;
@tailwind utilities;
"""

default_browser_icon='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path d="M284.3 11.7c-15.6-15.6-40.9-15.6-56.6 0l-216 216c-15.6 15.6-15.6 40.9 0 56.6l216 216c15.6 15.6 40.9 15.6 56.6 0l216-216c15.6-15.6 15.6-40.9 0-56.6l-216-216z"/></svg>'


try:
    print("Please wait a couple seconds while your project is being generated");
    os.mkdir(new_project_path);
    os.chdir(new_project_path);
    os.mkdir("css");
    os.mkdir("js");
    os.mkdir("assets")

    with open(fr"{new_project_path}\index.html", "w") as file:
        file.write(html_boilerPlate);
    
    with open(fr"{new_project_path}\css\input.css", "w") as file:
        file.write(input_css_tailwind_boilerPlate);
    
    with open(fr"{new_project_path}\js\app.js", "w") as file:
        file.write("");
    
    with open(fr"{new_project_path}\assets\favicon.svg", "w") as file:
        file.write(default_browser_icon);


    os.system("npm init -y");
    os.system("npm install -D  tailwindcss vite");
    os.system("npx tailwind init");

    print(f"\nAlmost done. Now cd into {dir_name}\n")
    print("\n1. Please add the entry point for tailwind, by copy and pasting './index.html' to the content array in the tailwind config file.\n");
    print('\n2. Please add the dev start script ( "dev": "vite" )  to the the package.json file for vite\n');
    print("Please open a seperate tab and run the mentioned below to generate the output.css file to start using tailwind \n npx tailwindcss -i ./css/input.css -o ./css/output.css --watch \n");
    print("\nNow opening VS Code if installed\n")
    os.system("code .");

except FileExistsError:
    print(f"\nThe directory {dir_name} already exist\n");