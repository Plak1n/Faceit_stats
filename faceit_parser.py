import os
import requests
import pyfaceit
from prettytable import PrettyTable
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

os.chdir(os.path.dirname(__file__))

class FaceitProfile(pyfaceit.Pyfaceit):
    def __init__(self, pname) -> None:
        super().__init__(pname)
        try:
            if super().player_id is None:
                raise Exception("Player doesnt exist")
            player_data_json = (requests.get(f"https://open.faceit.com/data/v4/players/{super().player_id}/stats/csgo",headers=self.api_header)).json()
            self.map_data = player_data_json['segments']
        except Exception:
            return None
    
    def show_map_data(self):
        table = PrettyTable()
        table.field_names = ["Map", "Matches", "Win Rate %", "Average Kills", "Average K/D Ratio", "Average K/R Ratio","Average Headshots %"]
        for i in range(len(self.map_data)):
            if self.map_data[i]['mode'] == "5v5":
                table.add_row([f"{self.map_data[i]['label']}",
                        f"{self.map_data[i]['stats']['Matches']}",
                        f"{self.map_data[i]['stats']['Win Rate %']}",
                        f"{self.map_data[i]['stats']['Average Kills']}",
                        f"{self.map_data[i]['stats']['Average K/D Ratio']}",
                        f"{self.map_data[i]['stats']['Average K/R Ratio']}",
                        f"{self.map_data[i]['stats']['Average Headshots %']}"])
        print(f"{self.pname} stats")
        print(table)
       
        
    @staticmethod
    def get_nicknames(url: str, team_number: int):
        """Team on the left has number1. Team on the right has number2"""
        chrome_options = Options()
        chrome_options.add_argument("--disable-infobars")
        driver = webdriver.Chrome(options = chrome_options)
        driver.get(url)
        driver.implicitly_wait(15)
        all_nicknames = (driver.find_element(By.NAME,f"roster{team_number}").text).split("\n")
        required_nicknames = [all_nicknames[0],all_nicknames[2], all_nicknames[4], all_nicknames[6], all_nicknames[8]]
        return required_nicknames

# url = input("Enter url of you faceit match: ")
# team_number = int(input("Enter team number. Team on the left has number 1, team on the right has number 2: "))
# nicknames = get_nicknames(url,team_number)
# profile_links = []
# for nk in nicknames:
#     profile_links.append(f"https://www.faceit.com/en/players/{nk}")
# print(profile_links)

if __name__ == "__main__":
    url = input("Enter url of faceit match: ")
    team_number = int(input("Enter team number 1 or 2(team on the left has number 1, on the right 2): "))
    nicknames = FaceitProfile.get_nicknames(url,team_number)
    for nick in nicknames:
        player = FaceitProfile(f"{nick}")
        player.show_map_data()