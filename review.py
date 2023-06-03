counties_dict={}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
counties_dict.items()
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")
voting_data=[]
voting_data.append({'county':'Arapahoe','registered_voters':422829})
voting_data.append({'county':'Denver','registered_voters':463353})
voting_data.append({'county':'Jefferson','registered_voters':432438})
for counties_dict in voting_data:
    print(f"{counties_dict['county']}  {counties_dict['registered_voters']}")
import datetime
now=datetime.datetime.now()
print('The time right now is',now)