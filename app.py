from flask import Flask, render_template, url_for
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Read bills.csv into pandas DataFrame
    bills_df = pd.read_csv(r'bills.csv')

    # Initialize an empty list to store dictionaries
    bills_list = []

    # Iterate over each row in the DataFrame
    for index, row in bills_df.iterrows():
        # Create a dictionary for the current row
        bills_dict = {}
        for i in range(len(row)):
            bills_dict[bills_df.columns[i]] = row.iloc[i]
        # Append the dictionary to the list
        bills_list.append(bills_dict)

    # Print the list of dictionaries
    print('bills table', bills_list)

    # Read CSV file into pandas DataFrame
    legislators_df = pd.read_csv(r'legislators.csv')

    # Initialize an empty list to store dictionaries
    legislators_list = []

    # Iterate over each row in the DataFrame
    for index, row in legislators_df.iterrows():
        # Create a dictionary for the current row
        legislators_dict = {}
        for i in range(len(row)):
            legislators_dict[legislators_df.columns[i]] = row.iloc[i]
        # Append the dictionary to the list
        legislators_list.append(legislators_dict)

    # Print the list of dictionaries
    print('legislators table', legislators_list)

    # Read CSV file into pandas DataFrame
    votes_df = pd.read_csv(r'votes.csv')

    # Initialize an empty list to store dictionaries
    votes_list = []

    # Iterate over each row in the DataFrame
    for index, row in votes_df.iterrows():
        # Create a dictionary for the current row
        votes_result_dict = {}
        for i in range(len(row)):
            votes_result_dict[votes_df.columns[i]] = row.iloc[i]
        # Append the dictionary to the list
        votes_list.append(votes_result_dict)

    # Print the list of dictionaries
    print('votes table', votes_list)

    # Read CSV file into pandas DataFrame
    vote_results_df = pd.read_csv(r'vote_results.csv')

    # Initialize an empty list to store dictionaries
    vote_results_list = []

    # Iterate over each row in the DataFrame
    for index, row in vote_results_df.iterrows():
        # Create a dictionary for the current row
        vote_result_dict = {}
        for i in range(len(row)):
            vote_result_dict[vote_results_df.columns[i]] = row.iloc[i]
        # Append the dictionary to the list
        vote_results_list.append(vote_result_dict)

    # Print the list of dictionaries
    print('vote result table', vote_results_list)

    # list to return
    listFinal = []
    listFinal2 = []

    for leg in legislators_list:
        auxInfo = {}
        counterYes = 0
        counterNo = 0
        auxInfo['legislator_id'] = leg['id']
        auxInfo['legislator_name'] = leg['name']
        for result in vote_results_list:
            print('im result ', result)
            if leg['id'] == result['legislator_id']:
                if result['vote_type'] == 1:
                    counterYes += 1
                elif result['vote_type'] == 2:
                    counterNo += 1
                else:
                    pass
            else:
                pass
        auxInfo['yes_votes'] = counterYes
        auxInfo['no_votes'] = counterNo
        listFinal.append(auxInfo)
        
    for bill in bills_list:
        auxInfo = {}
        support = 0
        oppose = 0
        auxInfo['bill_id'] = bill['id']
        auxInfo['bill_title'] = bill['title']
        auxInfo['bill_sponsor'] = bill['sponsor_id']
        for result in vote_results_list:
            if result['vote_type'] == 1:
                support += 1
            elif result['vote_type'] == 2:
                oppose += 1
            else:
                pass
        for leg in legislators_list:
            if leg['id'] == bill['sponsor_id']:
                auxInfo['legislator_name'] = leg['name']
                auxInfo['legislator_id'] = leg['id']
                break
        auxInfo['support'] = support
        auxInfo['oppose'] = oppose
        listFinal2.append(auxInfo)
    return render_template('index.html', listFinal=listFinal, listFinal2=listFinal2)

if __name__ == '__main__':
    app.run(debug=True)