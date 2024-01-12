import URLOrganizer3

output, url = URLOrganizer3.scrapping_func()

class Categories1():

    def __init__(self, topic1 = ''):
        self.topic1 = topic1

    def name_change(self):
        list1 = ['archery', 'badminton', 'cricket', 'bowling', 'boxing', 'tennis', 'skateboard',
                 'surf', 'ice hockey', 'figure skating', 'yoga', 'dancing', 'fencing', 'gymnastics',
                 'karate', 'kung-fu', 'martial arts', 'taekwondo', 'weightlift', 'baseball', 'softball',
                 'rugby', 'football', 'wrestling', 'high jump', 'hang gliding', 'racing', 'cycling', 'run',
                 'track', 'table tennis', 'fishing', 'judo', 'climb', 'hiking', 'swim',
                 'horse', 'golf', 'soccer', 'diving', 'handball', 'tchoukball', 'snowboard', 'field hockey',
                 'skiing', 'speed skating', 'long jump', 'discus', 'javelin', 'hammer', 'pole vault', 'canoe',
                 'trampoline', 'dodgeball', 'zip lining', 'bungee', 'sky diving', 'sled', 'walk', 'jog',
                 'volleyball', 'curling', 'row', 'basketball', 'sport','recreation']
        while len(list1) > 0:
                self.topic1 = list1[0]
                if self.topic1 in output.lower():
                    print(f'Will be categorized under {self.topic1.upper()}.')
                    list1.pop(0)
                    result = input('Is that fine?')
                    if result.lower() in ['yes','y']:
                        return self.topic1.capitalize()
                    else:
                        continue
                else:
                    list1.pop(0)
        else:
            main_list = ['archery', 'badminton', 'cricket', 'bowling', 'boxing', 'tennis', 'skateboard', 'surf',
                         'ice hockey','figure skating', 'yoga', 'dancing', 'fencing', 'gymnastics', 'karate', 'kung-fu',
                         'martial arts', 'taekwondo','weightlift', 'baseball', 'softball', 'rugby', 'football', 'wrestling',
                         'high jump','hang gliding', 'racing','cycling', 'run', 'track', 'table tennis', 'fishing',
                         'judo', 'climb', 'hiking','swim', 'horse','golf', 'soccer', 'diving', 'handball', 'tchoukball',
                         'snowboard', 'field hockey', 'skiing','speed skating','long jump', 'discus', 'javelin', 'hammer',
                         'pole vault', 'canoe', 'trampoline', 'dodgeball','zip lining','bungee', 'sky diving', 'sled',
                         'walk', 'jog', 'volleyball', 'curling','row','basketball','sport','recreation']
            print([x.upper() for x in sorted(main_list)])
            self.topic1 = input('Sorry, an appropriate topic cannot be found. What would you like the topic to be then? Choose from above.')
            print('All Done!')
            return self.topic1.capitalize()
