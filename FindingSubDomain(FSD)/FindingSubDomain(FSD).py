import requests

# variables 
domain = input("The Domain: ") 
file = open(input("The Word List File Name: "))
content = file.read()
subdomains = content.splitlines()
discovered_subdomains = []


#Main function
for subdomain in subdomains:
    link = f"http://{subdomain}.{domain}"
    try:
        requests.get(link)
    except requests.ConnectionError:
        pass
    else:
        print("[+] Discovered subdomains", link)
        discovered_subdomains.append(link)

#Saving Output
with open("Results.txt", "w") as f:
    for subdomain in discovered_subdomains:
        print(subdomain, file=f)

