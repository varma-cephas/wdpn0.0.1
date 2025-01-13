import shutil
import sys
import os


try:
    dir_name=sys.argv[1];
except IndexError:
    print("\nPlease enter the directory name you want to store your project in as an arugment.\n")
    exit(1)

current_working_path=os.getcwd();

new_project_path=fr"{current_working_path}\{dir_name}";
boiler_plate_path=r"C:\Users\varma\Documents\jan2025\wdpn.0.1\boilerPlate";


html_boilerPlate=f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{dir_name.capitalize()}</title>

    <link rel="icon" type="image/svg" href="./assets/favicon.png.svg">
    <link rel="stylesheet" href="./css/tailwind.css">

    <!-- google font -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
    <!-- google font -->

    <!-- font awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css">
    <!-- font awesome -->

</head>
<body>
    <h1 class="text-3xl font-bold underline">Hello World</h1>

    <script src="./js/app.js"></script>
</body>
</html>
"""

with open(r"C:\Users\varma\Documents\jan2025\wdpn.0.1\boilerPlate\index.html", "w") as file:
    file.write(html_boilerPlate);


try:
    shutil.copytree(boiler_plate_path, new_project_path);
    os.system(f"code {new_project_path}");
    # print(new_project_path)
    # os.system(f"cd ${new_project_path}");
    # os.system("npm init -y");
    # os.system("npm install -D  tailwindcss postcss autoprefixer vite");
    # os.system("npx tailwind init -p");
    print("Please add the start script to the the package.json file for vite")
except FileExistsError:
    print(f"\nThe directory {dir_name} already exist\n")
