from data import randomuser_data


def get_full_names(data: dict) -> list[str]:
    """
    Returns a list of users' full names in 'First Last' format.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        list[str]: List of full names.
    """
    
    #TODO map()  bilan ishlashi

    result = map(lambda text: {"first": text['name']['first'], "last": text['name']['last']}, randomuser_data['results'])
    return list(result)



    #TODO for bilan ishlagani

    #useres = data['results']
    # full_names = list()
    # for user in useres:
    #     name = user['name']
    #     first_name = name['first']
    #     last_name = name['last']

    #     full_names.append(f"{first_name} {last_name}")

    # return full_names


def get_users_by_country(data: dict, country: str) -> list[dict]:
    """
    Filters and returns users who live in a specific country.

    Args:
        data (dict): JSON data containing user records.
        country (str): Country name to filter by.

    Returns:
        list[dict]: List of dictionaries containing full name and email of matching users.
    """
    
    filtered_users = filter(
        lambda user:user['location']['country'].lower() == country.lower(),
        data['results']
    )

    users = list(map(
        lambda user:{"name":user['name']['first'], "email":user['email']},
        filtered_users
    ))
    
    return users
   
    
    # user_list = list()
    # for user in data['results']:
    #     if user['location']['country'] == country:
    #         user_list.append(user)
    
    # return user_list


def count_users_by_gender(data: dict) -> dict:
    """
    Counts the number of users by gender.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        dict: Dictionary with gender as keys and count as values.
    """
    
    males = list(filter(
        lambda user: user['gender'].lower() == 'male',
        data['results']
    ))

    females = list(filter(
        lambda user: user['gender'].lower() == 'famale',
        data['results']
    ))

    return {
        "male": len(males),
        "female": len(females)
    }

    #TODO for bilan ishlangani
    
    '''geder_list = list()
    for user in data['results']:
        if user['gender'] == 'male':
            print('name')
        # if user['gender'] == 'female':
        #     print('name')

        geder_list.append(user)
    return geder_list'''


def get_emails_of_older_than(data: dict, age: int) -> list[str]:
    """
    Returns a list of emails of users older than the given age.

    Args:
        data (dict): JSON data containing user records.
        age (int): Age threshold.

    Returns:
        list[str]: List of email addresses.
    """
    
    filtered_users = filter(
        lambda user: user['dob']['age'] > age,
        data['results']
    )

    users = list(map(
        lambda user: user['email'],
        filtered_users
    ))
    
    return users
    
    
    #TODO for bilan ishlangani
    '''users = data['results']
    email_list= list()

    for user in users:
        if user['dob']['age'] >= age:
            email = user['email']
            email_list.append(email)

    return email_list'''


def sort_users_by_age(data: dict, descending: bool = False) -> list[dict]:
    """
    Sorts users by age in ascending or descending order.

    Args:
        data (dict): JSON data containing user records.
        descending (bool, optional): Whether to sort in descending order. Defaults to False.

    Returns:
        list[dict]: List of users with name and age sorted accordingly.
    """

    sorted_users = sorted(
        data['results'],
        key = lambda user: user['dob']['age'],
        reverse=descending
    )

    users = list(map(
        lambda user:{"name":user['name']['first'], "age":user['dob']['age']},
        sorted_users
    ))
    
    return users

def get_usernames_starting_with(data: dict, letter: str) -> list[str]:
    """
    Returns a list of usernames starting with a given letter.

    Args:
        data (dict): JSON data containing user records.
        letter (str): The starting letter to filter usernames.

    Returns:
        list[str]: List of matching usernames.
    """
    
    filtered_users = filter(
        lambda user: user['login']['username'].startswith(letter),
        data['results']
    )
    
    users = list(map(
        lambda user: user['login']['username'],
        filtered_users
    ))
    
    return users
    
        
    #TODO for bilan ishlanishi
    users = data['results']
    list_startswith = list()
    for user in users:
        username = str(user['login']["username"])
        if username.startswith(letter):
          list_startswith.append(username)
        if not username.startswith(letter):
            return "username not defined"
    
    return list_startswith


