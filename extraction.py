import requests
import time
import os

data_dir = "F:\\zomato-master\\Zomato\\new_zomato_data1"

api_keys = "20b2f75b61122ae67c5c803d6819ac4e"

api_endpoint = "https://developers.zomato.com/api/v2.1/search"

# list of Establishment Id
establishment_type_list = []
filename = "F:\\zomato-master\\Zomato\\list_files\\establishment_id_list"
with open(filename,'r') as f:
    lines = f.readlines()
for line in lines:
    establishment_type_list.append(line.replace("\n",""))
#print(establishment_type_list) 

#List of Subzones in Pune
subzone_list = []
filename = "F:\\zomato-master\\Zomato\\list_files\\zomato subzone list.txt"
with open(filename,'r') as f:
    lines = f.readlines()
for line in lines:
    subzone_list.append(line.replace("\n","").replace(" ","%20"))
#print(subzone_list)


api_call_count = 0
# headers = {"user-key":api_keys[0],"Accept":"application/json"}
# print(headers)
i= 0

for subzone in subzone_list:
    data_path = data_dir+"\\"+subzone
    #print(data_path)
    if os.path.exists(data_path) == False:
        os.mkdir(data_path)
    for establishment_type in establishment_type_list:
        start=0
        while start <100: 
            print("This is start : ",start)
            headers = {"user-key":api_keys[i],"Accept":"application/json"}
            print(headers)
            url = api_endpoint + '?' + 'q=' +  subzone + '&'+'establishment_type=' + establishment_type + '&start=' + str(start)
            print(url)
            response = requests.get(url = url,headers = headers)
            api_call_count = api_call_count +1
            #print(response.text)
            # sample_response = '{"results_found":70,"results_start":0,"results_shown":1,"restaurants":[{"restaurant":{"R":{"has_menu_status":{"delivery":-1,"takeaway":-1},"res_id":19105279},"apikey":"20b2f75b61122ae67c5c803d6819ac4e","id":"19105279","name":"Vishay Snacks","url":"https:\/\/www.zomato.com\/pune\/vishay-snacks-nigdi?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1","location":{"address":"Guru Dwara Chowk, Akurdi Station, Opposite Manok Chowdry Classic, Nigdi, Pune","locality":"Nigdi","city":"Pune","city_id":5,"latitude":"18.6476915231","longitude":"73.7640691549","zipcode":"","country_id":1,"locality_verbose":"Nigdi, Pune"},"switch_to_order_menu":0,"cuisines":"Street Food","timings":"7 PM to 11 PM","average_cost_for_two":200,"price_range":1,"currency":"Rs.","highlights":["Cash","Takeaway Available","Dinner","Standing Tables","Indoor Seating","Digital Payments Accepted","Self Service"],"offers":[],"opentable_support":0,"is_zomato_book_res":0,"mezzo_provider":"OTHER","is_book_form_web_view":0,"book_form_web_view_url":"","book_again_url":"","thumb":"","user_rating":{"aggregate_rating":0,"rating_text":"Not rated","rating_color":"CBCBCB","rating_obj":{"title":{"text":"-"},"bg_color":{"type":"grey","tint":"400"}},"votes":0},"all_reviews_count":0,"photos_url":"https:\/\/www.zomato.com\/pune\/vishay-snacks-nigdi\/photos?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1#tabtop","photo_count":0,"menu_url":"https:\/\/www.zomato.com\/pune\/vishay-snacks-nigdi\/menu?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1&openSwipeBox=menu&showMinimal=1#tabtop","featured_image":"","has_online_delivery":0,"is_delivering_now":0,"include_bogo_offers":true,"deeplink":"zomato:\/\/restaurant\/19105279","is_table_reservation_supported":0,"has_table_booking":0,"events_url":"https:\/\/www.zomato.com\/pune\/vishay-snacks-nigdi\/events#tabtop?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1","phone_numbers":"+91 8087787375","all_reviews":{"reviews":[]},"establishment":["Food Court"],"establishment_types":{"establishment_type":{"id":"20","name":"Food Court"}}}}]}'
            # sample_response2 = '{"code":440,"status":"","message":"API limit exceeded"}'
                
            sample_response = response.text
                
            res_found = sample_response.find('results_found')
            #print(res_found)
            if res_found != -1:
                    
                ## store response in json file
                ## --> append in file named as 'subzone_establishmentID'
                filename = data_path+"\\"+subzone+"_"+establishment_type+".json"
                with open(filename,"a") as record:
                    # record.writelines(response.text)
                    record.writelines(sample_response)
                ##if results_found is less than 100
                ## --> reduce number of unnecessory api calls
                s = sample_response.split(",")[0].split(":")[1]
                #print(s)
                result_found_count = int(s)
                start = start +20
                if start > result_found_count:
                    print("start = ",start," Result Found = ",result_found_count)
                    break
            ## if API call limit exceeded change user_key
            ## --> use next key from api_keys list
            #if api_call_count == 3:
            if "API limit exceeded" in sample_response:
                #if "API limit exceeded" in response.text:
                print("api call count : ",api_call_count)
                print("start : ",start)
                print("i : ",i)
                api_call_count=0
                i = i+1
                print("new api call count : ",api_call_count)
                print("new start : ",start)
                print(" new i : ",i)
                del(response)
                del(sample_response)
                time.sleep(20)
                #print(i)
                    
                time.sleep(2)
            else:
                print("i out of bound")
                break
            
            
