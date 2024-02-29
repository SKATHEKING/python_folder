from TikTokApi import TikTokApi
import pandas as pd
api = TikTokApi.get_instance()




def inputUserID():
  userName = input("Enter Username: ")
  userInfo = api.get_user(userName)
  userID = userInfo['id']
  secUID = userInfo['secUid']
  return userID, secUID

def getUserVideos(userDefID, secDefUID):
  # Sets up a few variables that will be used throughout the code
  cursorValue = 0
  hasMore = True
  df = pd.DataFrame()  # Function to pull video data until all have been pulled
  while hasMore:
    # Makes initial call to the API
    TikTokList = api.user_page(userID=userDefID,
    secUID=secDefUID,
    cursor=cursorValue)    # Function used to clean
    data = cleanData(TikTokList['itemList'])
    df = df.append(data)    # updates our variables based on the latest scrape
    cursorValue = int(TikTokList['cursor'])
    hasMore = TikTokList['hasMore']
  else:
    print("No more data")
    df.to_csv('UserVideos.csv')

def cleanData(data):
  nested_values = ['video', 'author', 'music', 'stats', 'authorStats']
  # Creates a dictionary for our df to be stored in
  flattened_data = {}
  for id, value in enumerate(data):
    flattened_data[id] = {}
    # Loop through each element
    for prop_id, prop_value in value.items():
      #Check if nested
      if prop_id in nested_values:
        for nested_id, nested_value in prop_value.items():
          flattened_data[id][prop_id + '_' + nested_id] = nested_value
      # If it's not nested, add it back to the flattened dictionary
        else:
            flattened_data[id][prop_id] = prop_value

    return pd.DataFrame.from_dict(flattened_data, orient='index')

#userInfo = inputUserID()
#getUserVideos(userInfo[0], userInfo[1])