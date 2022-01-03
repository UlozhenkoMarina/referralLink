#token for telegram bot api
API_TOKEN = ''

#url for getting user identifier and name by referral link
getUserByLinkUrl = "http://127.0.0.1:8000/userByLink/"

#url for getting frequency of using incorrect referral link by user
getFrequencyByChat = "http://127.0.0.1:8000/amountByChat/"

#url for increasing frequency of using incorrect referral link by user
postFrequencyByChat = "http://127.0.0.1:8000/frequencyByUserIncrease/"

#maximum possible amount of using incorrect url by user
maxIncorrectAmount = 2