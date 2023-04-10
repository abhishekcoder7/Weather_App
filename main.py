import requests
import json
import os

flag=1
while flag==1:
    city = input("Enter City name to find it's Weather / Press Q to Exit ")
    if city=="Q" or city=="q":
        flag=0
        command = f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('Closing Weather Application')"
        answer="Closing Weather Application"
        break
    url = requests.get(f"https://api.weatherapi.com/v1/current.json?key=61c72ba2e6f846b7ae6170022231004&q={city}")

    result = json.loads(url.text)
    temperature = result["current"]["temp_c"]

    answer = f"Temperature of {city.capitalize()} is {temperature} celsius"

    command = f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{answer}')"
    print(answer)
    os.system(command)



print(answer)
os.system(command)