def get_average_age(data: dict) -> float:
    """
    Calculates and returns the average age of users.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        float: Average age.
    """
    
    ages = list(map(
        lambda user:user['dob']['age'],
        data['results']
    ))
    
    return sum(ages) / len(ages)
    
    
    
    
    #TODO for bilan ishlangani 
    '''orta_y = list()
    user_age = 0

    users = data['results']
    for user in users:
        user_age += user['dob']['age']
        n = float(user_age / 10)
    print(n)
    orta_y.append(n)
    return orta_y
'''



def group_users_by_nationality(data: dict) -> dict:
    """
    Groups and counts users by their nationality.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        dict: Dictionary with nationality as keys and count as values.
    """
    
    group = dict()
    for user in data['results']:
        if user['nat'] not in group.keys():
            group[user['nat']] = 1
        else:
            group[user['nat']] += 1

    return group
    
    #TODO for bilan ishlangani
    # user_list = list()
    # user_nl = 0
    # user_in = 0
    # user_ie = 0
    # user_rs = 0
    # user_nat = list()
    # users = data['results']
    # for user in users:
    #     if user['nat'] == "NL":
    #         user_nl += 1
    #     if user['nat'] == "IN":
    #         user_in += 1
    #     if user['nat'] == "IE":
    #         user_ie += 1
    #     if user['nat'] == "RS":
    #         user_rs += 1
    # print("NL:",user_nl, "IE:",user_ie, "RS:",user_rs, "IN:",user_in)
        




def get_all_coordinates(data: dict) -> list[tuple[str, str]]:
    """
    Extracts all users' coordinates as tuples of (latitude, longitude).

    Args:
        data (dict): JSON data containing user records.

    Returns:
        list[tuple[str, str]]: List of coordinate tuples.
    """
    
    coordinates = list(map(
        lambda user: (user['location']['coordinates']['latitude'], user['location']['coordinates']['longitude']),
        data['results']
    ))
    return coordinates
    #TODO for bilan ishlangani
    users = data['results']
    cor_list = list()
    for user in users:
        cor = user['location']['coordinates']
        print(cor)
        cor_list.append(cor)
    return cor_list
    




def get_oldest_user(data: dict) -> dict:
    """
    Finds and returns the oldest user's name, age, and email.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        dict: Dictionary containing 'name', 'age', and 'email' of the oldest user.
    """

   
    user = max(
        data['results'],
        key=lambda user: user['dob']['age']
    )  
    return user 
   
    # age_list = list()
    # users = data['results']
    # for user in users:
    #     if user["dob"]["age"] >= 80:
    #         print(user['email'])
    # age_list.append(user)

    # return age_list

        
        
    


def find_users_in_timezone(data: dict, offset: str) -> list[dict]:
    """
    Returns users whose timezone offset matches the given value.

    Args:
        data (dict): JSON data containing user records.
        offset (str): Timezone offset (e.g. '+5:30').

    Returns:
        list[dict]: List of users with full name and city.
    """
    pass


def get_registered_before_year(data: dict, year: int) -> list[dict]:
    """
    Returns users who registered before a given year.

    Args:
        data (dict): JSON data containing user records.
        year (int): Year threshold.

    Returns:
        list[dict]: List of users with full name and registration date.
    """
    pass


def run_functions() -> None:
    """
    Runs and prints results of all data processing functions for demonstration purposes.
    
    """
    #TODO
    #print("Users by country:", get_users_by_country(randomuser_data,"Netherlands"))
    #TODO
    #print("Full names",get_full_names(randomuser_data))
    #TODO
    #print("Gender",count_users_by_gender(randomuser_data))
    #TODO 
    # age_enter = int(input("yoshi >> "))
    # print("Enter email",get_emails_of_older_than(randomuser_data,age_enter))
    #TODO
    #print(sort_users_by_age(randomuser_data))
    #TODO
    # letter = input()
    # print("Enter login",get_usernames_starting_with(randomuser_data,letter))
    #TODO
    # print("orta yoshlar",get_average_age(randomuser_data))
    #TODO
    #print(group_users_by_nationality(randomuser_data))
    #TODO
    #print("cordinatalari",get_all_coordinates(randomuser_data))
    #TODO
    #print("age email",get_oldest_user(randomuser_data))



run_functions()
