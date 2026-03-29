required_package = {"python3" , "pip" , "requests" , "boto3" , "pip"}
print(required_package)
print("if request in required package: " , "requests" in required_package)
print("if ansible in requierd package:" , "ansible" in required_package)
print(f"is 'requests' requierd? {"requests" in required_package}")
required_package.add("paramiko")
print(required_package)
required_package.remove("pip")
print(required_package)
required_package.discard("pip")
print(required_package)

installed_packages = {"docker" , "python3" , "pip"}
missing_packages = required_package.difference(installed_packages)
print(missing_packages)
extra_packages = installed_packages.difference(required_package)
print(extra_packages)
common_packages = required_package.intersection(installed_packages)
print(f"Missing Packages : {missing_packages} \nExtra Packages : {extra_packages} \nCommon Packages : {common_packages}")