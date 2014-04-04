import json
import sexmachine.detector as gender
from random import randint
from datetime import datetime, timedelta

delim = ","

d = gender.Detector(case_sensitive=False)

# read users file
yelp_users_file = open("yelp_training_set_user.json", "r")
yelp_users_raw_lines = yelp_users_file.readlines()
yelp_users_file.close()

# write the data we want into a pipe separated data file
pig_users_file = open("pig_set_user.txt", "w")
for user_line in yelp_users_raw_lines:
    json_user = json.loads(user_line)
    user_id = json_user["user_id"]
    user_name = json_user["name"]
    user_gender = d.get_gender(user_name).replace("mostly_", "").replace("andy", "unspecified")
    user_age = str(randint(18,70))
    user_printinfo = user_id + delim + user_name + delim + user_gender + delim + user_age
    pig_users_file.write(user_printinfo.encode('utf8') + "\n")
pig_users_file.close()

#read businesses file
yelp_business_file = open("yelp_training_set_business.json", "r")
yelp_business_raw_lines = yelp_business_file.readlines()
yelp_business_file.close()

# write the data we want into a pipe separated data file
pig_business_file = open("pig_set_business.txt", "w")
for business_line in yelp_business_raw_lines:
    json_business = json.loads(business_line)
    business_id = json_business["business_id"]
    business_name = json_business["name"]
    business_categories = json_business["categories"]
    for business_category in business_categories:
        business_printinfo = business_id + delim + business_name + delim + business_category
        pig_business_file.write(business_printinfo.encode('utf8') + "\n")
pig_business_file.close()


# read reviews file
yelp_reviews_file = open("yelp_training_set_review.json")
yelp_reviews_raw_lines = yelp_reviews_file.readlines()
yelp_reviews_file.close()

# write the data we want into a pipe seperated data file
pig_reviews_file = open("pig_set_reviews.txt", "w")
for reviews_line in yelp_reviews_raw_lines:
    json_review = json.loads(reviews_line)
    business_id = json_review["business_id"]
    user_id = json_review["user_id"]
    review_id = json_review["review_id"]
    review_date = json_review["date"]
    review_fact = json_review["stars"]
    for x in range(0,5):
        # mutate the fact by up to 25%
        fuzzed_review_fact = str(review_fact * ((randint(1, 50) + 75)/(100*1.0)))

        #mutate the date by up to 15 days
        review_date = (datetime.strptime(review_date, '%Y-%m-%d') + timedelta(days=randint(1,15))).strftime('%Y-%m-%d')

        review_printinfo = review_id + delim + business_id + delim + user_id + delim + fuzzed_review_fact + delim + review_date
        pig_reviews_file.write(review_printinfo.encode('utf8') + "\n")
pig_reviews_file.close()





