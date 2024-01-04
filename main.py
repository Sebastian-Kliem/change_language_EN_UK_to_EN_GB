import os


files = []
root_directory = "pkg_def"
for name in os.listdir(root_directory):
    if "Leer" in name:
        continue
    subname = os.path.join(root_directory, name)
    if os.path.isdir:
        subs = os.listdir(subname)
        for sub in subs:
            if ".txt" in sub:
                files.append(os.path.join(subname, sub))

    xml_path = os.path.join(root_directory, name, "root", "Eloma.Data", "UserData", "Config", "ParamsValue_Language.xml")

    if os.path.isfile(xml_path):
        files.append(xml_path)
    # print(xml_path)

print(f"{len(files)} in directory.")

counter = 0
for file in files:

    with open(file, "r+") as openfile:
        content = openfile.read()
        if "en_UK" in content:
            counter += 1
            print(file)

            changed_content = content.replace("en_UK", "en_GB")
            openfile.seek(0)
            openfile.write(changed_content)
            openfile.truncate()


print(f"{counter} Files are changed")