#{"code":440,"status":"","message":"API limit exceeded"}
            
            
#{"results_found":1,"results_start":0,"results_shown":1,"restaurants":[{"restaurant":{"R":{"has_menu_status":{"delivery":-1,"takeaway":-1},"res_id":19105279},"apikey":"20b2f75b61122ae67c5c803d6819ac4e","id":"19105279","name":"Vishay Snacks","url":"https:\/\/www.zomato.com\/pune\/vishay-snacks-nigdi?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1","location":{"address":"Guru Dwara Chowk, Akurdi Station, Opposite Manok Chowdry Classic, Nigdi, Pune","locality":"Nigdi","city":"Pune","city_id":5,"latitude":"18.6476915231","longitude":"73.7640691549","zipcode":"","country_id":1,"locality_verbose":"Nigdi, Pune"},"switch_to_order_menu":0,"cuisines":"Street Food","timings":"7 PM to 11 PM","average_cost_for_two":200,"price_range":1,"currency":"Rs.","highlights":["Cash","Takeaway Available","Dinner","Standing Tables","Indoor Seating","Digital Payments Accepted","Self Service"],"offers":[],"opentable_support":0,"is_zomato_book_res":0,"mezzo_provider":"OTHER","is_book_form_web_view":0,"book_form_web_view_url":"","book_again_url":"","thumb":"","user_rating":{"aggregate_rating":0,"rating_text":"Not rated","rating_color":"CBCBCB","rating_obj":{"title":{"text":"-"},"bg_color":{"type":"grey","tint":"400"}},"votes":0},"all_reviews_count":0,"photos_url":"https:\/\/www.zomato.com\/pune\/vishay-snacks-nigdi\/photos?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1#tabtop","photo_count":0,"menu_url":"https:\/\/www.zomato.com\/pune\/vishay-snacks-nigdi\/menu?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1&openSwipeBox=menu&showMinimal=1#tabtop","featured_image":"","has_online_delivery":0,"is_delivering_now":0,"include_bogo_offers":true,"deeplink":"zomato:\/\/restaurant\/19105279","is_table_reservation_supported":0,"has_table_booking":0,"events_url":"https:\/\/www.zomato.com\/pune\/vishay-snacks-nigdi\/events#tabtop?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1","phone_numbers":"+91 8087787375","all_reviews":{"reviews":[]},"establishment":["Food Court"],"establishment_types":{"establishment_type":{"id":"20","name":"Food Court"}}}}]}
