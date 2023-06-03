counties = ['Arapahoe','Denver','Jefferson']
counties_tuple=("Arapahoe","Denver","Jefferson")
counties_dict={}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
counties_dict.items()

voting_data=[]
voting_data.append({'county':'Arapahoe','registered_voters':422829})
voting_data.append({'county':'Denver','registered_voters':463353})
voting_data.append({'county':'Jefferson','registered_voters':432438})
#for counties_dict in voting_data:
    #print(counties_dict)
for counties_dict in voting_data:
    print(f"{counties_dict['county']} county has {counties_dict['registered_voters']:,} registered voters.")


#How many votes did you get?
candidate_votes=int(input("How many votes did you get in the election? "))
#Total votes in the election
total_votes=int(input("What is the total votes in the election? "))
#print(f"You received {candidate_votes:,} number of votes. \nThe total number of votes in the election was {total_votes:,}. \nYou received {candidate_votes/total_votes*100:.2f} % of the total votes.")

